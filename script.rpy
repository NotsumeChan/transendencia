label start:
    show mc at center

    menu:
        "con que personaje quieres comenzar la historia?"


        "Trans-Masculino":
            $ personaje = "1"

        "No-Binario":
            $ personaje = "2"

        "Trans-Femenina":
            $ personaje = "3"
            

    python:
        name = ""
        name = renpy.input("¿Cual es tu nombre?", length=15, multiline = False)
        name = name.strip()

        if not name:
            name = "Anonimo"

    hide mc

    jump prologo

label prologo:

    show mcM at center

    "Algunos nacen sabiendo que quieren y quien deben ser, otros lo descubren en el camino…"
    "¿Alguna vez te has mirado al espejo y has visto a alguien mas?" 
    "¿has tenido algo dentro de ti escondido, queriendo salir pero sabes que podria cambiarlo todo?..." 
    "Hay momentos en los que debemos decidir sobre ser fiel a lo que sentimos o ocultarlo un poco mas. Debemos ser valientes, los dos caminos son dificiles." 
    "Pero tambien hay que ser pacientes, hacer las cosas a nuestro tiempo, no importa cuanto nos lleve, no hay respuesta correcta…Crecer es una aventura que debemos recorrer."

    hide mcM

    jump cap1


label cap1:

    show pieza:
        zoom 0.65
    show mc at center

    "Llegaste de la escuela, es un dia normal." 
    "Hora de ponerse algo mas comodo y aprovechar el tiempo libre." 
    "Hay algo que te ha estado molestando ultimamente… Te miras al espejo y sientes esa sensacion extraña de nuevo."

    hide pieza
    hide mc
    show mcM
    ch "¿que es esto? ¿porque lo siento de nuevo?"

    hide mcM
    "Decides al fin hacer algo, vas a tu computadora y decides usar la herramienta mas grande, la internet."

    show pc:
        zoom 1.0

    ch "de seguro aqui debe haber algo…"

    "Desde que descubriste que el genero que te asignaron cuando naciste no concordaba con como te sentias por dentro la “molestia” se ha hecho mas presente." 
    "Investigaste un poco por tu cuenta y descubriste el termino “transgenero”." 
    "Eso y un poco mas de leer te ayudo a entender un poco, pero sigues preguntandote porque esa “molestia” no se va, no sabes si es algo solo tuyo o si alguien mas lo tiene" 
    "puede que tenga un nombre quiza" 
    "alguien debe saber como ayudarte." 
    "Pero hablar con otros no es opcion, no aun, quieres primero saber como ponerlo en palabras" 
    "si no puedes explicarlo es dificil que puedas recibir ayuda" 
    "Quizas buscar a otras personas trans pueda ayudarte en algo, ver que dicen y si tienen algo parecido contigo."

    menu:
        "¿Que vas a hacer?"

        "Buscar en redes sociales a personas transgenero.":
            "buscas algun perfil con las palabras claves que se te vienen a la mente y logras encontrar varios grupos de personas que cuentan sus experiencias siendo trans"
            "lamentablemente la mayoria de estos estan en ingles. De todos modos, decides mirar un poco lo que dicen para ver si hay algo que te haga sentido."
            "Mientras exploras un poco con ayuda del traductor, te encuentras con relatos conmovedores de personas que han superado desafios similares a los tuyos" 
            "Algunos comparten consejos sobre como lidiar con algo llamado “disforia”" 
            "como abordar estos sentimientos" 
            "parece que eso es lo que estas buscando" 
            "A pesar de tener problemas con el idioma, te sientes extrañamente parte de esta comunidad virtual, eso te alegra" 
            "Decides seguir algunos perfiles y guardar algunas publicaciones que llamaron mas tu atencion."
            $ rrss = True
            
        "Buscar post de organizaciones al respecto.":
            "Escribes la palabra “Transgenero” en el buscador, logras encontrar entre los resultados algunas organizaciones que pertenecen a Chile"
            "echas un vistazo y encuentras un monton de informacion sobre las campañas que llevan a cabo." 
            "Intentas mirar todas las secciones para encontrar algo que te sirva y te topas con un monton de investigaciones y escritos profesionales sobre distintos temas." 
            "Se ven complicados pero aun asi revisas unos cuantos."
            "Mientras revisas las paginas, descubres que hay grupos de apoyo presenciales y en linea donde las personas comparten sus experiencias. Algunas de estas campañas se ven utiles para tu situacion, ademas tambien notas algunas dirigidas a la familia" 
            "¿Podrias invitar a tus papas a una reunion?" 
            "quiza cuando te armes de valor para decirles podrias intentarlo." 
            "Aparte de eso solo te topas con escritos profesionales que hablan sobre la identidad de genero escritos por personas desde lo educacional y la psicologia" 
            "Al leer algunos te das cuenta de que obviamente no se centran en cosas mas personales, sino en cosas como estudios y politicas" 
            "Esto hace que te sientas confundido por los tecnicismos, pero de todos modos logras captar unas cuantas ideas" 
            "Por otro lado" 
            "te hace sentir seguridad el saber que hay instituciones de  verdad a las que pedir ayuda."
            $ post = True


        "Buscar series o peliculas con personajes transgenero.":
            "El buscador te muestra varios ejemplos de series y peliculas que podrian servirte, empiezas a revisar cada una por si es que la sinopsis dice algo interesante al respecto." 
            "Luego de un rato te das cuenta que la mayoria no suenan para nada esperanzadoras, tienen esa vista muy triste que hace que te preocupe un poco lo que esta por venir en tu vida."
            "De todos modos decides ver algunas" 
            "sientes esperanza al ver personas en situaciones parecidas a las que vives" 
            "pero aun asi la variedad de reacciones hace que te preguntes como reaccionaria la gente alrededor tuyo" 
            "(Nace en ti un sentimiento de incertidumbre)"
            $ series = True

    hide pc
    jump cap2


