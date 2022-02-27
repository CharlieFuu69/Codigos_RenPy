## CharlieFuu69
## MouseFinderTool

## Utilidad para rastrear la posición del mouse en la interfaz de un juego Ren'Py.

#############################################################

init python:
    import time
    import threading

    class MouseFinderTool:
        """Esta clase se encarga de obtener la posición del mouse y organizarla para
        posteriormente mostrarla en un recuadro."""

        def __init__(self, interval = 0.1):
            """Constructor."""

            self.pixel_pos = [0, 0]
            self.float_pos = [0.0, 0.0]
            self.update_rate = interval
            self.save = 0

        def get_pos(self):
            """Devuelve una lista con dos listas: la que contiene coordenadas en píxeles y
            la que contiene coordenadas relativas."""

            return [self.pixel_pos, self.float_pos]

        def save_in_textfile(self):
            self.save += 1
            save_string = "> Coordenada %s\n- En píxeles: %s\n- Relativo: %s\n\n"  % (self.save, self.get_pos()[0], self.get_pos()[1])

            try:
                with open(config.basedir + "/mouse_log.txt", "a") as mftfile:
                    mftfile.write(save_string)
                    mftfile.close()
                renpy.notify("Registro guardado en el archivo \"mouse_log.txt\", en la carpeta base de tu proyecto.")

            except:
                renpy.notify("Ocurrió un error mientras se escribía en el archivo TXT.")

        def coordinate_dispatcher(self):
            """Obtiene las coordenadas del mouse y calcula las coordenadas relativas
            (es decir, flotante entre 0.0 y 1.0) según sea necesario."""

            while True:
                current = renpy.get_mouse_pos()

                self.pixel_pos = [current[0], current[1]]
                self.float_pos = [
                round(1.0 * current[0] / config.screen_width, 2),
                round(1.0 * current[1] / config.screen_height, 2)]

                time.sleep(self.update_rate)
                renpy.restart_interaction()

        def run(self):
            """Ejecuta el detector en un hilo aparte del juego."""

            t1 = threading.Thread(target =  self.coordinate_dispatcher)
            t1.daemon = True
            t1.start()

screen ShowDetails():
    zorder 300
    style_prefix "cft"

    default getcf = MouseFinderTool()
    default getcf_show = True

    on "show" action Function(getcf.run)

    if getcf_show:
        drag:
            drag_name "ShowDetails"
            pos(0.0, 0.2)
            drag_handle (0.0, 0.2, 370, 280)

            frame:
                xysize(370, 280)

                vbox:
                    xalign 0.5 ypos 15
                    text "CharlieFuu69 - MouseFinderTool" xalign 0.5 color "#ff0"
                    text "[[Esta ventana es arrastrable]" xalign 0.5 italic True

                vbox:
                    pos(15, 100)
                    spacing 10

                    vbox:
                        text "Coordenadas en píxeles" color "#ff0"
                        text "X: %spx / Y: %spx" % (getcf.get_pos()[0][0], getcf.get_pos()[0][1])

                    vbox:
                        text "Coordenadas relativas" color "#ff0"
                        text "X: %s / Y: %s" % (getcf.get_pos()[1][0], getcf.get_pos()[1][1])

                textbutton "{size=18}Ocultar ventana{/size}" action [SetScreenVariable("getcf_show", False),
                Function(renpy.notify, "Presiona la tecla \"C\" para mostrar la ventana nuevamente")] align(0.5, 0.95)

    key "c" action SetScreenVariable("getcf_show", True)
    key "r" action Function(getcf.save_in_textfile)
    
style cft_text:
    size 18

init python:
    ## Esto asegura que se muestre el cuadro de detalles en tu juego.
    if config.developer or config.debug:
        config.overlay_screens.append("ShowDetails")
