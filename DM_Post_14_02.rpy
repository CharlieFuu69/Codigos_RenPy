## ElectroBasicsYT - CharlieFuu69 Creations! (2020)
## Script Utility : Código para hacer Solicitudes Web en un juego Ren'Py

###############################################################

## NOTAS DE ESTE ARCHIVO :

## ESTE ARCHIVO ES UNA MODIFICACIÓN DEL CÓDIGO QUE APARECE EN EL TUTORIAL DE DITECNOMAKERS.

## Si quieres probar este archivo, haz un nuevo proyecto en Ren'Py y cuando se termine de crear,
## borra el archivo "script.rpy" para que no te de problemas al ejecutar.
## Recuerda que este código funcionará si proporcionas correctamente el link del archivo JSON
## alojado en tu servidor.

## Este código, y el módulo Requests, solo operarán con links de tipo HTTP, no HTTPS.
## Recuerda tener ya ubicado la carpeta "python-packages" dentro de la carpeta "game" de tu
## juego.
## Si no tienes el módulo en las carpetas del juego, este script, junto con tu juego, arrojará error.

## Este código no funciona con hilos, por lo que puede generar detenciones en el juego.
## Para evitar el crasheo del juego, recomiendo usar "threading" para ejecutar las solicitudes.

## Obten el RAR con los archivos del módulo Requests, desde este link :
## https://mega.nz/file/4IljCILQ#da32pKUQ0QMha4_WesjoxuXt_qwHkNdXXEJcE4Uht04

###############################################################
## CÓDIGO (Modificación alternativa mejor organizada)
###############################################################

default Network_Data = None

## PASO 1 : Importar los módulos necesarios para hacer las solicitudes y para procesar el JSON
## alojado en tu server.
init python:
    import requests
    import json
    
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
    $ Request_Function("Escribe tu URL aquí")

    ## PASO 2 : Mostrar el texto recibido, interpolando en una cadena.
    "[Network_Data]"

    return # Fin del juego
