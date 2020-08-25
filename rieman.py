# %%

import math
#import mathplotlib

#import sympy



def EULER():
    print('<EULER>')
    n = 150
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
    print('<PI>')
    serie = float()
    odd = 1
    for k in range(0, 300):
        serie += (((-1)**(k+1)))/((2*k)+1)

    pi = float(serie*4)
    print('Pi:', pi)
    print('Con arco tangente:', math.atan(1)*4)
    print("Absoluto con <math.pi> :", abs(math.pi))

def EULER_SQUARE():
    print('<Euler^2>')
    n = 100
    suma =0
    for i in range(1,n+1):
        suma += ((-1)**(i+1))/(i)

    print(suma)

def MAC_SERIES():
    n=100
    suma=0
    for i in range(1,n):
        pass

SENOR_PIG()
print('\n---------')
EULER()
print('\n---------')
EULER_SQUARE()
