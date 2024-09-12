########################################
# module: random_mat_inv.py 
# description: converting random
# matrices and comparing the
# product of AA^-1 to identity
# matrices; this is the source code
# of an example we discussed in class on
# 01/17/2024.
#
# bugs to vladimir kulyukin in canvas
########################################


## generate random 3x3 mat until
## you get a matrix whose determinant is not 0.
## if the determinant of A is not 0, i.e.,
## A is invertible, then use np.close to
## to invert A, i.e., compute A^-1 and
## then use np.close to compare A*A^-1 to
## a 3 x 3 identity matrix.
## np.eye(n) returns n x n identity matrix.

import numpy as np
import numpy.random
if __name__== '__main__':
    n = 3
    A = np.random.rand(n, n)
    while not np.allclose(np.linalg.det(A), 0):
        A = np.random.rand(n, n)
        break
    assert np.allclose(np.dot(A, np.linalg.inv(A)),
                       np.eye(n))
    print('Assertion passed')
