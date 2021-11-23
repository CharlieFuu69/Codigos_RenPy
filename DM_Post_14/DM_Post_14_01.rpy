## ElectroBasicsYT - CharlieFuu69 Creations!
## Script Utility : Código para hacer Solicitudes Web en un juego Ren'Py

###############################################################

## NOTAS DE ESTE ARCHIVO :

## Si quieres probar este archivo, haz un nuevo proyecto en Ren'Py y cuando se termine de crear,
## borra el archivo "script.rpy" para que no te de problemas al ejecutar.

## Este código, y el módulo Requests, solo operarán con links de tipo HTTP, no HTTPS.
## El código funcionará si proporcionas correctamente la URL del archivo JSON alojado en
## tu servidor.
## Recuerda tener ya ubicado la carpeta "python-packages" dentro de la carpeta "game" de tu
## juego.
## Si no tienes el módulo en las carpetas del juego, este script, junto con tu juego, arrojará error.

## No he agregado un método para hacer las solicitudes con hilos, por lo que puede generar
## detenciones en el juego mientras se contacta al servidor.
## Para evitar el crasheo del juego, recomiendo usar "threading" para ejecutar las solicitudes.

## Recomiendo revisar el archivo "DM_Post_14_02.rpy" en este repositorio.
## El código presente en ese archivo está mejor organizado, ya que se simplifican las solicitudes
## mediante un llamado a una función.

## Si no tienes para costear un host, hazte una cuenta en 000Webhost. Es un host gratuito que
## ofrece mas o menos 300 MB de espacio en disco y 3 GB de ancho de banda mensual.
## Link : https://www.000webhost.com/

## Obten el RAR con los archivos del módulo Requests, desde este link :
## https://mega.nz/file/4IljCILQ#da32pKUQ0QMha4_WesjoxuXt_qwHkNdXXEJcE4Uht04

###############################################################
## CÓDIGO (Presente en el tutorial de DitecnoMakers)
###############################################################

## PASO 1 : Importar los módulos necesarios para hacer las solicitudes y para procesar el JSON
## alojado en tu server.
init python:
    import requests
    import json

label start:

    # Muestra texto centrado
    show text "Conectando..." at truecenter

    # Apertura del bloque Python
    python:
        ## Bloques try/except para manejar futuros errores
        try:
            link = "Aquí va la URL de tu solicitud"
            data = requests.get(link) # Solicitud
            data.encoding = "utf-8" # Codificación como UTF-8

            lectura = json.loads(data.text) # Decodificación del JSON
            text_output = lectura["texto_mamadisimo"] # Extracción del texto final

            # Impresión en consola
            print("Respuesta del servidor :", data) # Imprime la respuesta del server
            print("JSON Decodificado :", text_output) # Imprime el texto decodificado

            network_status = True # Señala que hay conexión exitosa

        except:
            data = "Conexión Débil" # Indica conexión fallida
            print("Respuesta del servidor :", data) # Imprime la respuesta

            network_status = False # Señala que no hay conexión exitosa

    ## PASO 2 : Mostrar el texto recibido, interpolando en una cadena
    if network_status:
        # Si 'network_status' es True, mostrará el texto decodificado en el cuadro de diálogos
        "[text_output]"

    else:
        # Si 'network_status' es False, no se mostrará la variable 'text'
        "No se obtuvo ninguna p*ta respuesta. Tu conexión es una auténtica mierda xD"

    return # Fin del juego
