#%%

from scipy.linalg import cholesky
import numpy as np
A= np.array([[25,15 ,-5 ,-10],[15, 10, 1, -7],[-5, 1, 21, 4],[-10, -7, 4, 18]])
L = cholesky(A, lower=True)
print('descomposicion por Cholesky:\n')
print(L)