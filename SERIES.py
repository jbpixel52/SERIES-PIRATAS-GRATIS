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


def esin():
    n = 10
    x = math.pi / 4
    prox_sen = 0
    prox_e = 0
    real_seno = math.sin(math.radians(45))
    real_ex = math.exp(x)
    real_producto = real_seno * real_ex
    error_producto = 1
    for i in range(n):
        prox_sen += (((-1) ** i) * (x ** (2 * i + 1))) / math.factorial(2 * i + 1)
        prox_e += (x ** i) / math.factorial(i)
        aprox_product = prox_sen * prox_e
        error_producto = abs(real_producto - aprox_product)
    print('<TAYLOR: e^x * sin(x)>')
    print('iteraciones:', n)
    print('Aproximacion:', aprox_product)
    print('Error de 10^-3:',error_producto)

SENOR_PIG()
print('\n---------')
EULER()
print('\n---------')
EULER_SQUARE()
print('\n---------')
LOGARTIMO()
print('\n---------')
esin()
# %%
