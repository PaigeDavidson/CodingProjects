################################
# cramer_example.py
# description: source code for
# the example we discussed in class
# on 01/17/2024.
#################################
import numpy as np

A = np.array([[5, -2, 1],
              [3, 2, 0],
              [1, 1, -1]],
             dtype=float)
b = np.array([[1],
              [3],
              [0]],
             dtype=float)
B0, B1, B2 = A.copy(), A.copy(), A.copy()
B0[:,0] = b.reshape(3)
B1[:,1] = b.reshape(3)
B2[:,2] = b.reshape(3)
detA = np.linalg.det(A)
x = np.array([[np.linalg.det(B0)/detA],
              [np.linalg.det(B1)/detA],
              [np.linalg.det(B2)/detA]])
assert np.allclose(np.dot(A, x), b)
print('Assertion passed...')
