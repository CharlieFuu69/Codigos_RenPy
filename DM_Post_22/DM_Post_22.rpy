## ElectroBasicsYT - CharlieFuu69 Creations!
## Script Utility : Recuperador de URL final de descargas de Mediafire

## ADVERTENCIA : Este script necesita del script DM_Post_18_02.rpy para funcionar.
##               obtén el script actualizado con instrucciones de uso, en esta URL :
##               >> https://github.com/CharlieFuu69/Codigos_RenPy/tree/master/DM_Post_18

#############################################################
## SECCIÓN 1 : EXTRACTOR DE URLS

init python:
    import re ## RegEx (Expresiones regulares).
    import requests ## Solicitudes web.
    import ssl ## Capa de seguridad del Host.
    import threading ## Ejecución en hilos.

    class DownloadFetch(threading.Thread):

        def __init__(self, shared_url, file_extension):
            """Inicializa y construye los atributos de la clase."""

            super(DownloadFetch, self).__init__()
            self.daemon = True ## Ejecuta el hilo como un daemon

            self.shared_url = shared_url ## La URL compartida
            self.file_extension = file_extension ## La extension del archivo objetivo

            self.fetch_finish = False ## Bandera de recuperación terminada
            self.url_end = None ## La URL definitiva extraida
            self.fetch_exception = None ## Bandera de excepciones

        def fetch_finished(self):
            """Retorna bool si la recuperación ha terminado o no."""
            return self.fetch_finish

        def end_url(self):
            """Retorna la URL final de descarga."""
            return self.url_end

        def runtime_exception(self):
            """Retorna bool si hubo una excepción o no, durante la recuperación."""
            if isinstance(self.fetch_exception, Exception):
                return True
            return False

        def raise_now(self):
            """Retorna el cuerpo de la excepción."""
            if self.runtime_exception():
                raise self.fetch_exception

        def run(self):
            """Realiza el raspado (Scrap) de la URL compartida."""

            ## Encabezados para pasar en solicitud GET
            headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

            print("> Adquiriendo URL...")
            try:
                ssl._create_default_https_context = ssl._create_unverified_context

                r = requests.get(self.shared_url, headers = headers)
                url = re.findall('"((http|ftp)s?://.*?)"', r.text)

                for i in url:
                    if i[0].endswith(self.file_extension):
                        self.url_end = i[0] ## La URL final encontrada
                    else:
                        pass

            except Exception as fetcherr:
                ## ¿Ha ocurrido un error?
                self.fetch_exception = fetcherr
                print("> Error al recuperar la URL de descarga :", type(fetcherr))

            finally:
                ## Finalmente...
                self.fetch_finish = True
                renpy.restart_interaction()
                print("> Proceso de extraccion finalizado.")

#############################################################
## SECCIÓN 2 : DISEÑO DE UI Y ACCIÓN DEL EXTRACTOR DE URL

screen DownloadSetup(url, extension, download_dir):

    ## Llama a la clase y pasa los argumentos necesarios para funcionar.
    default dl = DownloadFetch(url, extension)

    on "show" action Function(dl.start) ## Inicia el hilo, poniendo en marcha al método run().

    frame:
        xsize 700
        ysize 400
        xpos 0.25
        ypos 0.2

        ## ¿Terminó la recuperación?
        showif dl.fetch_finished():

            ## ¿Ocurrió un error durante la recuperación?
            showif dl.runtime_exception():
                ## add "IC_Warning" zoom 1.8 xalign 0.5 ypos 0.17
                vbox:
                    xsize 700
                    ypos 0.45
                    spacing 15

                    text "¡Woops! Hubo un error durante la conexión :(" xalign 0.5
                    null height 25
                    textbutton "Mostrar excepción" action Function(dl.raise_now) xalign 0.5 ypos 0.58
                    textbutton "Volver al Menú Principal" action MainMenu() xalign 0.5 ypos 0.58

            ## Si no ocurrió un error, procede a la descarga con la URL obtenida
            else:
                timer 0.01 action [
                Hide("DownloadSetup"),

                ## La screen de descarga será llamado y se pasarán los siguientes argumentos.
                ## url = El método que retorna la URL final
                ## out = La ruta física donde se descargará el archivo.
                Show("download_screen", url = dl.end_url(), out = download_dir)]

        ## Si aún no termina la recuperación...
        else:
            ## add "IC_Connecting" zoom 0.7 xalign 0.5 ypos 0.1
            vbox:
                xsize 700
                ypos 0.5
                spacing 15

                text "Preparando la descarga..." xalign 0.5
                text "Este proceso puede tardar unos segundos."xalign 0.5
