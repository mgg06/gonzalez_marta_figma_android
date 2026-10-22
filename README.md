# Pequeño Davante - Inicio de sesión en Android

Proyecto de la pantalla «00 Inicio de sesión» para la actividad «Del prototipo al código (I)» de Desarrollo de Interfaces, 2.º DAM

El proyecto incluye los recursos del diseño y la pantalla de inicio de sesión construida con vistas Android

Los campos permiten escribir, la contraseña se oculta y la aceptación de términos se puede marcar o desmarcar

Los botones muestran un aviso de demostración, no existe una conexión con servicios de autenticación ni se guardan credenciales

## Configuración

- Java y vistas XML
- Minimum SDK 28
- compileSdk 36.1 y targetSdk 36
- ViewBinding activado
- InicioSesionActivity y activity_inicio_sesion.xml
- Tema Material 3 claro, con colores de Pequeño Davante

## Recursos

colors.xml, strings.xml, styles.xml, themes.xml y dimens.xml contienen los valores del diseño, res/font incluye Roboto Regular 400 y Medium 500 y la licencia está en LICENCIA-Roboto.txt

Los iconos están en drawable como VectorDrawable y la fotografía del centro en drawable-xxhdpi como WebP de 438 × 360 px

## Abrir y ejecutar

Abre esta carpeta con Android Studio, deja que se configure la ruta del SDK y sincroniza Gradle, ejecuta la app en un dispositivo o emulador compatible, se muestra la pantalla de inicio de sesión

El contenido respeta las barras del sistema y se puede desplazar cuando aparece el teclado o falta altura

Los nombres de las vistas corresponden al árbol de la memoria, el contenedor raíz conserva el identificador "main" y la agrupación interior utiliza "ly_inicio_sesion"

Desde una terminal con JDK y SDK configurados también puedes usar gradlew.bat assembleDebug lintDebug en Windows

La carpeta ZIP de entrega no incluye build, .gradle ni local.properties, Android Studio regenerará esos archivos locales
