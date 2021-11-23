## ElectroBasicsYT - CharlieFuu69 Creations!
## Script Utility : Descargador de archivos con módulo WGET. (Código Alternativo)

###############################################################

## NOTAS DE ESTE ARCHIVO :

## IMPORTANTE : Este archivo es una modificación del sistema de descargas del Post #18.
## Este a diferencia del código anterior, puede ejecutar descargas tanto en Windows como
## también en Android, ya que se ha aplicado un detector híbrido de Searchpaths, el cual
## provee la ruta de descarga según el sistema operativo donde esté arrancando el juego.

## IMPORTANTE PARA COMPILAR EN ANDROID : Si descargas el módulo WGET desde webs
## como PyPI, es posible que la descarga presente el error "no module named termios".
## He modificado el código de WGET para que no hayan problemas en Android.
## Adjuntaré el script "wget.py" para que lo puedas descargar.
## Link : https://mega.nz/file/xVcnUYxI#iUg3e7tQnl5oJaToLsL4lANNc_jtCVGzW7jsWB90lGQ

## Si quieres probar este archivo, haz un nuevo proyecto en Ren'Py y cuando se termine de crear,
## borra el archivo "script.rpy" para que no te de problemas al ejecutar. Recuerda que no pueden
## haber dos "label start" dentro de un juego Ren'Py.

## WGET puede operar con URLs de rango HTTP y HTTPS. Si tu servidor o host no tiene certificados
## de seguridad, escribe las URL solo como HTTP.

## Si no tienes para costear un host, hazte una cuenta en 000Webhost. Es un host gratuito que
## ofrece mas o menos 300 MB de espacio en disco y 3 GB de ancho de banda mensual.
## Link : https://www.000webhost.com/

## Este código ejecuta la descarga de un archivo usando hilos para no interrumpir el funcionamiento
## de Ren'Py.

## Todas las imágenes agregadas con "add" y "scene" han sido comentadas para evitar problemas
## en el código. Si posees iconos en tus archivos, puedes añadirlos con "add".

#############################################################
## SECCIÓN 1 : DETECTOR HÍBRIDO DE SEARCHPATH
#############################################################

init python:
    ## Desde aquí se puede incrustar código escrito en Python

    import os ## Módulo que interactúa con el sistema operativo.

    ## El valor de esta variable tendrá más adelante una string con el Searchpath detectado
    ## Por defecto al inicializar, será None.
    SEARCHPATH = None

    def Gamedir_Setup():
        """Esta función actualiza a la variable SEARCHPATH con la ruta de la carpeta /game
        del dispositivo en donde se arranca el juego.
        En Android, esta función preparará una carpeta "game" virtual en la ruta pública y
        actualizará la variable "SEARCHPATH" con la ruta "game" en Android."""

        global SEARCHPATH

        ## ¿El sistema operativo es Android?
        if renpy.android:
            ## ¿Existe la carpeta /game en la ruta pública? Si existe, no se hace nada. Si no existe,
            ## ¡pues hagámosla!
            if os.path.exists(os.environ["ANDROID_PUBLIC"] + "/game"):
                pass
            else:
                os.mkdir(os.environ["ANDROID_PUBLIC"] + "/game")

            ## Actualiza la variable con la ruta /game en Android
            SEARCHPATH = os.environ["ANDROID_PUBLIC"] + "/game"

        ## ¿El sistema operativo es Windows?
        elif renpy.windows:
            ## En Windows, las rutas se separan por un "Backslash". La variable se actualizará
            ## de inmediato con la ruta separada con slash normales o "Forward Slash".
            SEARCHPATH = config.gamedir.replace(os.sep, "/")


    ## Llama la función en el arranque. En este punto, la variable SEARCHPATH ya tendrá la
    ## ruta /game detectada en el sistema operativo utilizado.
    Gamedir_Setup()


    ############################################################
    ## SECCIÓN 2 : SISTEMA DE DESCARGAS CON WGET.
    ############################################################

    import threading ## Procesamiento en hilos
    import wget ## El módulo que ejecuta las descargas
    from os import path ## Modulo para asignar las rutas de salida
    import ssl

    class WGET_Assets_Downloader(threading.Thread):

        def __init__(self, url, out=None):
            """Inicializa los atruibutos de la clase y recibe los parámetros de descarga.
            url:
                El URL del archivo en tu servidor.
            out:
                La ruta de salida del archivo."""

            super(WGET_Assets_Downloader, self).__init__()
            self.daemon = True

            self.__url = url
            self.__out = out

            self.__actual = None
            self.__target = None

            self.__download_status = None
            self.__is_finished = False

            self.__exception = None
            self.__result_filename = None

        @property
        def status(self):
            """Retorna el porcentaje descargado"""
            return (self.__download_status or .0)

        @property
        def MB_Actual(self):
            """Retorna los Megabytes descargados"""
            return (self.__actual or .0)

        @property
        def MB_Target(self):
            """Retorna el tamaño total del archivo"""
            return (self.__target or .0)

        @property
        def _filename(self):
            """Retorna el nombre asignado al archivo"""
            return self.__result_filename

        def download_is_finished(self):
            """Retorna cuando finaliza la descarga"""
            return self.__is_finished

        def _has_exception(self):
            """Retorna -True- si se presenta un error en la descarga"""
            if isinstance(self.__exception, Exception):
                return True
            return False

        def _raise_from_thread(self):
            """(Opcional) Permite rastrear el error mediante un archivo Traceback"""
            if self._has_exception():
                raise self.__exception

        def _callback_func(self, current, total, *args, **kwargs):
            """Calcula el progreso de la descarga."""
            current, total = map(float, (current, total))
            if total > .0:
                self.__download_status = (current / total)
                self.__actual = round((current / 1048576), 2)
                self.__target = round((total / 1048576), 2)
                renpy.restart_interaction()

        def run(self):
            """Inicia la descarga"""
            ssl._create_default_https_context = ssl._create_unverified_context
            try:
                _result_fn = wget.download(
                    self.__url,
                    self.__out,
                    bar=self._callback_func
                )
            except Exception as ex:
                self.__exception = ex
                self.__download_status = .0
            else:
                self.__result_filename = path.abspath(_result_fn)
            finally:
                self.__is_finished = True
                renpy.restart_interaction()


