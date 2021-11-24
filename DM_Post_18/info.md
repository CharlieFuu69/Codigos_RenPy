# (Leeme) Notas de los scripts del Post #18

¡Hola! Si quieres usar el sistema de descargas que he creado, te recomiendo que uses el script [DM_Post_18_02.rpy](https://github.com/CharlieFuu69/Codigos_RenPy/blob/37deda9adccc27600f02f144763719ecc295f7c4/DM_Post_18/DM_Post_18_02.rpy), pues es una versión mejorada que incluye compatibilidad tanto para Windows como Android.

### Importante para Ports de Ren'Py (Android) :
Ren'Py al parecer no posee el módulo "termios", por lo que si descargas el módulo "WGET" desde webs como PyPI, te va a dar problemas al iniciar una descarga.
Te recomiendo que uses la versión modificada de "WGET" con el que no tendrás problemas para usar en Android. [Presiona aquí](https://github.com/CharlieFuu69/Codigos_RenPy/blob/37deda9adccc27600f02f144763719ecc295f7c4/DM_Post_18/wget.py) para descargar el módulo con las modificaciones necesarias.

---

### Instrucciones para implementar el sistema de descargas :

* __Paso 1 : Instalación de WGET en tu juego__
Descarga WGET desde la URL señalada en el apartado "Importante para Ports de Ren'Py (Android)". Al descargarlo, crea una carpeta llamada `python-packages` y coloca el archivo `wget.py` en su interior.

* __Paso 2 : Instalación del sistema de descargas__
Descarga el script que contiene el sistema de descargas y colócalo en el interior de la carpeta `game` de tu proyecto.

* __Paso 3 : ¡Cuidado con el "label start"!__
El script del sistema de descargas ofrecido en este repositorio, trae consigo un fragmento de muestra de cómo se puede emplear las descargas dentro del `label start`.
Si vas a instalar el sistema de descargas en un proyecto que ya estás creando, reacomoda la llamada de la screen `download_screen()` en el interior del código de tu juego, según te sea más cómodo, y elimina el `label start` del script que contiene el sistema de descargas.
¡No puedes definir más de 1 `label start"` en tu juego! ¡Eso te arrojará una excepción!

---

### ¿Cómo usar y/o probar el sistema de descargas, una vez instalado? :

Para usar el sistema de descargas, sigue este ejemplo :

```renpy
label start:
    ## scene Game_Background

    $ link = "Escribe aquí tu URL"
    $ path = SEARCHPATH + "Escribe en esta string el nombre de tu archivo a descargar"

    menu:
        "Descargar archivo de Audio":
            jump Download_Section

    label Download_Section:
        ## Llama a la screen de descarga con sus dos parámetros.
        call screen download_screen(link, path)
        return
```
