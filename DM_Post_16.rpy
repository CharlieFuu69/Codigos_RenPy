## ElectroBasicsYT - CharlieFuu69 Creations!
## Script Utility : Countdown para menús de elección en Ren'Py
## (Barra animada)

##############################################################

## NOTAS DE ESTE ARCHIVO :

## Este archivo corresponde al Post #16 del hilo "Programando Juegos VN con Ren'Py!"

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

screen Countdown_Displayer(time_left, label_dest):
    ## Parámetros
    ## time_left : Tiempo del countdown en segundos (Valor Flotante)
    ## label_dest : El label a donde se transferirá el control del juego (String)

    vbox:
        xalign 0.5
        yalign 0.8
        xsize 740

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