screen download_screen(url, out=None):

    ## Invoca a la clase y pasa los parámetros de la Screen como sus argumentos.
    default Download_Action = WGET_Assets_Downloader(url, out)

    ## Indica si la descarga ha iniciado.
    default _Download_Activity = False

    showif _Download_Activity:
        showif Download_Action.download_is_finished():
            showif Download_Action._has_exception():
                ## Bloque de código que se muestra cuando ocurre un error en la descarga.
                frame:
                    xmaximum 700
                    ymaximum 400
                    xsize 700
                    ysize 400

                    xpos 0.25
                    ypos 0.2

                    ## add "IC_Warning" zoom 1.8 xalign 0.5 ypos 0.17
                    text "Hubo un error al descargar el archivo :(" xalign 0.5 ypos 0.48
                    textbutton "Volver al Menú Principal" action MainMenu() xalign 0.5 ypos 0.58
                    textbutton "Mostrar/Rastrear el error" action Function(Download_Action._raise_from_thread) xalign 0.5 ypos 0.68

            else:
                ## Bloque de código que se muestra cuando la descarga finaliza.
                frame:
                    xmaximum 700
                    ymaximum 400
                    xsize 700
                    ysize 400

                    xpos 0.25
                    ypos 0.2

                    ## add "IC_Connecting" zoom 0.7 xalign 0.5 ypos 0.17
                    text "¡Descarga Completa!" xalign 0.5 ypos 0.48
                    textbutton "Volver al Menú Principal" action MainMenu() xalign 0.5 ypos 0.58
        else:
            ## Bloque de código que se muestra cuando hay una descarga en curso.
            frame:
                xmaximum 700
                ymaximum 400
                xsize 700
                ysize 400

                xpos 0.25
                ypos 0.2

                ## add "IC_Connecting" zoom 0.7 xalign 0.5 ypos 0.1
                text "Descargando recursos..." xalign 0.5 ypos 0.36
                text "Progreso : {0} MB / {1} MB".format(Download_Action.MB_Actual, Download_Action.MB_Target) xalign 0.5 ypos 0.6

                hbox:
                    xalign 0.5
                    ypos 0.73
                    spacing 20
                    bar:
                        xmaximum 350
                        value AnimatedValue(Download_Action.status, 1.)

                    text "[[{0:.1%}]".format(Download_Action.status)
    else:
        ## Bloque de código que se muestra cuando aún no se inicia la descarga.
        frame:
            xalign 0.5 yalign 0.5
            button:
                action [
                Function(Download_Action.start),
                SetScreenVariable("_Download_Activity", True)]
                text _("Iniciar descarga") style "button_text"

## Aquí empieza tu juego
## ADVERTENCIA : Si ya posees un "label start" en tu código, omite el "label start" que verás acá
## de otro modo obtendrás un error.

label start:
    ## scene Game_Background

    $ link = "Escribe aquí tu URL"
    $ path = SEARCHPATH + "Escribe en esta string el nombre de tu archivo a descargar"

    menu:
        "Descargar archivo de Audio":
            jump Download_Section

        "Reproducir audio descargado":
            jump Test_Audio

        "Ir al menú principal":
            return

    label Download_Section:
        ## Llama a la screen de descarga con sus dos parámetros.
        call screen download_screen(link, path)
        return

    label Test_Audio:
        ## Llama al archivo de audio que se descargó en la carpeta /game
        play music "Aquí va el nombre del archivo de audio a reproducir"

        ## Muestra una string con la ruta del archivo de audio mientras el juego la reproduce
        "Reproduciendo audio...\nRuta de archivo : [path]"

        jump start
