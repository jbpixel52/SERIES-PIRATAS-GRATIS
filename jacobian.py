#%%
import numpy as np
LIMIT = 15
iteracion = 0
A = np.array([[4., -1., 1., 0.], [4., -8., 1., 2.], [-2., -1., 10., -1.], [1, -4., 3., 10.]])
b = np.array([7., -23., 16., -15.])
for i in range(A.shape[0]):
    row = ["{}*x{}".format(A[i, j], j + 1) for j in range(A.shape[1])]
    print(" + ".join(row), "=", b[i])
    print()
x = np.zeros_like(b)
for it_count in range(LIMIT):
    iteracion = it_count
    #print("Current solution:", x)
    x_new = np.zeros_like(x)
    for i in range(A.shape[0]):
        s1 = np.dot(A[i, :i], x[:i])
        s2 = np.dot(A[i, i + 1 :], x[i + 1 :])
        x_new[i] = (b[i] - s1 - s2) / A[i, i]
    if np.allclose(x, x_new, atol=1e-10, rtol=0.):
        break
    x = x_new

print("Iteracion", iteracion, ":")
print("Solution:")
print(x)
error = np.dot(A, x) - b
print("Error:")
print(error)