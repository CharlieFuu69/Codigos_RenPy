## ElectroBasicsYT - CharlieFuu69 Creations!
## Script Utility : Verificador Online de Actualizaciones para juegos Ren'Py

###############################################################

## NOTAS DE ESTE ARCHIVO :

## Si quieres probar este archivo, basta con que lo coloques en tu proyecto y va a funcionar.
## Mucha atención si ya tenías un "label splashscreen" en tu proyecto. En ese caso será mejor
## que hagas algunas modificaciones para evitar errores en el arranque del juego.

## El módulo "Requests" puede operar con URLs de rango HTTP y HTTPS. Si tu servidor o host
## no tiene certificados de seguridad, escribe las URL solo como HTTP.

## Si no tienes para costear un host, hazte una cuenta en 000Webhost. Es un host gratuito que
## ofrece mas o menos 300 MB de espacio en disco y 3 GB de ancho de banda mensual.
## Link : https://www.000webhost.com/

## Todas las imágenes agregadas y "scene" han sido comentadas para evitar problemas en el
## código.

#############################################################
## SECCIÓN 1 : [PYTHON] SOLICITUDES WEB Y VERIFICADOR DE ACTUALIZACIONES
#############################################################

default Update_Beacon = False ## Variable por defecto

init python:
    ## Desde aquí puedes incrustar código escrito en Python

    import requests ## Módulo para hacer las solicitudes web
    import json ## Módulo para procesar el objeto JSON recibido desde la solicitud web.

    def Update_Checker(url):
        """Esta función ejecuta una solicitud web hacia un archivo JSON. Este archivo JSON debe
        contener la versión del juego, o bien, las nuevas versiones que vayas publicando de tu
        juego para así decirle a tus jugadores que hay una nueva versión para actualizar.

        La función necesita que le pases los siguientes parámetros :

            - url : String con la URL de tu archivo JSON.
        """
        global Update_Beacon ## Considera esta variable como variable de alcance global

        try:
            ## Aquí va tu solicitud web. Tiempo de espera máximo : 10 Segundos.
            data = requests.get(url, timeout = 10)
            data.encoding = "utf-8" ## Los datos recibidos están codificados como UTF-8

            try:
                json_digest = json.loads(data.text) ## Aquí se procesa el objeto JSON recibido.

                ## CONDICIONAL : ¿La versión del servidor es la misma que la versión del juego?
                ## Si es así, no debe saltar la alerta de actualización.
                if json_digest["game_version"] == config.version:
                    persistent.Update_Beacon = False
                else:
                    persistent.Update_Beacon = True

            except:
                ## ¿Error al procesar el JSON? Hacer como que no hay ninguna actualización.
                persistent.Update_Beacon = False
        except:
            ## ¿Errores de conexión? Hacer como que no hay ninguna actualización.
            persistent.Update_Beacon = False

    ## Llama a la función anterior en el arranque, colocando la URL de tu JSON.
    Update_Checker("http://URL_DE_TU_SERVIDOR.com/control_de_versiones.json")


#############################################################
## SECCIÓN 2 : [REN'PY] UI DE LA VENTANA DE ALERTA
#############################################################

screen Update_Alert():

    ## Esto dibuja un recuadro de 700x150 píxeles en la pantalla
    frame:
        xsize 700 ysize 150
        xalign 0.5 yalign 0.5
        vbox:
            xalign 0.5
            ypos 0.3
            text "¡Hay una nueva actualización disponible del juego!" xalign 0.5
            text "Actualiza para obtener nuevas características" xalign 0.5

    ## Esto contiene los botones de acción para mostrar
    hbox:
        xalign 0.5 yalign 0.8
        spacing 50
        frame:
            ## Esto redirige a mi Gameblog. Cambia la URL por la URL de tu blog o de la tienda de apps.
            textbutton "Descargar Actualización" action OpenURL("https://eeqproject.blogspot.com")

        frame:
            ## Esto cierra el recuadro y opcional, redirige al menú principal del juego.
            textbutton "Cerrar aviso" action [Hide("Update_Alert"), MainMenu(confirm = False)]


#############################################################
## SECCIÓN 3 : [REN'PY] ALERTA DE ACTUALIZACIÓN EN PANTALLA DE BIENVENIDA
#############################################################

label splashscreen:
    ## Agrega una imagen si así lo desas
    ## scene Game_Background

    ## CONDICIONAL : ¿Hay una actualización disponible?
    if persistent.Update_Beacon:
        call screen Update_Alert
    else:
        pass

    return
