#!/usr/bin/python

################################################
# module: linalg_02.py
# description: matrix multiplication in numpy
# bugs to vladimir kulyukin via canvas
################################################

import numpy as np

A = np.array([[7, 1],
              [4, -3],
              [2, 0]])
B = np.array([[2, 1, 7],
              [0, -1, 4]])
C = np.array([[1, -1, 3],
              [2, 2, 3],
              [-1, 4, 7]])

print('A x B = ')
print(np.dot(A, B))
print('A x C = ')

try:
    ## This throws an exception
    print(np.dot(A, C))
except:
    print('Undefined')

# matrix multiplication is not commutative
A1 = np.array([[0, 2],
               [3, 5]])
A2 = np.array([[0, 1],
              [2, 5]])

## This example illustrates that matrix
## multiplication is not commutative.
print('A1=', A1)
print('A2=', A2)
print('A1 x A2')
print(np.dot(A1, A2))
print('A2 x A1')
print(np.dot(A2, A1))
