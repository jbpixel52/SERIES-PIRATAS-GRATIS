# %%

import math
import scipy
import numpy
import matplotlib
from sympy import *


def EULER():
    print('\n<EULER>')
    n = 150
    suma = 1
    count_dec = 0;
    for i in range(1, n + 1):
        suma = suma + (1 / math.factorial(i))
        e_error = abs(suma - math.e)
        count_dec += 1;
        if e_error <= 0.001:
            break
    
    absolute = abs(math.e)
    error = e_error
    relativeError = error/absolute
    print("Relative Error:", relativeError)
    print("Absoluto", absolute)
    print("Serie:", suma)
    print('Error:', error)
    print("Numero de iteraciones:",count_dec)

def LOGARTIMO():
    print('\nLOGARITMO')
    suma = 0
    count_dec = 0
    n = 100
    for i in range(1,n+1):
        suma += (1) / ((2 ** i) * i)
        e_error = abs(suma - numpy.log(2))

        count_dec += 1;
        if e_error <= 0.001:
            break
    
    absolute = abs(numpy.log(2))
    error = e_error
    relativeError = error/absolute
    print("Relative Error:", relativeError)
    print("Serie:", suma)
    print('Error:', error)
    print("Numero de iteraciones:",count_dec)


def SENOR_PIG():
    print('\n<PI>')
    suma = 0
    count_dec = 0
    n = 5000
    for i in range(0, n):
        n+=1
        suma +=(2)/((4*i+1)*(4*i+3))
        e_error = abs(suma*4 - math.pi)
        count_dec += 1;
        if e_error < 0.001:
            break
        
    pi = suma*4
    print('Con arco tangente:', math.atan(1)*4)
    print("Absoluto con <math.pi> :", abs(math.pi))
    ###
    absolute = abs(math.pi)
    error = e_error
    relativeError = error/absolute
    print("Relative Error:", relativeError)
    print("Absoluto", absolute)
    print("Serie:", pi)
    print('Error:', error)
    print("Numero de iteraciones:",count_dec)

def EULER_SQUARE():
    print('\n<Euler^2>')
    count_dec = 0
    n=100
    suma = 0
    for i in range(0, n + 1):
        suma +=(2**i)/(math.factorial(i))
        #suma += ((-1)**(i+1))/(i)
        e_error = abs(suma - (math.e**2))
        count_dec += 1;
        if e_error <= 0.001:
            break
    
    absolute = abs(math.exp(2))
    error = e_error
    relativeError = error/absolute
    print("Relative Error:", relativeError)
    print("Absoluto", absolute)
    print("Serie:", suma)
    print('Error:', error)
    print("Numero de iteraciones:",count_dec)


def MAC_SERIES():
    print('\nMAC SERIES')

    suma = 0
    Xinput = (math.pi/4)
    count_dec=0
    x = Symbol('x')
    i = Symbol('i')
    f = (x**i)/(factorial(i)) 
    operacion = (lambdify(i,f))
    print('f(x)', operacion(1))
    e_error=0
    temp_f = f;
    for k in range(1, 100):
        #suma += operacion(Xinput)
        #print(suma)
        temp_f += (x ** (i * k)) / (factorial(k))
        temp_lamb = lambdify([i,x], temp_f)
        
        e_error = abs(temp_lamb(k, Xinput) - (math.exp(Xinput) * (math.sin(math.radians(Xinput)))))
        print('e_eeror:',e_error)
        suma += temp_lamb(k,Xinput)
        count_dec += 1
        if e_error <= 0.01:
            break
    

    print('Real:', (math.exp(Xinput)*math.sin(math. (Xinput))))
    ecuacionF = lambdify(x,suma)
    print('e^x sin(x):',ecuacionF(Xinput )) #AQUI VA EL VALOR DE X

SENOR_PIG()
print('\n---------')
EULER()
print('\n---------')
EULER_SQUARE()
print('\n---------')
LOGARTIMO()
print('\n---------')
MAC_SERIES()
# %%
