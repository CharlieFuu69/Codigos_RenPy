## ElectroBasicsYT - CharlieFuu69 Creations!
## Script Utility : Countdown para menús de elección en Ren'Py
## (Countdown Numérico + Barra animada)

##############################################################

## NOTAS DE ESTE ARCHIVO :

## Este archivo corresponde al Post #17 del hilo "Programando Juegos VN con Ren'Py!", en el
## que se hacen ciertas modificaciones al archivo del Post #16.

## No coloques directamente este archivo en tu proyecto. Puede generar errores poc contener
## un "label start". Intenta acomodar el código de este archivo en tu proyecto, o bien, haz
## un nuevo proyecto, elimina el archivo "script.rpy" y reemplaza por este archivo.

## Para que el countdown funcione correctamente, debes realizar algunas modificaciones
## a la "screen choice(items)" presente en el archivo "screens.rpy" de tu proyecto.
## Más abajo dejaré comentado el fragmento de código de ese archivo para que puedas
## hacer las modificaciones correspondientes, sin cometer errores en el intento.

##############################################################
## CÓDIGO DEL COUNTDOWN
##############################################################

init python:
    ## Aquí se puede incrustar código escrito en Python.

    ## Aquí empieza la función del Countdown
    def Countdown_Display_Function(st, at, length=0.0):
        """Esta función se encarga de retornar la cuenta regresiva mediante el displayable Text().
        El parámetro -length- al ser llamado, recibe como argumento una cifra numérica de coma
        flotante o un entero, que corresponde a la duración que tendrá la cuenta regresiva"""

        ## Esta variable obtiene el tiempo restante
        remaining = length - st

        ## Estas dos variables obtienen el tiempo en Minutos y Segundos, que servirán para
        ## formatear un contador regresivo como [00:00]
        m = (int) (length - st) / 60
        s = (int) (length - st) % 60

        ## Retorna un objeto Text() con los minutos y segundos restantes
        ## La palabra clave -color- recibe como argumento el color que tendrá el contador
        ## numérico, y -size- determina el tamaño de la fuente de texto.
        return Text("%02d:" % m + "%02d" % s, color="#FFF", size=30), .1

## Screen del Countdown
screen Countdown_Displayer(time_left, label_dest):
    ## Parámetros
    ## time_left : Tiempo del countdown en segundos (Valor Flotante)
    ## label_dest : El label a donde se transferirá el control del juego (String)

    vbox:
        xalign 0.5
        yalign 0.8
        xsize 740
        spacing 20

        ## Dentro del vbox, llamaremos a la función de la cuenta regresiva usando
        ## DynamicDisplayable(), el cual entrega a la screen, la cuenta regresiva como
        ## un objeto de imagen.
        add DynamicDisplayable(Countdown_Display_Function, length = time_left) xalign 0.5

        bar value AnimatedValue(old_value = 1.0, value = 0.0, range = 1.0, delay = time_left)

    timer time_left action [Hide("Countdown_Displayer"), Jump(label_dest)]

## Aquí empieza tu juego
label start:
    ## Llamada de la screen
    ## Parámetros (time_left, label_dest)
    show screen Countdown_Displayer(21.0, "Player_Timeout")
    menu:
        "Ejecutando cuenta regresiva en menú electivo"

        "Responder":
            jump Player_Response

        "Responder, pero en otro botón xD":
            jump Player_Response

label Player_Response:
    "¡Excelente! ¡Has respondido dentro del tiempo asignado!"
    return

label Player_Timeout:
    "El tiempo se ha acabado. Has tardado demasiado en responder."
    return

##############################################################
## MODIFICACIÓN EN SCREENS.RPY
##############################################################

## Dentro de "screens.rpy", busca a "screen choice(items)"
## Debes modificar la screen, en la que quedará de esta forma :

#screen choice(items):
#    style_prefix "choice"
#
#    vbox:
#        for i in items:
#            textbutton i.caption action [Hide("Countdown_Displayer"), i.action]
