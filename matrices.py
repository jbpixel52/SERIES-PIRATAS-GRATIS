#%%
import numpy as np


x = np.array([[1, 2], [3, 4]])
print('x{}'.format(x))


y = np.linalg.inv(x)

print('y{}'.format(y))