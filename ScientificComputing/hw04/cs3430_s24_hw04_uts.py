#############################################################
# module: cs3430_hw04_uts.py
# description: unit tests for CS 3430: S24: Assignment 04
# bugs to vladimir kulyukin in canvas.
##############################################################

import unittest
import numpy as np
from cs3430_s24_hw04 import simplex
from cs3430_s24_hw04 import get_solution_from_tab
from cs3430_s24_hw04 import display_solution_from_tab

class cs3430_s24_uts(unittest.TestCase):

    ### ================ Problem 1: Unit Tests =====================

    def test_hw04_prob01_ut01(self):
        print('\n***** CS3430: S24: HW04: Problem 01: Unit Test 01 ************')
        in_vars = {0:3, 1:4}
        m = np.array([[2,    2,   3, 1, 0, 160],
                      [5,    1,  10, 0, 1, 100],
                      [-10, -6,  -2, 0, 0, 0]],
                     dtype=float)
        tab = (in_vars, m)
        tab, solved = simplex(tab)
        assert solved is True
        sol = get_solution_from_tab(tab)
        assert np.allclose(sol[0], 5.0)
        assert np.allclose(sol[1], 75.0)
        assert np.allclose(sol['p'], 500.0)
        print(get_solution_from_tab(tab))
        display_solution_from_tab(tab)
        print('CS 3430: S24: HW04: Problem 01: Unit Test 01: pass')


    """
    My output of test_hw04_prob01_ut01(self):
    ***** CS3430: S24: HW04: Problem 01: Unit Test 01 ************
    in vars: {0: 3, 1: 4}
    mat:
    [[  2.   2.   3.   1.   0. 160.]
    [  5.   1.  10.   0.   1. 100.]
    [-10.  -6.  -2.   0.   0.   0.]]
    evc = 0
    dvr = 1
    pivoting dvr=1, evc=0
    in vars: {0: 3, 1: 0}
    mat:
    [[  0.    1.6  -1.    1.   -0.4 120. ]
    [  1.    0.2   2.    0.    0.2  20. ]
    [  0.   -4.   18.    0.    2.  200. ]]
    evc = 1
    dvr = 0
    pivoting dvr=0, evc=1
    in vars: {0: 1, 1: 0}
    mat:
    [[ 0.000e+00  1.000e+00 -6.250e-01  6.250e-01 -2.500e-01  7.500e+01]
    [ 1.000e+00  0.000e+00  2.125e+00 -1.250e-01  2.500e-01  5.000e+00]
    [ 0.000e+00  0.000e+00  1.550e+01  2.500e+00  1.000e+00  5.000e+02]]
    evc = -1
    {1: 75.0, 0: 5.0, 'p': 500.0}
    x1	=	75.0
    x0	=	5.0
    p	=	500.0
    CS 3430: S24: HW04: Problem 01: Unit Test 01: pass
    """

    def test_hw04_prob01_ut02(self):
        print('\n***** CS3430: S24: HW04: Problem 01: Unit Test 02 ************')
        in_vars = {0:3, 1:4, 2:5}
        m = np.array([[20,  4,  4, 1, 0, 0, 6000],
                      [8,   8,  4, 0, 1, 0, 10000],
                      [8,   4,  2, 0, 0, 1, 4000],
                      [-3, -8, -6, 0, 0, 0, 0]],
                     dtype=float)
        tab = (in_vars, m)
        tab, solved = simplex(tab)
        assert solved is True
        sol = get_solution_from_tab(tab)
        assert np.allclose(sol[1], 500.0)
        assert np.allclose(sol[2], 1000.0)
        assert np.allclose(sol[4], 2000.0)
        assert np.allclose(sol['p'], 10000.0)
        print('in_vars = {}'.format(in_vars))
        print('tab = {}'.format(tab[1]))
        print(get_solution_from_tab(tab))
        display_solution_from_tab(tab)
        print('CS 3430: S24: HW04: Problem 01: Unit Test 02: pass')

    """
    My output of test_hw04_prob01_ut02(self):
    ***** CS3430: S24: HW04: Problem 01: Unit Test 02 ************
    in vars: {0: 3, 1: 4, 2: 5}
    mat:
    [[ 2.e+01  4.e+00  4.e+00  1.e+00  0.e+00  0.e+00  6.e+03]
    [ 8.e+00  8.e+00  4.e+00  0.e+00  1.e+00  0.e+00  1.e+04]
    [ 8.e+00  4.e+00  2.e+00  0.e+00  0.e+00  1.e+00  4.e+03]
    [-3.e+00 -8.e+00 -6.e+00  0.e+00  0.e+00  0.e+00  0.e+00]]
    evc = 1
    dvr = 2
    pivoting dvr=2, evc=1
    in vars: {0: 3, 1: 4, 2: 1}
    mat:
    [[ 1.2e+01  0.0e+00  2.0e+00  1.0e+00  0.0e+00 -1.0e+00  2.0e+03]
    [-8.0e+00  0.0e+00  0.0e+00  0.0e+00  1.0e+00 -2.0e+00  2.0e+03]
    [ 2.0e+00  1.0e+00  5.0e-01  0.0e+00  0.0e+00  2.5e-01  1.0e+03]
    [ 1.3e+01  0.0e+00 -2.0e+00  0.0e+00  0.0e+00  2.0e+00  8.0e+03]]
    evc = 2
    dvr = 0
    pivoting dvr=0, evc=2
    in vars: {0: 2, 1: 4, 2: 1}
    mat:
    [[ 6.0e+00  0.0e+00  1.0e+00  5.0e-01  0.0e+00 -5.0e-01  1.0e+03]
    [-8.0e+00  0.0e+00  0.0e+00  0.0e+00  1.0e+00 -2.0e+00  2.0e+03]
    [-1.0e+00  1.0e+00  0.0e+00 -2.5e-01  0.0e+00  5.0e-01  5.0e+02]
    [ 2.5e+01  0.0e+00  0.0e+00  1.0e+00  0.0e+00  1.0e+00  1.0e+04]]
    evc = -1
    in_vars = {0: 2, 1: 4, 2: 1}
    tab = [[ 6.0e+00  0.0e+00  1.0e+00  5.0e-01  0.0e+00 -5.0e-01  1.0e+03]
    [-8.0e+00  0.0e+00  0.0e+00  0.0e+00  1.0e+00 -2.0e+00  2.0e+03]
    [-1.0e+00  1.0e+00  0.0e+00 -2.5e-01  0.0e+00  5.0e-01  5.0e+02]
    [ 2.5e+01  0.0e+00  0.0e+00  1.0e+00  0.0e+00  1.0e+00  1.0e+04]]
    {2: 1000.0, 4: 2000.0, 1: 500.0, 'p': 10000.0}
    x2	=	1000.0
    x4	=	2000.0
    x1	=	500.0
    p	=	10000.0
    CS 3430: S24: HW04: Problem 01: Unit Test 02: pass
    """

    def test_hw04_prob01_ut03(self):
        print('\n***** CS3430: S24: HW04: Problem 01: Unit Test 03 ************')
        in_vars = {0:3, 1:4}
        m = np.array([[1,  -1,  1, 1, 0, 5],
                      [2,   0, -1, 0, 1, 10],
                      [-1, -2, -1, 0, 0, 0]],
                     dtype=float)
        tab = (in_vars, m)        
        tab, solved = simplex(tab)        
        assert solved is False
        print(get_solution_from_tab(tab))
        display_solution_from_tab(tab)
        print('CS 3430: S24: HW04: Problem 01: Unit Test 03: pass')

    """
    My output of test_hw04_prob01_ut03(self):

    ***** CS3430: S24: HW04: Problem 01: Unit Test 03 ************
    in vars: {0: 3, 1: 4}
    mat:
    [[ 1. -1.  1.  1.  0.  5.]
    [ 2.  0. -1.  0.  1. 10.]
    [-1. -2. -1.  0.  0.  0.]]
    evc = 1
    dvr = -1
    {3: 5.0, 4: 10.0, 'p': 0.0}
    x3	=	5.0
    x4	=	10.0
    p	=	0.0
    CS 3430: S24: HW04: Problem 01: Unit Test 03: pass
    """

    def test_hw04_prob01_ut04(self):
        print('\n***** CS3430: S24: HW04: Problem 01: Unit Test 04 ************')
        in_vars = {0:2, 1:3}
        m = np.array([[ 4,  3,  1, 0, 480],
                      [ 3,  6,  0, 1, 720],
                      [-5, -4,  0, 0, 0]],
                     dtype=float)
        tab = (in_vars, m)
        tab, solved = simplex(tab)
        assert solved is True
        sol = get_solution_from_tab(tab)
        assert np.allclose(sol[0], 48.0)
        assert np.allclose(sol[1], 96.0)
        assert np.allclose(sol['p'], 624.0)
        display_solution_from_tab(tab)        
        print('\nCS3430: S24: HW04: Problem 01: Unit Test 04 pass')


    """
    ***** CS3430: S24: HW04: Problem 01: Unit Test 04 ************
    in vars: {0: 2, 1: 3}
    mat:
    [[  4.   3.   1.   0. 480.]
    [  3.   6.   0.   1. 720.]
    [ -5.  -4.   0.   0.   0.]]
    evc = 0
    dvr = 0
    pivoting dvr=0, evc=0
    in vars: {0: 0, 1: 3}
    mat:
    [[ 1.00e+00  7.50e-01  2.50e-01  0.00e+00  1.20e+02]
    [ 0.00e+00  3.75e+00 -7.50e-01  1.00e+00  3.60e+02]
    [ 0.00e+00 -2.50e-01  1.25e+00  0.00e+00  6.00e+02]]
    evc = 1
    dvr = 1
    pivoting dvr=1, evc=1
    in vars: {0: 0, 1: 1}
    mat:
    [[ 1.00000000e+00  0.00000000e+00  4.00000000e-01 -2.00000000e-01
    4.80000000e+01]
    [ 0.00000000e+00  1.00000000e+00 -2.00000000e-01  2.66666667e-01
    9.60000000e+01]
    [ 0.00000000e+00  0.00000000e+00  1.20000000e+00  6.66666667e-02
    6.24000000e+02]]
    evc = -1
    x0	=	48.0
    x1	=	96.0
    p	=	624.0
    
    CS3430: S24: HW04: Problem 01: Unit Test 04 pass
    """

    ### ================= Problem 2 UTs ===================================

    def test_hw04_prob_2_1_ut(self):
        print('\n***** CS3430: S24: HW04: Problem 2.1: Unit Test ************')
        in_vars = {0:2, 1:3}
        m = np.array([[3,   8, 1, 0, 24],
                      [6,   4, 0, 1, 30],
                      [-2, -3, 0, 0, 0]],
                     dtype=float)
        tab = (in_vars, m)
        tab, solved = simplex(tab)
        assert solved is True
        sol = get_solution_from_tab(tab)
        assert np.allclose(sol[0], 4.0)
        assert np.allclose(sol[1], 1.5)
        assert np.allclose(sol['p'], 12.5)
        print(get_solution_from_tab(tab))
        display_solution_from_tab(tab)
        print('\nCS3430: S24: HW04: Problem 2.1: Unit Test pass')

    """
    ***** CS3430: S24: HW04: Problem 2.1: Unit Test ************
    in vars: {0: 2, 1: 3}
    mat:
    [[ 3.  8.  1.  0. 24.]
    [ 6.  4.  0.  1. 30.]
    [-2. -3.  0.  0.  0.]]
    evc = 1
    dvr = 0
    pivoting dvr=0, evc=1
    in vars: {0: 1, 1: 3}
    mat:
    [[ 0.375  1.     0.125  0.     3.   ]
    [ 4.5    0.    -0.5    1.    18.   ]
    [-0.875  0.     0.375  0.     9.   ]]
    evc = 0
    dvr = 1
    pivoting dvr=1, evc=0
    in vars: {0: 1, 1: 0}
    mat:
    [[ 0.          1.          0.16666667 -0.08333333  1.5       ]
    [ 1.          0.         -0.11111111  0.22222222  4.        ]
    [ 0.          0.          0.27777778  0.19444444 12.5       ]]
    evc = -1
    {1: 1.5, 0: 4.0, 'p': 12.5}
    x1	=	1.5
    x0	=	4.0
    p	=	12.5
    
    CS3430: S24: HW04: Problem 2.1: Unit Test pass
    """

    def test_hw04_prob_2_2_ut(self):
        print('\n***** CS3430: S24: HW04: Problem 2.2: Unit Test ************')
        in_vars = {0:2, 1:3}
        m = np.array([[1,  -1, 1, 0, 4],
                      [-1,  3, 0, 1, 4],
                      [-1,  0, 0, 0, 0]],
                     dtype=float)
        tab = (in_vars, m)
        tab, solved = simplex(tab)
        assert solved is True
        err = 0.0001
        sol = get_solution_from_tab(tab)
        assert abs(sol[0] - 8.0) <= err
        assert abs(sol[1] - 4.0) <= err
        assert abs(sol['p'] - 8.0) <= err
        print('in_vars = {}'.format(in_vars))
        print('tab = {}'.format(tab[1]))
        print(get_solution_from_tab(tab))
        display_solution_from_tab(tab)
        print('\nCS3430: S24: HW04: Problem 2.2: Unit Test pass')

    """
    ***** CS3430: S24: HW04: Problem 2.2: Unit Test ************
    in vars: {0: 2, 1: 3}
    mat:
    [[ 1. -1.  1.  0.  4.]
    [-1.  3.  0.  1.  4.]
    [-1.  0.  0.  0.  0.]]
    evc = 0
    dvr = 0
    pivoting dvr=0, evc=0
    in vars: {0: 0, 1: 3}
    mat:
    [[ 1. -1.  1.  0.  4.]
    [ 0.  2.  1.  1.  8.]
    [ 0. -1.  1.  0.  4.]]
    evc = 1
    dvr = 1
    pivoting dvr=1, evc=1
    in vars: {0: 0, 1: 1}
    mat:
    [[1.  0.  1.5 0.5 8. ]
    [0.  1.  0.5 0.5 4. ]
    [0.  0.  1.5 0.5 8. ]]
    evc = -1
    in_vars = {0: 0, 1: 1}
    tab = [[1.  0.  1.5 0.5 8. ]
    [0.  1.  0.5 0.5 4. ]
    [0.  0.  1.5 0.5 8. ]]
    {0: 8.0, 1: 4.0, 'p': 8.0}
    x0	=	8.0
    x1	=	4.0
    p	=	8.0
    
    CS3430: S24: HW04: Problem 2.2: Unit Test pass
    """

    def test_hw04_prob_2_3_ut(self):
        print('\n***** CS3430: S24: HW04: Problem 2.3: Unit Test ************')
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
        print('\nCS3430: S24: HW04: Problem 2.3: Unit Test pass')

    """
    ***** CS3430: S24: HW04: Problem 2.3: Unit Test ************
    in vars: {0: 3, 1: 4, 2: 5}
    mat:
    [[ 1.2e+01  6.0e+00  0.0e+00  1.0e+00  0.0e+00  0.0e+00  1.5e+03]
    [ 1.8e+01  1.2e+01  1.0e+01  0.0e+00  1.0e+00  0.0e+00  2.5e+03]
    [ 1.5e+01  8.0e+00  0.0e+00  0.0e+00  0.0e+00  1.0e+00  2.0e+03]
    [-1.5e+00 -8.0e-01 -2.5e-01  0.0e+00  0.0e+00  0.0e+00  0.0e+00]]
    evc = 0
    dvr = 0
    pivoting dvr=0, evc=0
    in vars: {0: 0, 1: 4, 2: 5}
    mat:
    [[ 1.00000000e+00  5.00000000e-01  0.00000000e+00  8.33333333e-02
    0.00000000e+00  0.00000000e+00  1.25000000e+02]
    [ 0.00000000e+00  3.00000000e+00  1.00000000e+01 -1.50000000e+00
    1.00000000e+00  0.00000000e+00  2.50000000e+02]
    [ 0.00000000e+00  5.00000000e-01  0.00000000e+00 -1.25000000e+00
    0.00000000e+00  1.00000000e+00  1.25000000e+02]
    [ 0.00000000e+00 -5.00000000e-02 -2.50000000e-01  1.25000000e-01
    0.00000000e+00  0.00000000e+00  1.87500000e+02]]
    evc = 2
    dvr = 1
    pivoting dvr=1, evc=2
    in vars: {0: 0, 1: 2, 2: 5}
    mat:
    [[ 1.00000000e+00  5.00000000e-01  0.00000000e+00  8.33333333e-02
    0.00000000e+00  0.00000000e+00  1.25000000e+02]
    [ 0.00000000e+00  3.00000000e-01  1.00000000e+00 -1.50000000e-01
    1.00000000e-01  0.00000000e+00  2.50000000e+01]
    [ 0.00000000e+00  5.00000000e-01  0.00000000e+00 -1.25000000e+00
    0.00000000e+00  1.00000000e+00  1.25000000e+02]
    [ 0.00000000e+00  2.50000000e-02  0.00000000e+00  8.75000000e-02
    2.50000000e-02  0.00000000e+00  1.93750000e+02]]
    evc = -1
    {0: 125.0, 2: 25.0, 5: 125.0, 'p': 193.75}
    x0	=	125.0
    x2	=	25.0
    x5	=	125.0
    p	=	193.75
    number of computer boxes = 125.0
    number of printer boxes  = 25.0
    number of paint boxes    = 0
    profit = 193.75
    
    CS3430: S24: HW04: Problem 2.3: Unit Test pass
    """
    
    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