label cap2:

    show pieza:
        zoom 0.65
    "Han pasado algunos dias desde tu investigacion" 
    "has estado dandole vueltas a las cosas que aprendiste y crees que es momento de compartir tus ideas con alguien" 
    "A pesar de que la idea te asusta el poder sacarte el peso de guardar este secreto es algo alentador" 
    "Pero" 
    "¿Que vas a decir?" 
    "o mas preocupante aun" 
    "¿como van a reaccionar? ¿Deberias decirle a tu familia primero?" 
    "Sabes que tus padres te aman, pero no sabes si estan listos para este tipo de conversaciones" 
    "quiza deberias hablar con alguien a quien le tengas mas confianza y cercania" 
    "como uno de tus amigos" 
    "alguno con el que puedas hablar de lo que sea y sabes que no lo estara contando al resto del grupo" 
    "O quiza seria mejor hablar con alguien externo" 
    "alguien que sepa sobre estos temas" 
    "alguien que haya visto mas cosas y pueda entender que no somos todos iguales en este mundo" 
    "Un monton de dudas se forman en tu cabeza."

    ch "Creo que sera mejor dormir"

    hide pieza

    "Duermes para seguir pensando en esto mañana"


    "Los dias pasan y ves que hay oportunidades para acercarte a hablar sobre el tema" 
    "pero aun no sabes a quien" 
    "ni siquiera si estas listo para esto" 
    "Pero aun asi te armas de valor y decides que debes hacerlo. "

    show mcM at center
    ch "Si no lo hago ahora, quiza no pueda nunca"

    "Contemplas la idea de no hacer nada" 
    "solo guardar como te sientes para ver si se pasa o si encuentras un momento mas perfecto para poder actuar sobre este tema"

    ch "Creo que lo mejor es eso, no hacer nada todavia, hasta que este mas seguro."

    hide mcM

    show colegio:
        zoom 0.3
    "Sigues tu vida como siempre intentando no pensar mucho al respecto" 
    "el sentimiento no se ha pasado pero te sigues repitiendo que va a hacerlo" 
    "eso hace que le quites importancia"
    "Un dia tu profesora de ciencias empieza a hablar sobre sexualidad y en ello comienza a mencionar otras orientaciones sexuales para dar paso a una charla sobre la diversidad."
    
    "menciona la diferencia sobre sexo y genero, hablando de como la identidad de genero es algo independiente de la orientacion sexual." 
    "Con esto comienza a dar ejemplos de personas transgenero importantes para la historia del mundo con mucho respeto y admiracion." 
    "El darte cuenta que alguien cercano acepta esto te hace sentir un poco mas aliviado, te da esperanza de decir algo y que sea bien recibido." 
    "Al terminar la clase ves como tus compañeras y compañeros siguen hablando del tema, escuchas algunos comentarios que te molestan un poco, pero decides no decir nada." 
    "Tambien escuchas algunas preguntas, te gustaria ser parte de la conversacion pero aun no te sientes muy seguro al respecto," 
    "aun te da miedo que piensen que eres raro y no puedas defenderte." 
    hide colegio

    show plaza:
        zoom 0.3
    "Al final dejas que los dias pasen"
    hide Plaza

    show pc
    "En tu casa buscas informacion sobre las personas que menciono tu profesora" 
    "te hace feliz saber que gente como tu ha existido desde hace mucho tiempo y que han podido hacer cambios para ayudar a los demas. "
    hide pc

    show colegio:
        zoom 0.3
    "En clases ves como tus compañeras y compañeros siguen hablando al respecto" 
    "de a poco vas notando como cada vez hay menos comentarios feos y mas palabras de aceptacion, quiza eso sea una señal."
    hide colegio

    show mcM
    "Llegas a tu casa y te miras en el espejo."

    ch "No tengo porque sentirme solo, quiero hablar con alguien de esto."

    "Te decidiste a hablarlo, ahora la pregunta es ¿quien? "

    ch "Podria decirle a mi mama…"

    "La idea no suena mala, pero aun no sabes como reaccionara, quiza debas ver otras opciones."

    ch " hmmm…¿quiza la Bea?"

    "Ha sido tu amiga desde que eran chicos, es tu compañera de puesto en la escuela y con quien mas confianza tienes, siempre se cuentan todo, no es una mala idea."

    ch "tal vez alguien que pueda saber del tema…"

    ch "Alguien mayor… el hermano de la Bea quiza sepa algo."

    "El hermano mayor de tu mejor amiga, va a la universidad y sabes que se junta con mucha gente muy diferente" 
    "de seguro el sabe algo" 
    "o conoce a alguien que pueda ayudarte." 
    "Debes decidir bien si quieres ayuda."
    hide mcM

    menu:
        "¿Con quien vas a hablar?"

        
        "Hablar con tu mama." if rrss or post:
            show MamaNeutra
            "le cuentas que has estado investigando sobre el tema y que te sientes identificado con lo que has leido"
            hide MamaNeutra
            show MamaPreocupada
            "tu mama te dice que no entiende pero te apoya, te advierte que quiza se vaya con la edad"
            hide MamaPreocupada
            jump cap3

        "Hablar con tu mejor amiga." if rrss or series:
            show AmigaFeliz
            "en un principio piensa que estas bromeando"
            hide AmigaFeliz
            show AmigaPreocupada
            "le preocupa que las cosas entre ustedes cambien, pero te apoya de manera incondicional" 
            "te pregunta si quieres decirle a su hermano para que te ayude a conseguir cosas que puedan ayudarte"
            hide AmigaPreocupada
            jump cap3
        
        "Hablar con el hermano de tu mejor amiga." if post or series:
            show HermanoNeutro
            "Te habla de las personas que conoce que son trans"
            hide HermanoNeutro
            show HermanoFeliz
            "te sientes aceptado y te ayuda a encontrar cosas que puedan ayudarte a sentirte mejor"
            "te incentiva a hablar con su hermana para que no la dejes fuera de las cosas"
            hide HermanoFeliz

            "Te trae ropa para que te pruebes"

            if personaje == "1":
                jump ropatm
            if personaje == "2":
                jump ropatn
            if personaje == "3":
                jump ropatf

#AGREGAR ROPA PARA EL MC

label ropatf:
    
    "te sientes feliz de que alguien te apoye y te ayude a sentirte mejor contigo mismo"
    
    "misma*"
    "tendras que acostumbrarte a eso"
    "te pruebas la ropa y te ves al espejo, te sientes bien"

    "Te sientes feliz de haber hablado con alguien, pero aun no sabes si estas listo para decirle a tu familia"
    
    jump cap3

label ropatn:

    "Te sientes feliz de haber hablado con alguien, pero aun no sabes si estas listo para decirle a tu familia"

    jump cap3

label ropatm:



    "Te sientes feliz de haber hablado con alguien, pero aun no sabes si estas listo para decirle a tu familia"

    jump cap3


label cap3:
    pass


label Agradecimientos:
    show us:
        xpos 700
        zoom 3.0    


    "Gracias por jugar"
    "Este juego fue creado por:\n
        Forg"