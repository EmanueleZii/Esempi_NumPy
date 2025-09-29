import numpy as np

a = np.array([[1, 2, 3],
            [0, 1, 4],
            [5, 6, 0]])

A_inv = np.linalg.inv(a)
print("Matrice inversa:")
print(A_inv)


#norma di un vettore
v = np.array([1, 2, 3])
norm_v = np.linalg.norm(v)
print("Norma del vettore v:")
print(norm_v)