define F = Character("Flan", color= "#8f3be3")
define N = Character("Notsume", color="#9b47ad")
define audio.background = "audio/Hopes and Dreams.mp3"

image a = "ch1/neutral.png"
image b = "ch2/neutral.png"
image c = "ch3/neutral.png"


label start:
    $ personaje = "0"

    show a at left
    show b at center
    show c at right

    menu:
        "con que personaje quieres comenzar la historia?"


        "(izquierda) Fran : Trans-Masculino":
            $ personaje = "1"

        "(centro) Extra : No-Binario":
            $ personaje = "2"

        "(derecha) Notsume : Trans-Femenina":
            $ personaje = "3"
            

    python:
        name = ""
        name = renpy.input("¿Cuál es tu nombre?", length=15, multiline = False)
        name = name.strip()

        if not name:
            name = "Anónimo"


    if personaje == "1":
        jump Inicio1
    if personaje == "2":
        jump Inicio2
    if personaje == "3":   
        jump Inicio3


label ShowMenu:
    return

