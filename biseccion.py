# %%
import math
from sympy import *
from numpy import *
from scipy.optimize import newton

def bisection(f,a,b,N):
    if f(a)*f(b) >= 0:
        print("Bisection falla.")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = (a_n + b_n)/2
        f_m_n = f(m_n)
        print('m_n:',m_n,'|a_n:',a_n,'|b_n:',b_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("SOLUCION EXACTA.")
            return m_n
        else:
            print("METODO FALLO.")
            return None
    eror = (b_n - a_n) / abs(m_n)
    notacion_e = "{:e}".format(eror)

    print('Error:', notacion_e)
    return (a_n + b_n)/2


f = lambda x: 2*math.sin(x)-(x**2)
print(bisection(f, 1, 2, 10))




def dx(f, x):
    return abs(0-f(x))
 
def newtons_method(f, df, x0, e):
    delta = dx(f, x0)
    while delta > e:
        x0 = x0 - f(x0)/df(x0)
        delta = dx(f, x0)
    print('Root is at: ', x0)
    print('f(x) at root is: ', f(x0))

