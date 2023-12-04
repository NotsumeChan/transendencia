label start:
    show mc at center

    menu:
        # stop "audio/FORG.wav"
        "con que personaje quieres comenzar la historia?"


        "Trans-Masculino":
            $ personaje = "1"
            $ genero = "niÑa"

        "No-Binario":
            $ personaje = "2"
                

        "Trans-Femenina":
            $ personaje = "3"
            $ genero = "niÑo"
            

    python:
        from random import randint
        genero = "niÑo" if randint(0,1) else "niÑa"
        pronombre = genero[-1]
        name = ""
        name = renpy.input("¿Cual es tu nombre?", length=15, multiline = False)
        name = name.replace("ñ", "Ñ")
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
        zoom 1
    show mc at center

    "Llegaste de la escuela, es un dia normal." 
    "Hora de ponerse algo mas comod[pronombre] y aprovechar el tiempo libre." 
    "Hay algo que te ha estado molestando ultimamente… Te miras al espejo y sientes esa sensacion extraÑa de nuevo."

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
            "A pesar de tener problemas con el idioma, te sientes extraÑamente parte de esta comunidad virtual, eso te alegra" 
            "Decides seguir algunos perfiles y guardar algunas publicaciones que llamaron mas tu atencion."
            $ rrss = True
            
        "Buscar post de organizaciones al respecto.":
            "Escribes la palabra “Transgenero” en el buscador, logras encontrar entre los resultados algunas organizaciones que pertenecen a Chile"
            "echas un vistazo y encuentras un monton de informacion sobre las campaÑas que llevan a cabo." 
            "Intentas mirar todas las secciones para encontrar algo que te sirva y te topas con un monton de investigaciones y escritos profesionales sobre distintos temas." 
            "Se ven complicados pero aun asi revisas unos cuantos."
            "Mientras revisas las paginas, descubres que hay grupos de apoyo presenciales y en linea donde las personas comparten sus experiencias." 
            "Algunas de estas campaÑas se ven utiles para tu situacion, ademas tambien notas algunas dirigidas a la familia" 
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
        zoom 1
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

    "Duermes para seguir pensando en esto maÑana"


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
        zoom 1
    "Sigues tu vida como siempre intentando no pensar mucho al respecto" 
    "el sentimiento no se ha pasado pero te sigues repitiendo que va a hacerlo" 
    "eso hace que le quites importancia"
    "Un dia tu profesora de ciencias empieza a hablar sobre sexualidad y en ello comienza a mencionar otras orientaciones sexuales para dar paso a una charla sobre la diversidad."
    
    "menciona la diferencia sobre sexo y genero, hablando de como la identidad de genero es algo independiente de la orientacion sexual." 
    "Con esto comienza a dar ejemplos de personas transgenero importantes para la historia del mundo con mucho respeto y admiracion." 
    "El darte cuenta que alguien cercano acepta esto te hace sentir un poco mas aliviad[pronombre], te da esperanza de decir algo y que sea bien recibido." 
    "Al terminar la clase ves como tus compaÑeras y compaÑeros siguen hablando del tema, escuchas algunos comentarios que te molestan un poco, pero decides no decir nada." 
    "Tambien escuchas algunas preguntas, te gustaria ser parte de la conversacion pero aun no te sientes muy seguro al respecto," 
    "aun te da miedo que piensen que eres rar[pronombre] y no puedas defenderte." 
    hide colegio

    "Al final dejas que los dias pasen"

    show pc
    "En tu casa buscas informacion sobre las personas que menciono tu profesora" 
    "te hace feliz saber que gente como tu ha existido desde hace mucho tiempo y que han podido hacer cambios para ayudar a los demas. "
    hide pc

    show colegio:
        zoom 1
    "En clases ves como tus compaÑeras y compaÑeros siguen hablando al respecto" 
    "de a poco vas notando como cada vez hay menos comentarios feos y mas palabras de aceptacion, quiza eso sea una seÑal."
    hide colegio

    show mcM
    "Llegas a tu casa y te miras en el espejo."

    ch "No tengo porque sentirme sol[pronombre], quiero hablar con alguien de esto."

    "Te decidiste a hablarlo, ahora la pregunta es ¿quien? "

    ch "Podria decirle a mi mama…"

    "La idea no suena mala, pero aun no sabes como reaccionara, quiza debas ver otras opciones."

    ch " hmmm…¿quiza la Bea?"

    "Ha sido tu amiga desde que eran chic[pronombre]s, es tu compaÑera de puesto en la escuela y con quien mas confianza tienes, siempre se cuentan todo, no es una mala idea."

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
            "Decides hablar con tu mama" 
            "asi que te acercas a ella cuando llegas de clases" 
            "la guias a tu pieza para poder hablar con ella mas tranquilamente."

            show pieza
            show Mama Neutra at right
            show mc Hablando at left

            ch "Mama, ¿podemos hablar?"

            mama "Claro, cariÑo! ¿Que sucede?"

            ch "Es solo que... ultimamente me siento incomod[pronombre], como si algo estuviera mal."

            mama @ Preocupada "¿Mal? ¿Como asi mi amor?"

            ch "No se como decirlo exactamente, pero... a veces no me siento yo mism[pronombre]."
            ch "Como si mi cuerpo no concordara con lo que siento por dentro."
            ch "Como si no fuera totalmente un [genero]"

            mama @ Preocupada "No se si te entiendo mi amor ¿Esto es de ahora o de hace tiempo?"

            ch "Creo que es algo con mi género mamá, no sé bien como explicártelo… eso si, viene desde hace tiempo."

            mama "Quiero que sepas que te apoyo, aunque no entiendo mucho, quiza es algo de la edad y se va a pasar con el tiempo."

            ch "¿De verdad? Me da miedo que no lo entiendas."

            mama @ Feliz "No te preocupes, amor. Estoy aquí para ti y tu mama siempre te va a apoyar."

            ch "¿Crees que es muy raro?"

            mama  "La verdad, no se, no entiendo bien como se siente eso." 
            mama @ Feliz "Pero aqui estamos y te voy a querer siempre."
            mama  "Aparte como te dije, quiza es algo que se te pase despues, no hay que preocuparnos mucho."
            
            ch "Gracias, mama. Me siento mejor sabiendo que te tengo a mi lado."

            mama "Siempre, cariÑo."
            
            "No estas sol[pronombre] en esto."

            hide pieza
            hide Mama
            hide mc

            jump cap3

        "Hablar con tu mejor amiga." if rrss or series:
            "Decides que lo mejor será hablarlo con tu mejor amiga, al menos para poder sacarlo de tu pecho un poco." 
            "Vas a clases y esperas a que sea el momento perfecto para hablar sobre el tema, pero sabes que si sigues esperando no vas a lograr nada"
            "asi que te armas de valor para hablarlo en este recreo, aqui mismo en la sala."
           
            show colegio
            show Amiga Neutra at right
            show mc Hablando at left

            ch "Oye hay algo que quiero hablar contigo."

            Amiga @ Feliz "¿Que paso? ¿Me vas a decir que te gusta alguien?"

            ch "No, esto es serio, de verdad quiero hablar contigo."

            Amiga @ Preocupada "uhhhh…. ¿Estas bien? ¿Te paso algo en la casa?"

            ch "No, no es eso… ¿Te acuerdas lo que hemos visto en  ciencias? "

            Amiga @ Preocupada "Si… ¿Pasa algo con eso?"

            ch "Ya….. ¿Que pasaria si yo no fuera un niño? "

            Amiga "¿Como? uhmmm osea, no se, no seria muy diferente que ahora ¿no?"

            Amiga @ Preocupada "¿Porque estamos hablando de eso?" 

            ch "Es que… a ver ¿Como te digo? "

            ch "Hace ya harto tiempo me siento raro… como si hubiera algo mal en mi, algo con mi cuerpo."

            Amiga "¿Ya? ¿Es como lo que dijo la profe? ¿El tema del genero?"

            ch "Si… eso mismo. "

            ch "Bea creo que soy transgenero… he estado viendo cosas sobre eso y pienso que si lo soy…" 
            ch "ahora ultimo me siento incomod[pronombre] con como me veo… no me quiero ver asi."

            Amiga "Uhm………. "

            Amiga @ Triste "Entonces … ¿Eso cambia algo con nosotros?"

            "Notas que tu amiga esta preocupada, mas bien triste, asi que la abrazas para que se sienta mejor."

            ch "Obvio que no tonta. Tu sigues siendo mi mejor amiga."
            python:
                if genero == "niÑo":
                    a = "a"
                else:
                    a = "o"
            Amiga @ Triste "Tu tambien eres mi mejor amig[pronombre]… amig[a]. Perdon."

            "Ambos hablan un rato sobre como te has sentido ultimamente, te alegra bastante el poder hablar al respecto finalmente, y saber que tu mejor amiga sigue ahi lo hace mucho mejor."
            "Llega la hora de la salida y acompañas a tu amiga a la plaza a esperar a su hermano. Mientras esperan ves como a Bea se le ocurre una idea."

            hide colegio
            hide Amiga
            hide mc

            show plaza
            show Amiga Neutra at right
            show Hermano Neutro at center
            show mc Hablando at left

            Amiga @ Feliz "Oye ¿Y si le decimos a mi hermano?"

            ch "¿Decirle que cosa?"

            Amiga "Ahh Tu sabes poh. Lo de tu genero. "

            ch "Uhm no se… ¿Serviria de algo?"

            Amiga @ Feliz "Obvio el Mati tiene un monton de amigos en la U, demas conoce a alguien que sepa mas de esto y pueda ayudarte."

            "Lo piensas un poco. Finalmente crees que si es una buena idea si alguien sabe algo, probablemente sea el. Asi que decides pedirle ayuda cuando llegue."

            Mati @ Feliz "hola cabra chica."

            Amiga @ Preocupada "Hola Mati, oye [name] quiere decirte algo."

            hide Amiga
            hide mc

            "Hablas con el y accede a ayudarte."
            "Te cuenta sobre su amiga de la universidad que esta “transicionando” no sabes bien que significa eso, pero estas feliz de poder recibir ayuda de alguien."
            "Te alegra porder habertelo sacado del pecho y poder haber encontrado a alguien que sepa mas de esto"
            hide plaza
            hide Hermano 
            "te sientes apoyad[pronombre]"
            "No estas sol[pronombre] en esto."
            jump cap3
        
        "Hablar con el hermano de tu mejor amiga." if post or series:
            "Decides que lo mejor es hablar con el hermano de tu mejor amiga, el probablemente sepa algo o de alguien que pueda ayudarte." 
            show colegio
            "Vas a la escuela decidido a hacer esto bien." 
            "Esperas a que terminen las clases para acompañar a Bea a esperar a su hermano en la plaza." 
            hide colegio

            "Una vez que llega te armas de valor para decirle algo."
            show plaza

            show mc Hablando at left
            show Hermano Neutro at right

            ch "Hola Mati. ¿Puedo hablar contigo?"

            Mati "Claro, [name] ¿Que pasa?"

            ch "Es solo que... siento que tu puedes saber mas de esto… bueno, ultimamente me siento un poco confundid[pronombre]. Como si mi cuerpo no coincidiera con lo que siento por dentro."

            Mati @ Preocupado "Entiendo… ¿Has escuchado hablar de personas trans?"

            ch "Sí, un poco, pero no entiendo mucho. Aunque creo que soy eso." #soy ese

            Mati "Bueno, esta bien sentirse confundid[pronombre]. Conozco a algunas personas trans y han pasado por cosas parecidas, no es tan raro."

            ch "¿En serio? No sabía que conocias a alguien asi."

            Mati "Si, tengo una amiga en la universidad que es trans. Ha pasado por un proceso para vivir de acuerdo con su identidad de genero. Cada persona tiene su propio camino."

            ch "¿Como puedo saber mas? de verdad quiero ayuda."

            Mati "Hay muchas formas. Podemos buscar informacion o… puedo hablar yo con mi amiga para que te ayude un poco. "

            ch "¿De verdad?! oh muchas gracias Mati. Sabia que ibas a ayudarme."

            Mati @ Preocupado "¿Le has dicho a alguien mas? A la Bea por ejemplo."

            ch "No, no quiero dejarla fuera, pero me da un poco de miedo."

            Mati "Entiendo, pero a veces compartir esto es mejor. No creo que se lo tome mal, deberias decirle."

            ch "Gracias, voy a hablar con ella pronto… "

            Mati @ Feliz "Ah tranquilo, tu anda de a poco. "


            hide plaza
            hide mc
            hide Hermano
            "El te ofrece ayuda a encontrar cosas y ropa que puedan ayudarte con tu “disforia”, como el llamo al sentimiento ese." 
            "Le agradeces profundamente y decides que debes hablar con su hermana ahora." 
            "Mientras aun estan en la plaza le dices un poco." 
            "Te sorprende lo comprensiva que se muestra con la noticia. "
            "Estas feliz, tienes ayuda y compañia." 
            "No estas sol[pronombre] en esto."
            jump cap3


label cap3:
    "Tras confiar a su circulo cercano sobre su identidad transgenero, [name] decide explorar la transicion legal, médica y social en Chile." 
    "Explica los procesos legales para cambiar su nombre y genero en documentos" 
    "considera opciones medicas como la terapia hormonal y planea como comunicar su identidad a las personas en su vida." 
    "Con el respaldo de sus amigos, [name] se siente mas seguro al tomar estos pasos significativos en su viaje de autenticidad y autodescubrimiento."
    pass


label Agradecimientos:
    show us:
        xpos 700
        zoom 3.0    


    "Gracias por jugar"
    "Este juego fue creado por:\n
        Forg"