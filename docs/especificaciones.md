# Ficha contrastada con Figma y Android

Copia de desarrollo: https://www.figma.com/design/EsUftS945DYUInVenDYTTj?node-id=46-723

## Colores

| Nombre funcional | Hexadecimal Android | Dónde se usa |
|---|---|---|
| "fondo" | #FFF5F8FD | Fondo de la pantalla y de las etiquetas flotantes |
| "texto_principal" | #FF17243D | Título, términos y flecha de regreso |
| "acento" | #FF0234AB | Panel de marca, botón principal, enlaces e icono Davante |
| "texto_sobre_acento" | #FFFFFFFF | Nombre, tipo de tienda, rótulo del centro y botón principal |
| "superficie_acceso_google" | #FFFFFFFF | Fondo del acceso con Google, mismo valor con otra función |
| "borde_control" | #FFD7DFEA | Bordes de campos y botones secundarios y líneas del separador |
| "texto_campo" | #FF49454F | Textos de ejemplo de los campos y contorno del control de aceptación |
| "texto_secundario" | #FF475569 | Etiquetas de campos, separador y pregunta de registro |
| "superficie_acceso_davante" | #FFEAF1FC | Fondo del acceso con Davante |

## Tipografía

He contrastado los nueve recursos de color y los 17 textos con la copia de Figma y con los archivos actuales del proyecto. Los textos coinciden en fuente, peso, tamaño, interlineado, color y espaciado entre letras. La fuente de la aplicación sigue siendo "Roboto". "Courier New" se utiliza aquí para presentar los nombres técnicos, no como un valor de la interfaz

| ID Android y texto visible | Fuente y peso | Tamaño | Interlineado | Color |
|---|---|---|---|---|
| "tv_titulo_inicio_sesion" / "Inicia sesión" | "Roboto" 500 Medium | 20 sp | 26 sp | #FF17243D |
| "tv_nombre_pequeno" / "PEQUEÑO" | "Roboto" 500 Medium | 11 sp | 17 sp | #FFFFFFFF |
| "tv_tipo_tienda" / "Ropa infantil" | "Roboto" 400 Regular | 12 sp | 18 sp | #FFFFFFFF |
| "tv_nombre_centro" / "MEDAC SEVILLA ESTE" | "Roboto" 500 Medium | 9 sp | 15 sp | #FFFFFFFF |
| "et_correo_electronico" / "Tu correo electrónico" | "Roboto" 400 Regular | 16 sp | 24 sp | #FF49454F |
| "til_correo_electronico" (etiqueta) / "Correo electrónico" | "Roboto" 400 Regular | 12 sp | 16 sp | #FF475569 |
| "et_contrasena" / "Tu contraseña" | "Roboto" 400 Regular | 16 sp | 24 sp | #FF49454F |
| "til_contrasena" (etiqueta) / "Contraseña" | "Roboto" 400 Regular | 12 sp | 16 sp | #FF475569 |
| "btn_recuperar_contrasena" / "¿Has olvidado tu contraseña?" | "Roboto" 500 Medium | 14 sp | 20 sp | #FF0234AB |
| "tv_texto_terminos" / "Acepto los términos y condiciones" | "Roboto" 400 Regular | 13 sp | 20 sp | #FF17243D |
| "btn_iniciar_sesion" / "Iniciar sesión" | "Roboto" 500 Medium | 14 sp | 20 sp | #FFFFFFFF |
| "tv_o_entra_con" / "o entra con" | "Roboto" 400 Regular | 12 sp | 20 sp | #FF475569 |
| "btn_acceder_google" / "Continuar con Google" | "Roboto" 500 Medium | 14 sp | 20 sp | #FF0234AB |
| "btn_acceder_davante" / "Entrar con mi cuenta Davante" | "Roboto" 500 Medium | 14 sp | 20 sp | #FF0234AB |
| "tv_pregunta_registro" / "¿Es tu primera visita?" | "Roboto" 400 Regular | 14 sp | 20 sp | #FF475569 |
| "btn_crear_cuenta" / "Crear cuenta" | "Roboto" 500 Medium | 14 sp | 20 sp | #FF0234AB |
| "btn_entrar_sin_sesion" / "Seguir sin iniciar sesión" | "Roboto" 500 Medium | 14 sp | 20 sp | #FF0234AB |

## Medidas

