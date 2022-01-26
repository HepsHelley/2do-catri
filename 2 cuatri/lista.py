class Person:
    def __init__(self,nombre,edad,genero,estatura):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.estatura = estatura
def persona():
    nombre = input("Ingresa un nombre: ")
    nombres.append(nombre)
    edad = input("ingresa la edad: ")
    edades.append(edad)
    genero = input ("ingresa el genero: ")
    generos.append(genero)
    estatura = input ("ingrese la estatura: ")
    estaturas.append(estatura)
    person = Person(nombre,edad,genero,estatura)
    main()
def agregar_persona():
    nombre = input("Ingresa un nombre: ")
    nombres.append(nombre)
    edad = input("ingresa la edad: ")
    edades.append(edad)
    genero = input ("ingresa el genero: ")
    generos.append(genero)
    estatura = input ("ingrese la estatura: ")
    estaturas.append(estatura)
def ver_lista():
    print ("que datos quiere ver? ")
    posicion = input (" ")
    if posicion == "0":
        print ("nombre " + nombres[0],
                "edad " + edades[0], 
                "genero " + generos[0], 
                "altura " + estaturas[0])
    elif posicion == "1":
       print ("nombre " + nombres[1],
                "edad " + edades[1], 
                "genero " + generos[1], 
                "altura " + estaturas[1])
    elif posicion == "2":
        print ("nombre " + nombres[2],
                "edad " + edades[2], 
                "genero " + generos[2], 
                "altura " + estaturas[2])
    elif posicion == "3":
        print ("nombre " + nombres[3],
                "edad " + edades[3], 
                "genero " + generos[3], 
                "altura " + estaturas[3])   
def main():
    while True:
        print("""
        
        1.- agregar a una persona
        
        2.- cambiar las edades

        3.- mostrar la lista

        4.- auto destruccion

        """)
        seleccion = input (" ")
        if seleccion == "1":
            agregar_persona()
        elif seleccion == "2":
            print ("chale aun no se usar el for")
        elif seleccion == "3":
            ver_lista()
        elif seleccion == "4":
            print ("seguro que quieres hacer eso? y/n")
            seguro = input (" ")
            if seguro == "y":
                print("has escogido la muerte")
                break
            elif seguro =="n":
                print ("viviremos otro dia")
                continue

nombres = []
edades = []
generos = []
estaturas = []
persona()