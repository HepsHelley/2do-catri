import matplotlib.pyplot as plt
import random
from math import *
import numpy


while True:
    print ("""MENU
    
    1.- asignaro valores al vector
    2.- valores random
    3.- normalizar el vector
    4.- salir""")

    respuesta = input(" ")

    if respuesta == "1":
        X1 = input ("valor de X:  ")
        Y1 = input ("valor de Y:  ")
    elif respuesta == "2":
        X1 = random.choice([-5,-4,-3,-2,-1,1,2,3,4,5])
        Y1 = random.choice([-5,-4,-3,-2,-1,1,2,3,4,5])
    elif respuesta == "3":
        numpy.linalg.norm(X1)
        numpy.linalg.norm(Y1)
    elif respuesta == "4":
        break
    else:
        print ("no existe esa opcion")


    class primer_vector:
        def __init__(self,a,b):
            self.vector_1 = int(a)
            self.vector_2 = int(b)

    def grafica_1(e):

        x, y = e.vector_1, e.vector_2

        izda = min(-1, x-1)
        dcha = max(1, x+1)
        abajo = min(-1, y-2)
        arriba = max(1, y+1)

        plt.quiver([x], [y], angles='xy', scale_units='xy', scale=1)

        plt.axhline(0, color='black')
        plt.axvline(0, color='black')

        plt.xlim([izda, dcha])
        plt.ylim([abajo, arriba])
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('({},{})'.format(e.vector_1,e.vector_2))
        plt.show()

    vector = primer_vector(X1,Y1)
    grafica_1(vector)

