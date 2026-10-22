# Inventario de recursos

| Capa o elemento | ¿Se exporta? | Formato o solución | Nombre y carpeta en Android | Justificación |
|---|---|---|---|---|
| Logo Davante | Sí | SVG a "VectorDrawable" | drawable/ / "ic_logo_davante.xml" | Un solo recurso para los siete trazados, mantiene la nitidez |
| Icono de volver | Sí | SVG a "VectorDrawable" | drawable/ / "ic_volver.xml" | Solo la flecha, sin exportar el área táctil de 48 dp |
| Icono Google | Sí | SVG a "VectorDrawable" | drawable/ / "ic_google.xml" | Mantiene los cuatro colores del prototipo, el estilo utiliza "iconTint" con valor "@null" |
| Icono Davante de acceso | Sí | SVG a "VectorDrawable" | drawable/ / "ic_davante.xml" | Símbolo vectorial separado del logo completo |
| Fotografía MEDAC Sevilla Este | Sí | PNG 3x a WebP | drawable-xxhdpi/ / "img_medac_sevilla_este.webp" | 438 × 360 px, se exporta solo la foto, sin rótulo ni panel |
| Panel azul, cápsulas y bordes | No | Fondos y componentes XML | No genera asset | No convertir fondos y controles en imágenes |
| Líneas del separador | No | "View" de 1 dp en el layout | No genera asset | Son geometría simple |
| Texto del centro y demás textos | No | "strings.xml" y estilos | values | Conservan traducción, legibilidad y escalado |
| Control de términos y sus dos estados | No | "MaterialCheckBox" y su estado | No genera asset | Un control, no dos capturas de marcado y desmarcado |
| Espacios de 12 y 8 | No | Márgenes | values/"dimens.xml" | No son contenido gráfico |
| Hora, cobertura, wifi y batería | No | Sistema Android | No genera asset | No pertenecen a la interfaz propia de la app |
| Indicador de gestos | No | Sistema Android | No genera asset | Lo dibuja el sistema |

La guía pide obtener los logos de terceros de su página oficial. He comprobado que el recurso oficial actual de Google utiliza un degradado, mientras que el prototipo lleva la versión anterior de cuatro colores. He conservado el icono original en la copia de Figma y en Android para mantener el mismo diseño. Por tanto, este recurso coincide con el prototipo, pero no con la versión oficial actual, y dejo indicada esa diferencia
