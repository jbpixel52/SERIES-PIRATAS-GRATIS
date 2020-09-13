#%%
import math

def f(x):
    return 2*math.sin(x)-(x**2)
def g(x):
    return math.sqrt(2*math.sin(x))

def fixedPointIteration(x0, e, N):
    print('\n\n*** PUNTO FIJO ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        x1 = g(x0)
        print('ITERACION-%d, x1 = %0.10f Y f(x1) = %0.10f' % (step, x1, f(x1)))
        x0 = x1

        step = step + 1
        
        if step > N:
            flag=0
            break
        
        condition = abs(f(x1)) > e

    if flag==1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')

x0 = input('Adivina: ')
e = input('Error: ')
N = input('Pasos: ')

x0 = float(x0)
e = float(e)

N = int(N)

fixedPointIteration(x0,e,N)
