######################################################
# module: cs3430_s24_hw01.py
# bugs to vladimir kulyukin in canvas
# YOUR NAME: Paige Davidson
# YOUR A-NUMBER: A02338425
######################################################

import numpy as np
import numpy.linalg
import random

# ========== Problem 1 ==============

def cs3430_s24_hw_01_prob_1_1():
    A = np.array(
        [[1, 1],
         [1, 4]],
         dtype=float) 
    b = np.array([[3],
                  [10]],
                  dtype=float) 
    try:
        x = np.linalg.solve(A, b)
    except np.linalg.LinAlgError as e:
        return e
    return A, x, b

def cs3430_s24_hw_01_prob_1_2():
    A = np.array(
        [[0, 1, -3],
         [2, 3, -1],
         [4, 5, -2]],
        dtype=float)
    b = np.array([[-5],
                  [7],
                  [10]],
                  dtype=float)
    try:
        x = np.linalg.solve(A, b)
    except np.linalg.LinAlgError as e:
        return e
    return A, x, b

def cs3430_s24_hw_01_prob_1_3():
    A = np.array(
        [[2, -1, 3],
         [3,  0, 2],
         [-2, 1, 4]],
        dtype=float)
    b = np.array([[4],
                  [5],
                  [6]],
                  dtype=float)  
    try:
        x = np.linalg.solve(A, b)
    except np.linalg.LinAlgError as e:
        return e
    return A, x, b

# def cs3430_s24_hw_01_prob_1_4():
#     A = np.array([[-1, 0, 1, -1],
#          [2, 2, -1, -7],
#          [4, -1, -9, -5],
#          [3, -1, -8, -6]], 
#          dtype=float)
#     b = np.array([[3],
#             [1],
#             [10],
#             [1]],
#             dtype=float)   
#     try:
#         x = np.linalg.solve(A, b)
#     except np.linalg.LinAlgError as e:
#         return e
#     return A, x, b
def cs3430_s24_hw_01_prob_1_4():
    A = np.array([[-1, 0, 1, -1],
        [2, 2, -1, -7],
        [4, -1, -9, -5],
        [3, -1, -8, -6]],
        dtype=float)
    b = np.array([[3],
        [1],
        [10],
        [1]],
        dtype=float)
    try:
        x = np.linalg.solve(A, b)
    except np.linalg.LinAlgError as e:
        return e
    return A, x, b


### ============== Problem 2 ==================

def leibnitz_det(mat):
    # Base case: determinant of 1x1 matrix
    if mat.shape[0] == 1:
        return mat[0, 0]

    # Initialize determinant
    det = 0

    # Iterate over the first row to calculate the determinant using cofactors
    for j in range(mat.shape[1]):
        # Calculate the minor matrix excluding the current row and column
        minor_matrix = np.delete(np.delete(mat, 0, axis=0), j, axis=1)
        
        # Calculate the cofactor (sign is determined by the position)
        cofactor = (-1) ** j * mat[0, j] * leibnitz_det(minor_matrix)
        
        # Add cofactor to the determinant
        det += cofactor

    return det

### ============== Problem 3 ==================

def cramers_rule(A, b):
     # Check if the determinant of A is non-zero
    determinant_A = leibnitz_det(A)
    if determinant_A == 0:
        raise ValueError("Determinant of A is zero. Cramer's rule cannot be applied.")

    # Get the number of variables (columns)
    numVariables = A.shape[1]

    # Initialize empty array in correct format
    solutions = np.empty((len(b), 1), dtype=float)

    # Iterate over each variable xi
    for i in range(numVariables):
        # Create a copy of A to replace the i-th column with the column vector b
        Ai = A.copy()

        Ai[:, i] = b[:, 0] 

        determinant_Ai = leibnitz_det(Ai)

        # Calculate the solution for xi using Cramer's rule
        xi = determinant_Ai / determinant_A

        # put solution in empty array
        solutions[i] = xi

    return solutions

### ===========================================    

    
              
