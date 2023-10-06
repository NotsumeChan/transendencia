define ch1 = Character('[name]', color="#44d0fa")
image Ich1 = "ch1/neutral.png"
image Notsume = "ch3/neutral.png"


screen mostrarOpt():
    add "bg/tm/room_01.jpeg" xpos  0 ypos 0 xsize 1.0 ysize 1.0
    #add "background.png" xpos 0 ypos 0  #fondo de la pantalla

    imagebutton:
        idle "assets/tm/eleccion_ropa/prenda_01.png"
        hover "assets/tm/eleccion_ropa/prenda_01(hover).png"

        xpos 200 
        ypos 200  
        action Jump("opt1")
        
    imagebutton:
        idle "assets/tm/eleccion_ropa/prenda_02.png"
        hover "assets/tm/eleccion_ropa/prenda_02(hover).png"
        xpos 350
        ypos 550  
        action Jump("opt2")

    imagebutton:
        idle "assets/tm/eleccion_ropa/prenda_03.png"
        hover "assets/tm/eleccion_ropa/prenda_03(hover).png"
        xpos 1550 
        ypos 500
        action Jump("opt3")

label opt1:
    "Has seleccionado la Opción 1."
    jump Agradecimientos

label opt2:
    "Has seleccionado la Opción 2."
    jump Agradecimientos

label opt3:
    "Has seleccionado la Opción 3."
    jump Agradecimientos


label Inicio1:


    play music ["<silence 1>" , background] fadein 5  volume 0.5# Reproduce la música 'bgm.mp3' en bucle.

    scene bg room # Muestra la imagen de fondo 'bg room.png' o 'bg room.jpg'.

    show Notsume at right # Muestra la imagen 'eileen happy.png' o 'eileen happy.jpg' en el lado izquierdo de la pantalla.
    show Ich1 at left
    
    N "hola soy notsume :3"

    ch1 "hola soy [name]"

    N "un gusto [name]"

    hide Notsume
    hide Ich1

    jump .Dia2

label .Dia2:

    "al dia siguiente..."

    "que deberia escoger para hoy?"

    
    call screen mostrarOpt

