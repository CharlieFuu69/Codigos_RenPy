## ElectroBasicsYT - CharlieFuu69 Creations!
## Script Utility : Detector híbrido de Searchpaths y código alternativo del sistema de descargas.

###############################################################

## NOTAS DE ESTE ARCHIVO :

## El código funciona tanto para Windows como tambien para Android. El sistema de descargas
## también funciona en Android así que es posible gestionar Assets externos en Android.

## Este archivo contiene el código listo para implementarlo en la característica que quieras
## crear. Basta que coloques este archivo en la carpeta /game de tu juego y podrás usar su
## código sin problemas.

## El código alternativo del sistema de descargas consiste en agregar este mismo código para
## realizar la descarga del archivo pero en el interior de la carpeta /game. Encuéntralo en
## el siguiente link de GitHub!
## Link : https://github.com/CharlieFuu69/Codigos_RenPy/blob/0b494f3c6d9e658839da4cf1095252e8a726980b/DM_Post_18_02.rpy

##############################################################
## CÓDIGO DETECTOR HÍBRIDO DE SEARCHPATHS
##############################################################

init python:
    ## Desde aquí se puede incrustar código escrito en Python

    import os ## Módulo que interactúa con el sistema operativo.

    SEARCHPATH = None ## La variable que apunta a la carpeta /game

    def Gamedir_Setup():
        """Esta función actualiza a la variable SEARCHPATH con la ruta de la carpeta /game
        del dispositivo en donde se arranca el juego.
        En Android, esta función preparará una carpeta "game" virtual en la ruta pública y
        actualizará la variable "SEARCHPATH" con la ruta "game" en Android."""

        global SEARCHPATH ## Considera a SEARCHPATH como una variable global.

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
