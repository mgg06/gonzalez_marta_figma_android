from pathlib import Path
import json, math, xml.etree.ElementTree as ET

BASE = Path(__file__).resolve().parents[1]
RES = BASE / 'app/src/main/res'
ANDROID = '{http://schemas.android.com/apk/res/android}'
APP = '{http://schemas.android.com/apk/res-auto}'
design = json.loads((BASE / 'docs/verificacion/figma-copia-auditoria.json').read_text(encoding='utf-8'))
nodes = {n['id']: n for n in design}
layout = ET.parse(RES / 'layout/activity_inicio_sesion.xml').getroot()
views = {n.get(ANDROID+'id', '').split('/')[-1]: n for n in layout.iter() if n.get(ANDROID+'id')}
styles = {n.get('name'): {i.get('name'): i.text for i in n} for n in ET.parse(RES/'values/styles.xml').getroot()}
strings = {n.get('name'): n.text for n in ET.parse(RES/'values/strings.xml').getroot()}
colors = {n.get('name'): n.text.upper() for n in ET.parse(RES/'values/colors.xml').getroot()}
dimens = {n.get('name'): n.text for n in ET.parse(RES/'values/dimens.xml').getroot()}

def value(s):
    if s and s.startswith('@string/'):
        return strings[s.split('/')[-1]]
    return s

def hexcolor(paints):
    p = next(p for p in paints if p['type'] == 'SOLID' and p.get('visible', True))
    c = p['color']
    return '#' + ''.join(f'{round(v*255):02X}' for v in [p.get('opacity',1),c['r'],c['g'],c['b']])

entries = [
 ('46:736','tv_titulo_inicio_sesion',False),
 ('46:739','tv_nombre_pequeno',False),
 ('46:748','tv_tipo_tienda',False),
 ('46:751','tv_nombre_centro',False),
 ('I46:753;52798:24886','et_correo_electronico',False),
 ('I46:753;52798:24888','til_correo_electronico',True),
 ('I46:755;52798:24886','et_contrasena',False),
 ('I46:755;52798:24888','til_contrasena',True),
 ('46:757','btn_recuperar_contrasena',False),
 ('46:762','tv_texto_terminos',False),
 ('I46:763;58653:14019','btn_iniciar_sesion',False),
 ('46:766','tv_o_entra_con',False),
 ('I46:769;58650:11132','btn_acceder_google',False),
 ('I46:777;58650:11132','btn_acceder_davante',False),
 ('46:780','tv_pregunta_registro',False),
 ('46:781','btn_crear_cuenta',False),
 ('46:783','btn_entrar_sin_sesion',False),
]
records=[]
for source_id, target_id, label in entries:
    source=nodes[source_id]
    view=views[target_id]
    style_id=view.get(APP+'hintTextAppearance' if label else 'style').split('/')[-1]
    style=styles[style_id]
    text=value(view.get(ANDROID+('hint' if label else 'text')) or view.get(ANDROID+'hint'))
    if style.get('android:textAllCaps')=='true':
        text=text.upper()
    font=style['android:fontFamily'].split('/')[-1]
    weight=500 if font=='roboto_medium' else 400
    android_color=colors[style['android:textColor'].split('/')[-1]]
    spacing=source['letterSpacing']['value']/source['fontSize']
    checks={
      'texto':text==source['text'],
      'fuente':source['fontName']['family']=='Roboto' and font in ('roboto_regular','roboto_medium'),
      'peso':weight==source['fontName'].get('variationSettings',{}).get('wght',500 if source['fontName']['style']=='Medium' else 400),
      'tamano':float(style['android:textSize'][:-2])==source['fontSize'],
      'interlineado':float(style['android:lineHeight'][:-2])==source['lineHeight']['value'],
      'color':android_color==hexcolor(source['fills']),
      'espaciado':math.isclose(float(style['android:letterSpacing']),spacing,abs_tol=0.000001),
    }
    assert all(checks.values()), (source_id,target_id,checks)
    records.append({'figma':source_id,'android':target_id,'estilo':style_id,'comprobaciones':checks})

color_sources={
 'fondo':('46:723','fills'),
 'texto_principal':('46:736','fills'),
 'acento':('46:737','fills'),
 'texto_sobre_acento':('46:739','fills'),
 'superficie_acceso_google':('I46:769;58650:11129','fills'),
 'borde_control':('I46:753;52798:24882','strokes'),
 'texto_campo':('I46:753;52798:24886','fills'),
 'texto_secundario':('I46:753;52798:24888','fills'),
 'superficie_acceso_davante':('I46:777;58650:11129','fills'),
}
assert set(colors)==set(color_sources)
for name,(node_id,property_name) in color_sources.items():
    assert colors[name]==hexcolor(nodes[node_id][property_name]),name
mapped_nodes=[n for n in design if n['name'].startswith(('ly_','tv_','iv_','et_','btn_','cb_','v_'))]
assert len(mapped_nodes)==30
assert all(n['name'] in views for n in mapped_nodes)
assert dimens['margen_pantalla']=='16dp'
assert dimens['alto_panel_marca']=='120dp'
assert dimens['radio_panel_marca']=='20dp'
assert nodes['46:737']['height']==120 and nodes['46:737']['cornerRadius']==20
assert dimens['alto_cabecera']=='64dp' and nodes['46:734']['height']==64
assert dimens['alto_campo']=='56dp' and nodes['46:753']['height']==56
assert dimens['radio_campo']=='4dp' and nodes['I46:753;52798:24882']['cornerRadius']==4
assert dimens['alto_area_tactil']=='48dp'
assert dimens['alto_visual_boton']=='40dp' and nodes['I46:763;58653:14016']['height']==40
assert dimens['espacio_entre_accesos']=='8dp' and nodes['46:775']['height']==8
assert dimens['separacion_campos']=='12dp' and nodes['46:754']['height']==12
report={'textos':records,'colores':colors,'dimensiones':dimens,'resultado':'17 textos y 9 recursos de color contrastados con la copia de Figma y los XML actuales','diferencias':[
 'Figma: marco fijo 360 x 800, Android: ancho adaptable y desplazamiento con limite de 512 dp para el contenedor exterior',
 'Figma: separaciones de 16 y 12 entre los bordes de panel/campos, Android: margenes de contenedores de 8 y 4 dp, mas el espacio automatico de las etiquetas Material',
 'Figma: radio 100 para la capsula principal, Android: radio 24 dp, limitado visualmente por la mitad de su altura',
 'Android: campos minHeight 56 dp y botones minHeight 48 dp con wrap_content, la altura puede crecer',
 'Android: colores de foco y estados de pulsacion, no representan valores de una captura estatica de Figma',
]}
(BASE/'docs/verificacion/auditoria-tablas-android-figma.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(report['resultado'])
