#!/usr/bin/python

##############################
# module: linalg_01.py
# description: matrix addition
# bugs to vladimir kulyukin in canvas
##############################

import numpy as np

A = np.array([[7, -1, -2],
              [3, 3, 0]])

B = np.array([[2, -3, 4],
              [1, 5, 9]])

C = np.array([[2, 1],
              [7, 3],
              [9, 2]])

D = np.array([[1, 2, 3],
              [0, 0, 0],
              [5, 6, 7],
              [0, 0, 0]])

print('A+B={}'.format(np.add(A, B)))
print('B+A={}'.format(np.add(B, A)))

### Some matrices cannot be added, because
### their dimensions are not conformable (i.e.,
### compatible).

try:
    print('A+C={}'.format(np.add(A, C)))
except Exception:
    print('Matrix addition undefined...')
    
try:
    print('B+C={}'.format(np.add(A, C)))
except Exception:
    print('Matrix addition undefined...')

try:
    print('A+D={}'.format(np.add(A, D)))
except Exception:
    print('Matrix addition undefined...')








            
    


    

