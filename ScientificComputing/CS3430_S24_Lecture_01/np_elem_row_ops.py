#!/usr/bin/python

###############################################
# module: np_elem_row_ops.py
# description: matrix creation, row and column access,
# elementary row operations with numpy.
# bugs to vladimir kulyukin in canvas.
###############################################

import numpy as np

## Let's create a matrix. This is the matrix
## we worked with in lecture 01 on 01/08/2024.
A = np.array([
        [7, 1],
        [4, -3],
        [2, 0]
        ])

## ============ Row and Column Access ============
## To get row r in a 2D matrix M, do, M[r,:]
## A.shape returns (r, c), where r is the number of
## rows and c is the number of columns.
for r in range(A.shape[0]):
    print('row {} = {}'.format(r, A[r,:]))

## To get column c in a 2D matrix M, do M[:,c].
## This is not necessary for standard Gauss-Jordan
## reduction, but it's good to see how to access
## columns.
for c in range(A.shape[1]):
    print('col {} = {}'.format(c, A[:,c]))

## ============ Elementary Row Ops ============    

## 1) Row Interchange: Interchanging two rows r1, r2 in a matrix M, do
## M[[r1, r2]] = M[[r2, r1]]. This operation is destructive. I'll
## show you below how to make a copy of a matrix to avoid potential
## hard of destructive modification.
print(A)
A[[1, 2]] = A[[2, 1]]
print(A)

## 2) Row Scaling: To multiply a row r by a scalar s in a 2D matrix
## M, do s*M[r,:]. 
print('4*{} = {}'.format(A[1,:], 4.0*A[1,:]))

## To multiply a colum c by a scalar s in a 2D matrix
## M, do s*M[:,c].
print('4*{} = {}'.format(A[:,0], 4.0*A[:,0]))

## This is how you can replace a row with a scalar
## multiple of itself. Here's how to make a copy of a matrix.
A1 = A.copy()
A1[1,:] = 4.0*A[1,:]
print(A1)

## 3) Row Addition: To replace row r1 in 2D matrix M with the sum
## of r and a multiple of row r2,
## do M[r1,:] = M[r1,:] + s*M[r2,:]
A2 = A.copy()
print(A2)
A2[1,:] = A2[1,:] + 2*A2[2,:]
print(A2)

## Same operation as above but on columns. Again, not
## necessary for Gauss-Jordan but useful for the sake of generality.
A3 = A.copy()
print(A3)
A3[:,1] = A3[:,1] + 2*A3[:,0]
print(A3)