En esta tabla separo las medidas de Figma y los valores que están escritos en Android. Las primeras están en px del prototipo y las segundas en dp del layout. El marco de 360 × 800 es una referencia, mientras que la app adapta su ancho y permite desplazarse. Los campos tienen un alto mínimo de 56 dp y los botones de 48 dp, por lo que pueden crecer al aumentar el tamaño de letra

La separación de los campos también depende de las etiquetas de "TextInputLayout". En Figma hay 16 px antes del primer campo y 12 px entre los dos. En el XML están definidos márgenes de 8 y 4 dp en los contenedores, más el espacio que añade Material para la etiqueta. Por eso anoto ambos valores y no los presento como si fueran la misma medida

| Elemento | Tamaño en Figma (px) | Radio Figma / Android (px / dp) | Espacios en Figma (px) | Valor real en Android (dp) |
|---|---|---|---|---|
| Marco de referencia | 360 × 800 | 0 / 0 | Padding 0 | Ancho y alto adaptables, scroll exterior limitado a 512 |
| Margen lateral | 16 a cada lado, 328 útiles | No tiene radio, es espacio | 16 a cada lado | Padding lateral 16 en el contenedor de desplazamiento |
| Cabecera | 328 × 64 | 0 / 0 | 16 entre el área de vuelta y el título | Alto 64, vuelta 48 × 48 y padding del icono 16 |
| Panel de marca y centro | 328 × 120 | 20 / 20 | Marca: 18 inicio, 12 final y 3 entre elementos | Alto 120, marca 55,4878 % y foto 44,5122 % del ancho |
| Logo Davante | 148 × 40,150623 | 0 / 0 | 3 antes y después del logo | Alto 40,15, ancho adaptable y ajuste proporcional con "fitStart" |
| Fotografía | 146 × 120 | 0 propio / 0 propio | Padding 0, dentro del panel con radio 20 | Alto 120, ancho restante y recorte "centerCrop" |
| Rótulo del centro | 146 × 24 | 0 / 0 | y=96 sobre la foto, texto centrado | Alto 24, pegado al borde inferior de la fotografía |
| Separación panel y formulario | 16 | No tiene radio, es margen | 16 entre panel y borde del campo | Margen superior 8 antes de "TextInputLayout", más su espacio de etiqueta |
| Campos de texto | 328 × 56 | 4 / 4 | 16 al inicio del texto y 12 entre campos | Alto mínimo 56, padding lateral 16 y margen 4 entre contenedores más etiqueta, borde 1 normal y 2 enfocado |
| Recuperar contraseña | 328 × 48 | 0 del grupo / 24 del botón transparente | Texto alineado al final | Alto mínimo 48, padding horizontal 0, vertical 10 e insets verticales 4 |
| Aceptación de términos | 328 × 48, círculo 20 × 20 | 10 del círculo / 10 del círculo | Área del control 48 y separación de texto 4 | Control 48 × 48, padding lateral 14 y margen de texto 4 |
| Botón principal | 328 × 48, forma visible de alto 40 | 100 / 24, limitados por la altura | 16 horizontal y 10 vertical en la capa visible | Alto mínimo 48, padding 16 horizontal y 10 vertical, insets 4 arriba y abajo |
| Separador de accesos | 328 × 32, líneas 112 × 1 | 0 / 0 | 10 a los lados y 12 entre línea y texto | Alto 32, líneas de grosor 1 y ancho repartido con peso 1 |
| Acceso Google | 328 × 48, forma visible de alto 40 | 24 / 24 | Icono 20 × 20 en x=20, y=14 | Alto mínimo 48, icono 20 × 20, padding inicio 20 y final 40 |
| Separación Google y Davante | 8 | No tiene radio, es margen | 8 entre las áreas de acceso | Margen superior 8 en el botón Davante |
| Acceso Davante | 328 × 48, forma visible de alto 40 | 24 / 24 | Icono 18,105009 × 20 en x=20, y=14 | Alto mínimo 48, icono 18,105 × 20, padding inicio 20 y final 38,105 |
| Registro e invitado | 328 × 48 por fila | 0 del grupo / 24 del botón transparente | 5 entre la pregunta y "Crear cuenta" | Alto mínimo 48 por fila, separación 5 en el registro |
| Barras del sistema | 360 × 24 superior e inferior | 0 del grupo, indicador 2 / gestión del sistema | Indicador 108 × 4, x=126, y=10 dentro de la barra inferior | Altura proporcionada por los insets de Android, no fijada a 24 |
