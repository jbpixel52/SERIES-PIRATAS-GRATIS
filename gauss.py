#%%
import numpy as np

ITERATION_LIMIT = 2000

# initialize the matrix
A = np.array([[10,6,12],
              [12,8,12],[15,12,18]])
# initialize the RHS vector
b = np.array([960,660,1080])

print("Sistema:")
for i in range(A.shape[0]):
    row = ["{0:3g}*x{1}".format(A[i, j], j + 1) for j in range(A.shape[1])]
    print("[{0}] = [{1:3g}]".format(" + ".join(row), b[i]))

x = np.zeros_like(b)
for it_count in range(1, ITERATION_LIMIT):
    x_new = np.zeros_like(x)
    print("Iteracion {0}: {1}".format(it_count, x))
    for i in range(A.shape[0]):
        s1 = np.dot(A[i, :i], x_new[:i])
        s2 = np.dot(A[i, i + 1 :], x[i + 1 :])
        x_new[i] = (b[i] - s1 - s2) / A[i, i]
    if np.allclose(x, x_new, rtol=1e-2): 
        break
    x = x_new

print("Solucion: {0}".format(x))
error = np.dot(A, x) - b
print("Error: {}".format(error))