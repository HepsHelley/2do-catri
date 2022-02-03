import random


lista_de_palabras = ["programacion", "movilidad social", "dibujo digital","narrativa", "PPA"]
palabra_secreta = random.choice(lista_de_palabras)
total_caracteres = len(palabra_secreta)

victoria = 0
def validacion():
    global victoria
    respuesta_2 = input ("escriba una palabra (si necesitas ayuda pica *): ")
    numero_de_letras = len(respuesta_2)
    if respuesta_2 == "*":
        print (" ")
        print('_ ' * len(total_caracteres))
        print (" ")
    if numero_de_letras == total_caracteres:
        victoria += 1
    elif numero_de_letras != total_caracteres:
        victoria >= 0


print ("""

    escoge una dificultad
    
    1.- ¿puedo jugar papá?
    
    2.- no me hagas daño :c
    
    3.- es todo lo que tienes?
    
    4.- lastimame!!!!!!!!!

""")

respuesta_1 = int(input(" "))
dificultad_1 = [1,2,3,4,5,6,7,8,9,10]
dificultad_2 = [1,2,3,4,5,6,7,8]
dificultad_3 = [1,2,3,4,5]
dificultad_4 = [1]


if respuesta_1 == 1:
    for i in range (len(dificultad_1)):
        print ("tienes 10 intentos, este es el intento ", i + 1)
        if i == 9:
            print ("tus vidas se acabaron")
            break
        elif victoria == 1:
            print ("ganaste el juego!!!")
            break
        elif i < 10:
            validacion()    
elif respuesta_1 == 2:
    for n in range (len(dificultad_2)):
        print ("tienes 10 intentos, este es el intento ", n + 1)
        if n == 7:
            print ("tus vidas se acabaron")
            break
        elif victoria == 1:
            print ("ganaste el juego!!!")
            break
        elif n < 8:
            validacion() 
elif respuesta_1 == 3:
    for j in range (len(dificultad_3)):
        print ("tienes 10 intentos, este es el intento ", j + 1)
        if j == 4:
            print ("tus vidas se acabaron")
            break
        elif victoria == 1:
            print ("ganaste el juego!!!")
            break
        elif j < 5:
            validacion() 
elif respuesta_1 == 4:
    for h in range (len(dificultad_4)):
        if h > 1:
            print ("creiste que ibas a ganar???")
            break
        elif victoria == 1:
            print ("ganaste el juego!!!")
            break
        elif h < 2:
            validacion() 
elif respuesta_1 == 10:
    print ("""
    Conoces la trajedia de Darth Plagueis el sabio?
    Eso pensé. Los jedi no cuentan esa historia, es una leyenda sith. Darth Plagueis era un señor oscuro de los sith tan poderoso y 
    tan sabio que usaba la fuerza para influir sobre las midiclorianos y crear vida. Tenia tal conocimiento del lado oscuro que incluso
    podia impedir que sus amados murieran. El lado oscuro de la fuerza es el camino a muchas habilidades que varios consideran nada naturales.
    Se volvio muy poderoso, lo único que temia era perder su poder, lo que finalmente sucedió. Por desgracia le enseño a su aprendiz todo lo que 
    sabia, y su aprendiz lo asesinó mientras dormia. 
    Irónico, salvaba a otros de morir pero no pudo a si mismo
     """)
else:
    print ("no es valido y por no seguir indicaciones te sacare del juego.")

