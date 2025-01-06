
#################################################
# Module: cs3430_s24_hw02.py
# YOUR NAME Paige Davidson
# YOUR A#02339425
# bugs to vladimir kulyukin in canvas
#################################################

import numpy as np
import pickle
import os

### =============== Problem 1 =============================

def lu_decomp(a, n):
    """ 
    lu_decomp(a, n) returns u, l such that np.dot(l, u) === a.
    a is an nxn matrix that is reduced to the upper and lower triangular matrices. 
    throws exception when there is no pivot in a column or rows must be swapped
    to create a pivot.
    lu_decomp(a, n) is destructive in that a is destructively modified into u.
    """

    # create I matrix
    I = np.eye(n, dtype=float)

    # goes through matrix column by column
    for col in range(I.shape[1]):
        for row in range(col + 1, I.shape[0]):
            # find the pivot in the column
            if a[row][col] == 0: 
                continue
            else:
                # calculate r value based on previous row 
                r = - a[row][col] / a[col][col]

                #  add r value to I matrix
                I[row][col] = -r

                # calculate all rows
                a[row][col:] = a[row][col:] + r * a[col][col:]

    # return u and l - updated A and I matrix
    l = I
    u = a
    return u, l


### =============== Problem 2 =============================

def bsubst(a, n, b, m):
    """
    bsubst uses back substitution to solve ax = b1, b2, ..., bm.
    a is an nxn upper-triangular matrix, n is its dimension.
    b is an nxm matrix of vectors b1, b2, ..., bm. 
    returns x.

    Backward substitution to solve the system Ax = B.
    
    Parameters:
    - a: n x n upper-triangular matrix
    - n: dimension of the matrix a
    - b: n x m matrix of m n x 1 vectors
    - m: number of vectors in the matrix b
    
    Returns:
    - x: n x m matrix of m n x 1 vectors
    """
    # decompose a to l and u
    u, l = lu_decomp(a.copy(), n)

    # set up x matrix
    x = np.zeros((n, m), dtype=float)

    # solve Ux = y for x with back substitution
    for j in range(m):
        x[n-1, j] = b[n-1, j] / u[n-1, n-1]
        for i in range(n-2, -1, -1):
            sum_terms = np.dot(u[i, i+1:], x[i+1:, j])
            x[i, j] = (b[i, j] - sum_terms) / u[i, i]

    return x


def fsubst(a, n, b, m):
    """
    fsubst uses forward substitution to solve ax = b1, b2, ..., bm.
    a is an nxn lower-triangular matrix, n is its dimension.
    b is an nxm matrix of vectors b1, b2, ..., bm.
    returns x.
    """

    # set up x matrix
    x = np.zeros((n, m), dtype=float)

    # solve Ly = b for y with forward substitution - a is the L matrix
    for j in range(m):
        for i in range(n):
            sum_terms = np.dot(a[i, :i], x[:i, j])
            x[i, j] = (b[i, j] - sum_terms) / a[i, i]

    return x

### =============== Problem 3 ====================

def lud_solve(a, n, b, m):
    """
    a is an nxn matrix; b is m nx1 vectors.
    Use forward subst to solve Ly = b for y.
    Use back    subst to solve Ux = y for x.
    Then LUx = Ly = b.
    Returns x.
    """
    # uses the LU decomposition to factor the matrix a into U and L
    u, l = lu_decomp(a.copy(), n)
    # uses forward substitution to solve Ly = b for y
    y = fsubst(l, n, b, m)
    # uses back substitution to solve Ux = y for x
    x = bsubst(u, n, y, m)

    return x



