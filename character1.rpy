define ch1 = Character('[name]', color="#44d0fa")
image Ich1 = "1.png"
image Notsume = "3.png"


screen mostrarOpt():
    add "black.png"
    #add "background.png" xpos 0 ypos 0  #fondo de la pantalla

    textbutton "Option_1" action Jump("opt1"):
        xpos 100 ypos 100  # Define la posición de la opción 1 en la pantalla

    textbutton "Option_2" action Jump("opt2"):
        xpos 600 ypos 300  # Define la posición de la opción 2 en la pantalla

    textbutton "Option_3" action Jump("opt3"):
        xpos 300 ypos 500  # Define la posición de la opción 3 en la pantalla

label opt1:
    "Has seleccionado la Opción 1."
    return

label opt2:
    "Has seleccionado la Opción 2."
    return

label opt3:
    "Has seleccionado la Opción 3."
    return


label Inicio1:


    play music ["<silence 1>" , background] fadein 5  volume 0.5# Reproduce la música 'bgm.mp3' en bucle.

    scene bg room # Muestra la imagen de fondo 'bg room.png' o 'bg room.jpg'.

    show Notsume at right # Muestra la imagen 'eileen happy.png' o 'eileen happy.jpg' en el lado izquierdo de la pantalla.
    show Ich1 at left
    
    N "hola soy notsume :3"

    ch1 "hola soy [name]"

    N "un gusto [name]"

    

    jump .Dia2

label .Dia2:

    "al dia siguiente..."

    "que deberia escoger para hoy?"
    call screen mostrarOpt

