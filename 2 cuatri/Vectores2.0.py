import random
import numpy

def main():
    while True:
        print ("""
        Menu
        
        1.- agregar valores de ambos vectores
        2.- sumar vectores
        3.- restar vectores 
        4.- randomizar vectores
        5.- normalizar vector A
        6.- normalizar vector B 
        7.- salir""")
        global respuesta
        respuesta = input (" ")
        if respuesta == "1":
            valor_de_vectores()
        elif respuesta == "2":
            sumar()
        elif respuesta == "3":
            restar()
        elif respuesta == "4":
            randomizar_vectores()
        elif respuesta == "5":
            normalizar_A()
        elif respuesta == "6":
            normalizar_B()
        elif respuesta == "7":
            break
        else:
            print ("equivocado")
        
def valor_de_vectores():
        print ("primer vector")
        global vector_AA,vector2_BA,X1,X2,Y1,Y2
        X1 = int(input("valor de x:  "))
        Y1 = int(input("valor de Y:  "))
        print ("segundo Vector")
        X2 = int(input("valor de x:  "))
        Y2 = int(input("valor de Y:  "))
        vector_AA = (X1, Y1)
        vector2_BA = (X2, Y2)
        print (vector_AA, vector2_BA)
        main()
     
def randomizar_vectores():
        print ("primer vector")
        global vector2_BB, vector_AB, X1,X2,Y1,Y2
        X1 = random.choice([-1,-2,-3,-4,-5,5,4,3,2,1])
        Y1 = random.choice([-1,-2,-3,-4,-5,5,4,3,2,1])
        print ("segundo Vector")
        X2 = random.choice([-1,-2,-3,-4,-5,5,4,3,2,1])
        Y2 = random.choice([-1,-2,-3,-4,-5,5,4,3,2,1])
        vector_AB = (X1, Y1)
        vector2_BB = (X2, Y2)
        print (vector_AB, vector2_BB)
        main()

def sumar():
    rs = X1 + X2, Y1 + Y2
    print (rs)
    main()

def restar():
    rr = X1 - X2, Y1 - Y2
    print (rr)
    main()

def normalizar_A():
    rn = numpy.linalg.norm(vector_AA)
    print (rn)
    main()

def normalizar_B():
    rn = numpy.linalg.norm(vector_AA)
    print (rn)
    main()

main()

