define ch1 = Character('[name]', color="#44d0fa")
image Ich1 = "1.png"
image Notsume = "3.png"

label Inicio1:

    play music ["<silence 1>" , background] fadein 5  volume 0.5# Reproduce la música 'bgm.mp3' en bucle.

    scene bg room # Muestra la imagen de fondo 'bg room.png' o 'bg room.jpg'.

    show Notsume at right # Muestra la imagen 'eileen happy.png' o 'eileen happy.jpg' en el lado izquierdo de la pantalla.
    show Ich1 at left
    
    N "hola soy notsume :3"

    ch1 "hola soy [name]"

    N "un gusto [name]"

    return

