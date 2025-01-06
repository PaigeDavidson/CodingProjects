#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: cs3430_s24_midterm01.py
# YOUR NAME: Paige Davidson
# YOUR A-NUMBER: A02339425
# WRITE THE TIME IT TOOK YOU TO COMPLETE THIS EXAM.: ~4 hours
##############################################################

import numpy as np
import numpy.linalg

### put your imports from your previous/current assignments.
from cs3430_s24_hw01 import cramers_rule
from cs3430_s24_hw02 import lud_solve, bsubst, fsubst
from cs3430_s24_hw04 import simplex, get_solution_from_tab

### ================ Problem 01 ========================

def solve_lin_sys_with_gje(a, b):
    x = np.linalg.solve(a, b)
    assert np.allclose(np.dot(a, x), b) == True
    return x

### ================ Problem 02 ========================

def solve_lin_sys_with_cramer(A, b):
    return cramers_rule(A, b)

### ================ Problem 03 =========================

def solve_lin_sys_with_bsubst(A, n, b, m):
    return bsubst(A, n, b, m)

### ================ Problem 04 =========================

def solve_lin_sys_with_fsubst(A, n, b, m):
    return fsubst(A, n, b, m)

### ================ Problem 05 =========================

def solve_lin_sys_with_lud(A, n, b, m):
    return lud_solve(A, n, b, m)


### ================ Problem 06 =========================

"""
Standard Maximization Problem (SMP): 

An SMP is a problem that maximizes a linear function for cost or profit. 
For a problem to be an SMP, it must:
1) Have a linear function to maximize
2) All decision variables are constrained to be non-negative
3) All "regular" constrants (not common sense constraints) are linear and in the form 
    linear sum <= r \in R (a positive real number).


Objective Function: 

An objective function is a function P to be maximized or minimized in an optimization problem. 
The objective function is a function of decision variables and usually involves calculating cost or profit 
with decision variable values. The objective function will be represented in the last row of a tableu.

Corner Point:

A corner point is an extreme point of a feasible set such that any segment in the set that contains 
the critical point, contains it as an endpoint. Each corner point is a solution of the system of equations.

Feasible Set:

A feasible set is The intersection of constraints in an optimization problem. The feasible set determines 
where a solution can be found if it exists.  

Two conditions when the simplex algorithm stops:

The simplex algorithm stops under the conditions when:
1) There is no entering variable becasue all the entries in the p-row (objective function) are positive which 
    means that the solution is already contained in the tableu.
2) There is an entering variable but no departing variable becasue there are no positive entries in 
    the column of the entering variable which means the SMP has no solution.  

Bounded Feasible Set:

If a feasible set is bounded, then an objective function obtains
its max/min value at the corner point of the feasible set.

Unbounded Feasible Set:
If a feasible set is unbounded, then an objective function obtains its max/min value 
at the corner point of the feasible set or takes large positive/negative values on the feasible set. 


Does the simplex algorithm work on any linear programmng problems or only on SMPs?

Yes, the simplex algorithm can be applied to any linear programming problem. 

"""

### ================ Problem 07 =========================

"""
p = 13x + 7y + 5z
Slack Equations:

6x + 0y + 1z + u = 480
0x + 2y + 5z + v = 502
9x - 7y + 6z + w = 902

Slack variables: u, v, w

Initial Tableu:

    ____________________________________________________
        |  x  |  y  |  z  |  u  |  v  |  w  |   B. S.  |
    ----------------------------------------------------
      u |  6  |  0  |  1  |  1  |  0  |  0  |    122   |
    ----------------------------------------------------
      v |  0  |  2  |  5  |  0  |  1  |  0  |    502   |
    ----------------------------------------------------
      w |  9  | -7  |  6  |  0  |  0  |  1  |    902   |
    ----------------------------------------------------
      p | -13 | -7  | -5  |  0  |  0  |  0  |     0    |
"""

### ================ Problem 08 =========================

"""
    ____________________________________________________
        |  x0 |  x1 |  x2 |  x3 |  x4 |  x5 |   B. S.  |
    ----------------------------------------------------
     x3 |  6  |  6  |  7  |  1  |  0  |  0  |    190   |
    ----------------------------------------------------
     x4 |  12 |  7  | 22  |  0  |  1  |  0  |    510   |
    ----------------------------------------------------
     x5 |  22 | 10  |  12 |  0  |  0  |  1  |    810   |
    ----------------------------------------------------
      p |  -7 | -22 | -12 |  0  |  0  |  0  |     0    |
                 ^
The pivot is the biggest negative (or smallest) value in the p-row. Since the smallest value in the 
p-row is -22, that will be the pivot value. The pivot is in row p, column x1

"""

### ================ Problem 09 =========================

"""

Numerical instability is the idea that there can be say three small positive real numbers z1, z1, and z3
such that z1 < z2 < z3 (for example: z1 = 5e-324, z2 = 1e-323, z3 = 5e-323). These three numbers are added 
to some positive real numbers (say x=1009) so that  x + z1 = x + z2 = x + z3. 
Though the numbers are mathematically different, they are interpreted as equalities by programming 
languages like python3. For example, 0 < z1 < z2 < z3 will return True but also x + z1 = x + z2 = x + z3 
will return True. When finite calculations on a computer are applied to a universe with infinite 
values sometimes weird results can occur. 

"""

### ================= Problem 10 ==========================

def farming_land_allocation():
    ### Set up your tableau by replacing Nones
    ### with appropriate values.
    in_vars = {0:3, 1:4}
    m = np.array([[120, 80, 50, 1, 0, 1000],
                  [6  ,  4,  4, 0, 1,  600],
                  [-1.0, -1.2, -2.0, 0, 0, 0]],
                dtype=float)
    tab = (in_vars, m)
    ### call simplex
    tab, solved = simplex(tab)
    ### get solution
    assert solved is True
    sol = get_solution_from_tab(tab)
    ### return it
    return sol
