###############################
# module: cs3430_s24_hw04.py
# description: CS3430: S24: Assignment 04
# YOUR NAME: Paige Davidson
# YOUR A-NUmBER: A02339425
###############################
import numpy as np

def simplex(tab):
    """
    Apply the simplex algorithm to the tableaue tab.
    """
    array = tab[1]
    numRows = len(array)

    while True:
        # if there all value in p-row are positive, there is no entering variable
        if np.all(array[-1, :-1] >= 0):
            # return the current tableu as the solution
            return tab, True

        # Choose entering variable (most negative coefficient in the p-row)
        enteringVar = np.argmin(array[-1, :-1])

        # return false if there is an entering variable but not departing one
        if np.all(array[:-1, enteringVar] <= 0):
            # Problem has no solution
            return tab, False

        # Choose departing variable - the smallest non-negative ratio
        min_ratio = np.inf #initialize with infinity value
        departingVar = -1
        for i in range(numRows - 1):
            if array[i, enteringVar] > 0:
                ratio = array[i, -1] / array[i, enteringVar]
                if ratio < min_ratio:
                    min_ratio = ratio
                    departingVar = i

        # Perform pivot operation
        pivot = array[departingVar, enteringVar]
        # Dividing the departing row by the pivot element - ensures that pivot becomes one
        array[departingVar, :] /= pivot
        # Eliminate the entering variable from other rows
        for i in range(numRows):
            if i != departingVar:
                factor = array[i, enteringVar]
                array[i, :] -= factor * array[departingVar, :]

        # Update the entering variable
        tab[0][departingVar] = enteringVar


def get_solution_from_tab(tab):
    in_vars, mat = tab[0], tab[1]
    nr, nc = mat.shape
    sol = {}
    for k, v in in_vars.items():
        sol[v] = mat[k,nc-1]
    sol['p'] = mat[nr-1,nc-1]
    return sol

def display_solution_from_tab(tab):
    sol = get_solution_from_tab(tab)
    for var, val in sol.items():
        if var == 'p':
            print('p\t=\t{}'.format(val))
        else:
            print('x{}\t=\t{}'.format(var, val))

# ******************* Problem 2 Solutions *********************

# Problem 2.1
def problem2_1():
    print("Problem 2.1")
    in_vars = {0:3, 1:4}
    m = np.array([[3, 8, 1, 0, 24],
                [6, 4, 0, 1, 30],
                [-2, -3, 0, 0, 0]],
                dtype=float)
    tab = (in_vars, m)
    tab, solved = simplex(tab)
    assert solved is True
    print(get_solution_from_tab(tab))
    display_solution_from_tab(tab)

# Problem 2.2
def problem2_2():
    print("Problem 2.2")
    in_vars = {0:2, 1:3}
    m = np.array([[1,  -1, 1, 0, 4],
                [-1,  3, 0, 1, 4],
                [-1,  0, 0, 0, 0]],
                dtype=float)
    tab = (in_vars, m)
    tab, solved = simplex(tab)
    assert solved is True
    print(get_solution_from_tab(tab))
    display_solution_from_tab(tab)

# Problem 2.3
def problem2_3():
        print("Problem 2.3")
        in_vars = {0:3, 1:4, 2:5}
        m = np.array([[12,    6,    0, 1, 0, 0, 1500],
                      [18,   12,   10, 0, 1, 0, 2500],
                      [15,    8,    0, 0, 0, 1, 2000],
                      [-1.5, -0.8, -0.25, 0, 0, 0, 0]],
                     dtype=float)
        tab = (in_vars, m)
        tab, solved = simplex(tab)
        assert solved is True
        sol = get_solution_from_tab(tab)
        assert np.allclose(sol[0], 125.0)
        assert np.allclose(sol[2], 25.0)
        assert np.allclose(sol['p'], 193.75)
        print(get_solution_from_tab(tab))
        display_solution_from_tab(tab)
        print('number of computer boxes = {}'.format(sol[0]))
        print('number of printer boxes  = {}'.format(sol[2]))
        print('number of paint boxes    = {}'.format(0))
        print('profit = {}'.format(sol['p']))

problem2_1()
problem2_2()
problem2_3()

# Solutions to problem 2:

"""
Problem 2.1
{1: 1.5, 0: 4.0, 'p': 12.5}
x1      =       1.5
x0      =       4.0
p       =       12.5
"""

"""
Problem 2.2
{0: 8.0, 1: 4.0, 'p': 8.0}
x0      =       8.0
x1      =       4.0
p       =       8.0
"""

"""
Problem 2.3
{0: 125.0, 2: 25.0, 5: 125.0, 'p': 193.75}
x0      =       125.0
x2      =       25.0
x5      =       125.0
p       =       193.75
number of computer boxes = 125.0
number of printer boxes  = 25.0
number of paint boxes    = 0
profit = 193.75
"""