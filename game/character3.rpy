define ch3 = Character("[name]", color="#fb8dff")
image Ich3 = "3.png"
image Flan = "1.png"

label Inicio3:

    play music ["<silence 1>" , background] fadein 5  volume 0.5# Reproduce la música 'bgm.mp3' en bucle.

    scene bg room # Muestra la imagen de fondo 'bg room.png' o 'bg room.jpg'.

    show Flan  at right 
    show Ich3 at left
    
    # Presenta las líneas del diálogo.
    F "hola soy flan y soy un personaje de prueba"

    ch3 "hola soy [name] xd"

    F "un gusto [name]"

    return