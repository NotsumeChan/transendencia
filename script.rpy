define F = Character("Flan", color= "#8f3be3")
define N = Character("Notsume", color="#9b47ad")
define audio.background = "audio/Hopes and Dreams.mp3"
define ch = Character('[name]', color="#44d0fa")

default rrss = False
default post = False
default series = False

image mc = "mc/Prota.png"
image mcM = "mc/Prota_espejo.png"


image us = "us.png"


label start:
    $ personaje = "0"

    show mc at center

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

    hide mc

    jump prologo

label prologo:

    show mcM at center

    "Algunos nacen sabiendo qué quieren y quién deben ser, otros lo descubren en el camino…"
    "¿Alguna vez te has mirado al espejo y has visto a alguien más?" 
    "¿has tenido algo dentro de ti escondido, queriendo salir pero sabes que podría cambiarlo todo?..." 
    "Hay momentos en los que debemos decidir sobre ser fiel a lo que sentimos o ocultarlo un poco más. Debemos ser valientes, los dos caminos son difíciles." 
    "Pero también hay que ser pacientes, hacer las cosas a nuestro tiempo, no importa cuánto nos lleve, no hay respuesta correcta…Crecer es una aventura que debemos recorrer."

    hide mcM

    jump cap1


label cap1:

    show mc at left

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
            $ rrss = True
            
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
            $ post = True


        "Buscar series o películas con personajes transgenero.":
            "El buscador te muestra varios ejemplos de series y películas que podrían servirte, empiezas a revisar cada una por si es que la sinopsis dice algo interesante al respecto." 
            "Luego de un rato te das cuenta que la mayoría no suenan para nada esperanzadoras, tienen esa vista muy triste que hace que te preocupe un poco lo que está por venir en tu vida."
            "De todos modos decides ver algunas" 
            "sientes esperanza al ver personas en situaciones parecidas a las que vives" 
            "pero aun así la variedad de reacciones hace que te preguntes cómo reaccionaría la gente alrededor tuyo" 
            "(Nace en ti un sentimiento de incertidumbre)"
            $ series = True

    jump cap2


label cap2:
    "Han pasado algunos días desde tu investigación" 
    "has estado dándole vueltas a las cosas que aprendiste y crees que es momento de compartir tus ideas con alguien" 
    "A pesar de que la idea te asusta el poder sacarte el peso de guardar este secreto es algo alentador" 
    "Pero" 
    "¿Qué vas a decir?" 
    "o más preocupante aún" 
    "¿cómo van a reaccionar? ¿Deberías decirle a tu familia primero?" 
    "Sabes que tus padres te aman, pero no sabes si están listos para este tipo de conversaciones" 
    "quiza deberias hablar con alguien a quien le tengas mas confianza y cercanía" 
    "como uno de tus amigos" 
    "alguno con el que puedas hablar de lo que sea y sabes que no lo estara contando al resto del grupo" 
    "O quizá sería mejor hablar con alguien externo" 
    "alguien que sepa sobre estos temas" 
    "alguien que haya visto más cosas y pueda entender que no somos todos iguales en este mundo" 
    "Un montón de dudas se forman en tu cabeza."

    ch "Creo que sera mejor dormir"
    "Duermes para seguir pensando en esto mañana"


    "Los días pasan y ves que hay oportunidades para acercarte a hablar sobre el tema" 
    "pero aun no sabes a quién" 
    "ni siquiera si estás listo para esto" 
    "Pero aun así te armas de valor y decides que debes hacerlo. "

    ch "Si no lo hago ahora, quizá no pueda nunca"

    "Contemplas la idea de no hacer nada" 
    "solo guardar como te sientes para ver si se pasa o si encuentras un momento más perfecto para poder actuar sobre este tema"

    ch "Creo que lo mejor es eso, no hacer nada todavía, hasta que esté más seguro."



    "Sigues tu vida como siempre intentando no pensar mucho al respecto" 
    "el sentimiento no se ha pasado pero te sigues repitiendo que va a hacerlo" 
    "eso hace que le quites importancia"
    "Un día tu profesora de ciencias empieza a hablar sobre sexualidad y en ello comienza a mencionar otras orientaciones sexuales para dar paso a una charla sobre la diversidad."
    
    "menciona la diferencia sobre sexo y genero, hablando de como la identidad de genero es algo independiente de la orientacion sexual." 
    "Con esto comienza a dar ejemplos de personas transgenero importantes para la historia del mundo con mucho respeto y admiración." 
    "El darte cuenta que alguien cercano acepta esto te hace sentir un poco más aliviado, te da esperanza de decir algo y que sea bien recibido." 
    "Al terminar la clase ves como tus compañeras y compañeros siguen hablando del tema, escuchas algunos comentarios que te molestan un poco, pero decides no decir nada." 
    "También escuchas algunas preguntas, te gustaría ser parte de la conversación pero aun no te sientes muy seguro al respecto," 
    "aun te da miedo que piensen que eres raro y no puedas defenderte.  Al final dejas que los días pasen"
    "En tu casa buscas información sobre las personas que menciono tu profesora" 
    "te hace feliz saber que gente como tu ha existido desde hace mucho tiempo y que han podido hacer cambios para ayudar a los demás. "
    "En clases ves como tus compañeras y compañeros siguen hablando al respecto" 
    "de a poco vas notando como cada vez hay menos comentarios feos y mas palabras de aceptación, quizá eso sea una señal."
    "Llegas a tu casa y te miras en el espejo."

    ch "No tengo porque sentirme solo, quiero hablar con alguien de esto."

    "Te decidiste a hablarlo, ahora la pregunta es ¿quién? "

    ch "Podría decirle a mi mamá…"

    "La idea no suena mala, pero aun no sabes como reaccionara, quizá debas ver otras opciones."

    ch " hmmm…¿quizá la Bea?"

    "Ha sido tu amiga desde que eran chicos, es tu compañera de puesto en la escuela y con quien más confianza tienes, siempre se cuentan todo, no es una mala idea."

    ch "tal vez alguien que pueda saber del tema…"

    ch "Alguien mayor… el hermano de la Bea quizá sepa algo."

    "El hermano mayor de tu mejor amiga, va a la universidad y sabes que se junta con mucha gente muy diferente" 
    "de seguro él sabe algo" 
    "o conoce a alguien que pueda ayudarte." 
    "Debes decidir bien si quieres ayuda."

    menu:
        "¿Con quién vas a hablar?"

        
        "Hablar con tu mamá." if rrss or post:
            "hablas con tu mamá te dice que no entiende pero te apoya, te advierte que quizá se vaya con la edad"

        
        "Hablar con tu mejor amiga." if rrss or series:
            "en un principio piensa que estás bromeando"
            "le preocupa que las cosas entre ustedes cambien, pero te apoya de manera incondicional" 
            "te pregunta si quieres decirle a su hermano para que te ayude a conseguir cosas que puedan ayudarte"

        
        "Hablar con el hermano de tu mejor amiga." if post or series:
            "Te habla de las personas que conoce que son trans"
            "te sientes aceptado y te ayuda a encontrar cosas que puedan ayudarte a sentirte mejor"
            "te incentiva a hablar con su hermana para que no la dejes fuera de las cosas"
            if personaje == "1":
                jump ropatm
            if personaje == "2":
                jump ropatn
            if personaje == "3":
                jump ropatf


label ropatf:
    jump cap3

label ropatn:
    jump cap3

label ropatm:
    jump cap3



label cap3:
    pass


label Agradecimientos:
    show us 


    "Gracias por jugar"
    "Este juego fue creado por:\n
        -Perr0Waton\n
        -Notsume"