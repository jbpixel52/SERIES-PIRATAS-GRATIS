import math


def EULER():
    n = int(input("Pasos: "))
    suma = 1
    for i in range(1, n+1):
        suma = suma+(1/math.factorial(i))
    absolute = abs(math.e)
    error = absolute-suma
    relativeError = error/absolute
    print("Relative Error:",relativeError)
    print("Absoluto",absolute)
    print("Serie:",suma )
    print('Error:',error)

def LOGARTIMO():

    print('\n_________\nLOGARITMO')


EULER()
LOGARTIMO()
