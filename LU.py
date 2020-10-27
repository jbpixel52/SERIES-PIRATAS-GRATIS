#%%
from scipy.linalg import lu
import numpy as np


A= np.array([[25,15 ,-5 ,-10],[15, 10, 1, -7],[-5, 1, 21, 4],[-10, -7, 4, 18]])
b = [[0], [10], [76], [60]]
print('DESCOMPOSICION LU:')
p, l, u = lu(A)
np.allclose(A - p @ l @ u, np.zeros((4, 4)))
print(p,l,u)