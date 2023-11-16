define F = Character("Flan", color= "#8f3be3")
define N = Character("Notsume", color="#9b47ad")
define audio.background = "audio/Hopes and Dreams.mp3"
define ch = Character('[name]', color="#44d0fa")

image a = "ch1/neutral.png"
image b = "ch2/neutral.png"
image c = "ch3/neutral.png"

image us = "us.png"


label start:
    $ personaje = "0"

    show a at left
    show b at center
    show c at right

    menu:
        "con que personaje quieres comenzar la historia?"


        "(izquierda) Trans-Masculino":
            $ personaje = "1"

        "(centro) No-Binario":
            $ personaje = "2"

        "(derecha) Trans-Femenina":
            $ personaje = "3"
            

    python:
        name = ""
        name = renpy.input("¿Cuál es tu nombre?", length=15, multiline = False)
        name = name.strip()

        if not name:
            name = "Anónimo"

    hide a
    hide b
    hide c

    jump prologo

if personaje == "1":
    jump Inicio1
if personaje == "2":
    jump Inicio2
if personaje == "3":   
    jump Inicio3


label prologo:

    "Algunos nacen sabiendo qué quieren y quién deben ser, otros lo descubren en el camino…"
    "¿Alguna vez te has mirado al espejo y has visto a alguien más?" 
    "¿has tenido algo dentro de ti escondido, queriendo salir pero sabes que podría cambiarlo todo?..." 
    "Hay momentos en los que debemos decidir sobre ser fiel a lo que sentimos o ocultarlo un poco más. Debemos ser valientes, los dos caminos son difíciles." 
    "Pero también hay que ser pacientes, hacer las cosas a nuestro tiempo, no importa cuánto nos lleve, no hay respuesta correcta…Crecer es una aventura que debemos recorrer."

    jump cap1


label cap1:
    "Llegaste de la escuela, es un día normal." 
    "Hora de ponerse algo más cómodo y aprovechar el tiempo libre." 
    "Hay algo que te ha estado molestando últimamente… Te miras al espejo y sientes esa sensación extraña de nuevo."

    ch "¿qué es esto? ¿porque lo siento de nuevo?"

    "Decides al fin hacer algo, vas a tu computadora y decides usar la herramienta mas grande, la internet."

    ch "de seguro aquí debe haber algo…"

    "Desde que descubriste que el género que te asignaron cuando naciste no concordaba con cómo te sentías por dentro la “molestia” se ha hecho más presente." 
    "Investigaste un poco por tu cuenta y descubriste el termino “transgénero”." 
    "Eso y un poco más de leer te ayudó a entender un poco, pero sigues preguntándote porque esa “molestia” no se va, no sabes si es algo solo tuyo o si alguien más lo tiene" 
    "puede que tenga un nombre quizá" 
    "alguien debe saber como ayudarte." 
    "Pero hablar con otros no es opción, no aún, quieres primero saber como ponerlo en palabras" 
    "si no puedes explicarlo es difícil que puedas recibir ayuda" 
    "Quizás buscar a otras personas trans pueda ayudarte en algo, ver que dicen y si tienen algo parecido contigo."

    menu:
        "¿Que vas a hacer?"

        "Buscar en redes sociales a personas transgenero.":
            "buscas algún perfil con las palabras claves que se te vienen a la mente y logras encontrar varios grupos de personas que cuentan sus experiencias siendo trans"
            "lamentablemente la mayoría de estos están en inglés. De todos modos, decides mirar un poco lo que dicen para ver si hay algo que te haga sentido."
            "Mientras exploras un poco con ayuda del traductor, te encuentras con relatos conmovedores de personas que han superado desafíos similares a los tuyos" 
            "Algunos comparten consejos sobre cómo lidiar con algo llamado “disforia”" 
            "cómo abordar estos sentimientos" 
            "parece que eso es lo que estás buscando" 
            "A pesar de tener problemas con el idioma, te sientes extrañamente parte de esta comunidad virtual, eso te alegra" 
            "Decides seguir algunos perfiles y guardar algunas publicaciones que llamaron más tu atención."
            
        "Buscar post de organizaciones al respecto.":
            "Escribes la palabra “Transgenero” en el buscador, logras encontrar entre los resultados algunas organizaciones que pertenecen a Chile"
            "echas un vistazo y encuentras un montón de información sobre las campañas que llevan a cabo." 
            "Intentas mirar todas las secciones para encontrar algo que te sirva y te topas con un montón de investigaciones y escritos profesionales sobre distintos temas." 
            "Se ven complicados pero aún así revisas unos cuantos."
            "Mientras revisas las páginas, descubres que hay grupos de apoyo presenciales y en línea donde las personas comparten sus experiencias. Algunas de estas campañas se ven útiles para tu situación, además también notas algunas dirigidas a la familia" 
            "¿Podrías invitar a tus papás a una reunión?" 
            "quizá cuando te armes de valor para decirles podrías intentarlo." 
            "Aparte de eso solo te topas con escritos profesionales que hablan sobre la identidad de género escritos por personas desde lo educacional y la psicología" 
            "Al leer algunos te das cuenta de que obviamente no se centran en cosas más personales, sino en cosas como estudios y políticas" 
            "Esto hace que te sientas confundido por los tecnicismos, pero de todos modos logras captar unas cuantas ideas" 
            "Por otro lado" 
            "te hace sentir seguridad el saber que hay instituciones de  verdad a las que pedir ayuda."


        "Buscar series o películas con personajes transgenero.":
            "El buscador te muestra varios ejemplos de series y películas que podrían servirte, empiezas a revisar cada una por si es que la sinopsis dice algo interesante al respecto." 
            "Luego de un rato te das cuenta que la mayoría no suenan para nada esperanzadoras, tienen esa vista muy triste que hace que te preocupe un poco lo que está por venir en tu vida."
            "De todos modos decides ver algunas" 
            "sientes esperanza al ver personas en situaciones parecidas a las que vives" 
            "pero aun así la variedad de reacciones hace que te preguntes cómo reaccionaría la gente alrededor tuyo" 
            "(Nace en ti un sentimiento de incertidumbre)"


label Agradecimientos:
    show us 


    "Gracias por jugar"
    "Este juego fue creado por:\n
        -Perr0Waton\n
        -Notsume"