# (Leeme) Notas de los scripts del Post #22

¡Hola! Este script se encarga de extraer la URL definitiva de un archivo de Mediafire, para que el sistema de descarga de Assets del [Post #18](https://ditecnomakers.com/programando-juegos-vn-con-renpy-18/) (DitecnoMakers) sea capaz de descargarlo.
Es necesario el script [DM_Post_18_02.rpy](https://github.com/CharlieFuu69/Codigos_RenPy/blob/37deda9adccc27600f02f144763719ecc295f7c4/DM_Post_18/DM_Post_18_02.rpy) para que funcione correctamente. Está actualizado asi que recomiendo descargar el script desde el hipervínculo anterior.

---

### Instrucciones para colocar el Extractor de URLs y usarlo desde el sistema de descargas :

* __1. Instalación de WGET en tu juego (Importante) :__
Descarga el módulo WGET que está en la carpeta [DM_Post_18](https://github.com/CharlieFuu69/Codigos_RenPy/tree/master/DM_Post_18). Al descargarlo, crea una carpeta llamada `python-packages` y coloca el archivo `wget.py` en su interior.

* __2. Instalación del sistema de descargas :__
Descarga el script que contiene el sistema de descargas que está en la carpeta [DM_Post_18](https://github.com/CharlieFuu69/Codigos_RenPy/tree/master/DM_Post_18) y colócalo en la carpeta `/game` de tu proyecto.

* __3. Instalación del Extractor de URLs :__
Al igual que como hiciste con el script del sistema de descargas, descarga el script [DM_Post_22.rpy](https://github.com/CharlieFuu69/Codigos_RenPy/blob/master/DM_Post_22/DM_Post_22.rpy) y colócalo en la carpeta `/game` de tu proyecto.

* __4. Edita el fragmento de código de ejemplo en el sistema de descargas :__
Para que este extractor funcione, debes modificar un par de líneas del fragmento de ejemplo. Las modificaciones que debes hacer, puedes verlas tanto en el Post #22 (el tutorial) y también más abajo en las instrucciones de uso.

---

### ¿Cómo usar/modificar el fragmento de ejemplo del sistema de descargas? :

Para usar el sistema de descargas junto a este extractor, coloca los dos scripts más el módulo WGET en las carpetas que se señalaron. Luego modifica el fragmento de ejemplo en el script [DM_Post_18_02.rpy](https://github.com/CharlieFuu69/Codigos_RenPy/blob/37deda9adccc27600f02f144763719ecc295f7c4/DM_Post_18/DM_Post_18_02.rpy) de la siguiente forma :

```renpy
label start:
    ## scene Game_Background

    $ link = "Coloca aqui la URL compartida del archivo alojado en Mediafire"
    $ file_extension = "Coloca aquí la extensión del archivo a descargar" ## Ejemplos: .mp3 | .ogg | .webm | .rpa | .rpyc
    $ path = SEARCHPATH + "Coloca aquí el nombre del archivo" ## Ejemplo : "/Snow_Halation.mp3"

    menu:
        "Descargar archivo de Audio":
            jump Download_Section

    label Download_Section:
        ## Llama a la screen que extrae la URL con sus 3 parámetros.
        call screen DownloadSetup(link, file_extension, path)
        return
```
