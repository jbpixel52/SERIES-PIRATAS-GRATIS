#%%
from scipy.optimize import newton
from sklearn.utils.testing import assert_almost_equal
import math

def f(x):
    return 2*math.sin(x) - (x**2)
def df(x):
    return math.cos(x)-x

def dx(f, x):
    return abs(0-f(x))
    
def newton_metodo(f, df, x0, e, print_res=False):
    delta = dx(f, x0)
    while delta > e:
        x0 = x0 - f(x0)/df(x0)
        delta = dx(f, x0)
    if print_res:
        print ('Raiz en: ', x0)
        print ('f(x) en la raiz en: ', f(x0))
    return x0

def test_with_scipy(f, df, x0s, e):
    for x0 in x0s:
        my_newton = newton_metodo(f, df, x0, e)
        scipy_newton = newton(f, x0, df, tol=e)
        assert_almost_equal(my_newton, scipy_newton, decimal=4)
        print ('Prueba...')

if __name__ == '__main__':
    # run test
    x0s= [1,1.5]    
    #test_with_scipy(f, df, x0s, 10e-4)
        
    for x0 in x0s:
        newton_metodo(f, df, x0, 10e-4, True)