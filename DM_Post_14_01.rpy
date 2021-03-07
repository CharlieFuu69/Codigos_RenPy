## ElectroBasicsYT - CharlieFuu69 Creations! (2020)
## Script Utility : Código para hacer Solicitudes Web en un juego Ren'Py

###############################################################

## NOTAS DE ESTE ARCHIVO :

## Si quieres probar este archivo, haz un nuevo proyecto en Ren'Py y cuando se termine de crear,
## borra el archivo "script.rpy" para que no te de problemas al ejecutar.
## Recuerda que este código funcionará si proporcionas correctamente el link del archivo JSON
## alojado en tu servidor.

## Si no tienes para costear un host, hazte una cuenta en 000Webhost mediante este link :
## https://www.000webhost.com/?__cf_chl_jschl_tk__=f1a74f7b7ca2dbcf49737158bb602b3e31e28d54-1599864700-0-ATamotvZDbFWKZO7_3H48hiTqWMhJHkDje54UC5hJ6Iux9JB8gaFaZLkHF-RwbNmvB0AmApBs6Phkdz4gCbSwaXRFjnLStfh_8f2S0xuzuJwvBOnEqfrdSF9SfqCQCv8kk8b45UURJVy7JeoRAiwy9_FL17xfgPMrsj3vqff3JZFZ2av4S162XE4IzdV5t4bl6eUEJDTC4d_OxrvpgjqsajEeM8dNwBsqjCJAb74R12ES-REOXhgpVjIYCzIMhGvIaArxXOWEWOfpEXV6BUgVr4

## Este código, y el módulo Requests, solo operarán con links de tipo HTTP, no HTTPS.
## Recuerda tener ya ubicado la carpeta "python-packages" dentro de la carpeta "game" de tu
## juego.
## Si no tienes el módulo en las carpetas del juego, este script, junto con tu juego, arrojará error.

## Este código no funciona con hilos, por lo que puede generar detenciones en el juego.
## Para evitar el crasheo del juego, recomiendo usar "threading" para ejecutar las solicitudes.

## Obten el RAR con los archivos del módulo Requests, desde este link :
## https://mega.nz/file/4IljCILQ#da32pKUQ0QMha4_WesjoxuXt_qwHkNdXXEJcE4Uht04

###############################################################
## CÓDIGO (Presente en el tutorial de DitecnoMakers
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

    ## PASO 2 : Mostrar el texto recibido en la sintasis de Ren'Py
    if network_status:
        # Si 'network_status' devuelve True, mostrará el texto decodificado en el cuadro de diálogos
        "[text_output]"

    else:
        # Si 'network_status' devuelve False, no se mostrará la variable 'text'
        "No se obtuvo ninguna p*ta respuesta. Tu conexión es una auténtica mierda xD"

    return # Fin del juego
