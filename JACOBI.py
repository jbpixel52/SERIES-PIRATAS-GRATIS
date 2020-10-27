#%%
from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot

def jacobi(A,b,N=25,x=None):                                                                
    if x is None:
        x = zeros(len(A[0]))
                                   
    D = diag(A)
    R = A - diagflat(D)

    for i in range(N):
        x = (b - dot(R,x)) / D
    return x

A = array([[10.0,12.0,15.0],[6.0,8.0,12.0],[12.0,12.0,18.0]])
b = array([[960.0],[660.0],[1080.0]])
guess = array([10.0,100.0])

sol = jacobi(A,b,N=25,x=guess)


print('x:')
pprint(sol)