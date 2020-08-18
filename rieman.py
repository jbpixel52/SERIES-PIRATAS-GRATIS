import math


def EULER():
    n = int(input("Pasos: "))
    suma = 1
    for i in range(1, n+1):
        suma = suma+(1/math.factorial(i))
    absolute = abs(math.e)
    error = absolute-suma
    relativeError = error/absolute
    print("Relative Error:", relativeError)
    print("Absoluto", absolute)
    print("Serie:", suma)
    print('Error:', error)


def LOGARTIMO():
    print('\n_________\nLOGARITMO')

def SENOR_PIG():
    serie = float()
    #ciclos = int(input("Ciclos: "))
    odd = 1
    for k in range(0, 400000):
        serie += (((-1)**(k+1)))/((2*k)+1)

    pi = float(serie*4)
    print('Pi:', pi)
    print('Con arco tangente:', math.atan(1)*4)
    print("Absoluto con <math.pi> :",abs(math.pi))


#EULER()
SENOR_PIG()
