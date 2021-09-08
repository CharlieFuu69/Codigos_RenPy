## ElectroBasicsYT - CharlieFuu69 Creations!
## Script Utility : Descargador de archivos con módulo WGET.

###############################################################

## NOTAS DE ESTE ARCHIVO :

## Si quieres probar este archivo, haz un nuevo proyecto en Ren'Py y cuando se termine de crear,
## sustituye el archivo "script.rpy" por este archivo.

## WGET puede operar con URLs de rango HTTP y HTTPS. Si tu servidor o host no tiene certificados
## de seguridad, escribe las URL solo como HTTP.

## Si no tienes para costear un host, hazte una cuenta en 000Webhost. Es un host gratuito que
## ofrece mas o menos 300 MB de espacio en disco y 3 GB de ancho de banda mensual.
## Link : https://www.000webhost.com/

## Este código ejecuta la descarga de un archivo usando hilos para no interrumpir el funcionamiento
## de Ren'Py.

## Los archivos se descargarán por defecto, en la carpeta raíz del motor Ren'Py.

## Todas las imágenes agregadas con "add" y "scene" han sido comentadas para evitar problemas
## en el código. Si posees iconos en tus archivos, puedes añadirlos con "add".

##############################################################
## CÓDIGO DEL SISTEMA DE DESCARGAS
##############################################################

init python:
    ## Desde aquí se puede incrustar código escrito en Python

    import threading ## Procesamiento en hilos
    import wget ## El módulo que ejecuta las descargas
    from os import path ## Modulo para asignar las rutas de salida

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

                    # add "IC_Warning" zoom 1.8 xalign 0.5 ypos 0.17
                    text "Hubo un error al descargar el archivo :(" xalign 0.5 ypos 0.48
                    textbutton "Volver al Menú Principal" action MainMenu() xalign 0.5 ypos 0.58

                    ## Añade este botón para observar con detalle el error.
                    ## textbutton "Mostrar/Rastrear el error" action Function(Download_Action._raise_from_thread) xalign 0.5 ypos 0.68

            else:
                ## Bloque de código que se muestra cuando la descarga finaliza.
                frame:
                    xmaximum 700
                    ymaximum 400
                    xsize 700
                    ysize 400

                    xpos 0.25
                    ypos 0.2

                    # add "IC_Connecting" zoom 0.7 xalign 0.5 ypos 0.17
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

                # add "IC_Connecting" zoom 0.7 xalign 0.5 ypos 0.1
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
    # scene Game_Background

    $ link = "Escribe aquí tu URL"
    $ path = "Escribe aquí el nombre de tu archivo a descargar"

    ## Llama a la screen
    ## Parámetros en orden : URL del archivo - Ruta de salida o nombre del archivo
    call screen download_screen(link, path)
    return
