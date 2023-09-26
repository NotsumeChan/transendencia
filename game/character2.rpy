define ch2 = Character('[name]', color="#ffffff")
image Ich2 = "2.png"
image Flan = "1.png"

label Inicio2:

    play music ["<silence 1>" , background] fadein 5  volume 0.5# Reproduce la música 'bgm.mp3' en bucle.

    scene bg room # Muestra la imagen de fondo 'bg room.png' o 'bg room.jpg'.
    
    show Flan  at right # Muestra la imagen 'eileen happy.png' o 'eileen happy.jpg' en el lado izquierdo de la pantalla.
    show Ich2 at left
    
    F "hola soy flan y soy un personaje de prueba"

    ch2 "hola soy [name] xd"

    F "un gusto [name]"
    return
