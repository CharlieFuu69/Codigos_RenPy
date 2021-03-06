## ElectroBasicsYT - CharlieFuu69 Creations!
## Script Utility : Código para hacer Solicitudes Web en un juego Ren'Py

###############################################################

## NOTAS DE ESTE ARCHIVO :

## ESTE ARCHIVO ES UNA MODIFICACIÓN DEL ARCHIVO "DM_Post_14_01.rpy".
## RECOMIENDO USAR EL CÓDIGO DE ESTE ARCHIVO POR SOBRE EL CÓDIGO DEL ARCHIVO
## MENCIONADO ANTERIORMENTE.

## Este código, y el módulo Requests, solo operarán con links de tipo HTTP, no HTTPS.
## El código funcionará si proporcionas correctamente la URL del archivo JSON alojado en
## tu servidor.
## Recuerda tener ya ubicado la carpeta "python-packages" dentro de la carpeta "game" de tu
## juego.
## Si no tienes el módulo en las carpetas del juego, este script, junto con tu juego, arrojará error.

## No he agregado un método para hacer las solicitudes con hilos, por lo que puede generar
## detenciones en el juego mientras se contacta al servidor.
## Para evitar el crasheo del juego, recomiendo usar "threading" para ejecutar las solicitudes.

## Si no tienes para costear un host, hazte una cuenta en 000Webhost. Es un host gratuito que
## ofrece mas o menos 300 MB de espacio en disco y 3 GB de ancho de banda mensual.
## Link : https://www.000webhost.com/

## Obten el RAR con los archivos del módulo Requests, desde este link :
## https://mega.nz/file/4IljCILQ#da32pKUQ0QMha4_WesjoxuXt_qwHkNdXXEJcE4Uht04

###############################################################
## CÓDIGO (Modificación alternativa mejor organizada)
###############################################################

## PASO 1 : Importar los módulos necesarios para hacer las solicitudes y para procesar el JSON
## alojado en tu server.
init python:
    import requests
    import json

    Network_Data = ""

    ## PASO 2 : Crea una función para llamar desde el juego en otro momento.
    def Request_Function(url):
        """Esta función genera una solicitud web para obtener texto de un JSON.
        El parámetro -url- recibe como argumento, una string con la URL del archivo
        JSON."""

        global Network_Data

        try:
            resp = requests.get(url, timeout = 10)
            resp.encoding = "utf-8"

            ## Lee la respuesta JSON
            lectura = json.loads(resp.text)

            ## Extrae el texto desde el JSON, presente en "texto_mamadisimo"
            Network_Data = lectura["texto_mamadisimo"]

            print("Respuesta del servidor :", resp) # Imprime la respuesta del server
            print("JSON Decodificado :", Network_Data) # Imprime el texto decodificado

        except:
            Network_Data = "No se ha recibido ninguna respuesta"


## Aquí comienza tu juego
label start:

    # Muestra texto centrado
    show text "Conectando..." at truecenter
    $ renpy.pause(2.0, hard = True)

    ## Llama a la función, proporcionando la URL del JSON
    $ Request_Function("Escribe la URL del JSON aquí")

    ## PASO 2 : Mostrar el texto recibido, interpolando en una cadena.
    "[Network_Data]"

    return # Fin del juego
