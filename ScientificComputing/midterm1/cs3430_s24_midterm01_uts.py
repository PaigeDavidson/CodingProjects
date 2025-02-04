#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: cs3430_s24_midterm01_uts.py
# descriptions: unit tests for midterm 01.
# bugs to vladimir kulyukin via canvas
##############################################################

import unittest
import numpy as np
import numpy.linalg
import pickle

from cs3430_s24_midterm01 import solve_lin_sys_with_gje
from cs3430_s24_midterm01 import solve_lin_sys_with_cramer
from cs3430_s24_midterm01 import solve_lin_sys_with_bsubst
from cs3430_s24_midterm01 import solve_lin_sys_with_fsubst
from cs3430_s24_midterm01 import solve_lin_sys_with_lud
from cs3430_s24_midterm01 import farming_land_allocation
### These are used in the last unit test
from cs3430_s24_hw04 import get_solution_from_tab
from cs3430_s24_hw04 import display_solution_from_tab


class cs3430_s24_midterm01_uts(unittest.TestCase):

    ### ===================== Problem 01 =======================================

    def test_midterm01_prob_01_ut01(self):
        print('\n***** CS3430: S24: Midterm01: Problem 01: Unit Test 01 ************')
        A = np.array([[1, 1, -3],
                      [2, 3, -1],
                      [4, 5, -2]],
                     dtype=float)
        b = np.array([[-5],
                      [7],
                      [10]], dtype=float)
        x  = solve_lin_sys_with_gje(A, b)
        bb = np.dot(A, x)
        assert np.allclose(bb, b)
        print('CS 3430: S24: Midterm01: Problem 01: Unit Test 01 pass')

    def test_midterm01_prob_01_ut02(self):
        print('\n***** CS3430: S24: Midterm01: Problem 01: Unit Test 02 ************')
        A = np.array([[1, 1, -3, 10],
                      [2, 3, -1, 11],
                      [4, 5, -2, 12],
                      [34, 52, -21, 121]],
                     dtype=float)
        b = np.array([[-7],
                      [9],
                      [12],
                      [24]], dtype=float)
        x  = solve_lin_sys_with_gje(A, b)
        bb = np.dot(A, x)
        assert np.allclose(bb, b)
        print('CS 3430: S24: Midterm01: Problem 01: Unit Test 02 pass')

    def test_midterm01_prob_01_ut03(self):
        print('\n***** CS3430: S24: Midterm01: Problem 01: Unit Test 03 ************')
        A = np.array([[1, 1, -3, 10, -11],
                      [2, 3, -1, 11, 201],
                      [4, 5, -2, 12, 301],
                      [34, 52, -21, 121, 44],
                      [134, 152, -121, 25, 254],                      
        ],
                     dtype=float)
        b = np.array([[-7],
                      [9],
                      [12],
                      [24],
                      [300]
        ], dtype=float)
        x  = solve_lin_sys_with_gje(A, b)
        bb = np.dot(A, x)
        assert np.allclose(bb, b)
        print('CS 3430: S24: Midterm01: Problem 01: Unit Test 03 pass')

    def test_midterm01_prob_01_ut04(self):
        print('\n***** CS3430: S24: Midterm01: Problem 01: Unit Test 04 ************')
        A = np.array([[446., 163.,  59., 129., 393., 483., 271.,  27., 384.,  58.],
                      [258., 116., 272., 401., 332., 216., 158., 211., 361., 236.],
                      [ 68., 498., 471.,  81., 178., 167., 166., 399., 484., 422.],
                      [338.,  38., 274., 476.,  99., 370., 322., 459., 151., 163.],
                      [380., 106., 421., 314., 425., 332.,  10., 135., 448., 407.],
                      [456., 270., 317., 268.,   3., 394., 250., 354., 135., 310.],
                      [330., 452., 456., 137., 457.,  37., 421.,   5., 357., 165.],
                      [294., 457., 147.,   1., 278., 474., 368., 138., 222., 122.],
                      [231.,   1., 184., 318., 315., 433., 434.,  76.,  71.,  34.],
                      [128., 306., 478., 349., 102., 484., 242., 159., 244., 408.]],
                     dtype=float)
        b = np.array(
            [[338.],
             [485.],
             [ 45.],
             [358.],
             [390.],
             [460.],
             [362.],
             [282.],
             [50.],
             [139.]],
            dtype=float)
        x  = solve_lin_sys_with_gje(A, b)
        bb = np.dot(A, x)
        assert np.allclose(bb, b)
        print('CS 3430: S24: Midterm01: Problem 01: Unit Test 04 pass')

    def test_midterm01_prob_01_ut05(self):
        print('\n***** CS3430: S24: Midterm01: Problem 01: Unit Test 05 ************')        
        A = np.array([[ 73., 136., 173., 112.],
                      [ 61., 165., 146.,  14.],
                      [137.,  43., 183.,  73.],
                      [196.,  40., 144.,  31.]])
        b = np.array([[1.0],
                      [-2.0],
                      [3.0],
                      [4.0]])
        x  = solve_lin_sys_with_gje(A, b)
        bb = np.dot(A, x)
        assert np.allclose(bb, b)
        print('CS 3430: S24: Midterm01: Problem 01: Unit Test 05 pass')

    ### ===================== Problem 02 =======================================

    def test_midterm01_prob_02_ut01(self):
        print('\n***** CS3430: S24: Midterm01: Problem 02: Unit Test 01 ************')
        A = np.array([[0, 1, -3],
                      [2, 3, -1],
                      [4, 5, -2]],
                     dtype=float)
        b = np.array([[-5],
                      [7],
                      [10]], dtype=float)
        x  = solve_lin_sys_with_cramer(A, b)
        bb = np.dot(A, x)
        assert np.allclose(bb, b)
        print('CS 3430: S24: Midterm01: Problem 02: Unit Test 01 pass')

    def test_midterm01_prob_02_ut02(self):
        print('\n***** CS3430: S24: Midterm01: Problem 02: Unit Test 02 ************')
        A = np.array([[0, 1, -3, 10],
                      [2, 3, -1, 11],
                      [4, 5, -2, 12],
                      [34, 52, -21, 121]],
                     dtype=float)
        b = np.array([[-7],
                      [9],
                      [12],
                      [24]], dtype=float)
        x  = solve_lin_sys_with_cramer(A, b)        
        bb = np.dot(A, x)
        assert np.allclose(bb, b)
        print('CS 3430: S24: Midterm01: Problem 03: Unit Test 02 pass')

    def test_midterm01_prob_02_ut03(self):
        print('\n***** CS3430: S24: Midterm01: Problem 02: Unit Test 03 ************')
        A = np.array([[0, 1, -3, 10, -11],
                      [2, 3, -1, 11, 201],
                      [4, 5, -2, 12, 301],
                      [34, 52, -21, 121, 44],
                      [134, 152, -121, 25, 254],                      
        ],
                     dtype=float)
        b = np.array([[-7],
                      [9],
                      [12],
                      [24],
                      [300]
        ], dtype=float)
        x  = solve_lin_sys_with_cramer(A, b)        
        bb = np.dot(A, x)
        assert np.allclose(bb, b)        
        print('CS 3430: S24: Midterm01: Problem 02: Unit Test 03 pass')

    def test_midterm01_prob_02_ut04(self):
        print('\n***** CS3430: S24: Midterm01: Problem 02: Unit Test 04 ************')
        A = np.array([[446., 163.,  59., 129., 393.],
                      [258., 116., 272., 401., 332.],
                      [ 68., 498., 471.,  81., 178.],
                      [338.,  38., 274., 476.,  99.],
                      [380., 106., 421., 314., 425.]],
                     dtype=float)
        b = np.array(
            [[338.],
             [485.],
             [ 45.],
             [358.],
             [390.]],
            dtype=float)
        x  = solve_lin_sys_with_cramer(A, b)                
        bb = np.dot(A, x)
        assert np.allclose(bb, b)        
        print('CS 3430: S24: Midterm01: Problem 02: Unit Test 04 pass')

    def test_midterm01_prob_02_ut05(self):
        print('\n***** CS3430: S24: Midterm01: Problem 02: Unit Test 05 ************')        
        A = np.array([[ 73., 136., 173., 112.],
                      [ 61., 165., 146.,  14.],
                      [137.,  43., 183.,  73.],
                      [196.,  40., 144.,  31.]])
        b = np.array([[1.0],
                      [-2.0],
                      [3.0],
                      [4.0]])
        x  = solve_lin_sys_with_cramer(A, b)                        
        bb = np.dot(A, x)
        assert np.allclose(bb, b)                
        print('CS 3430: S24: Midterm01: Problem 02: Unit Test 05 pass')

    # ### ============== Problem 03 ============================
    
    def test_midterm01_prob_03_ut01(self):
        print('\n***** CS3430: S24: Midterm01: Problem 03: Unit Test 01 ************')
        a = np.array([[2, 3, -1],
                      [0, 2, 6],
                      [0, 0, -15]],
                     dtype=float)
        b = np.array([[-4, 5],
                      [10, 11],
                      [-30, 28]],
                     dtype=float)
        
        x = solve_lin_sys_with_bsubst(a, 3, b, 2)
        b0 = np.dot(a, x[:,0])
        assert np.allclose(b[:,0], b0)
        b1 = np.dot(a, x[:,1])
        assert np.allclose(b[:,1], b1)
        print('\n CS3430: S24: Midterm01: Problem 03: Unit Test 01 pass')

    def test_midterm01_prob_03_ut02(self):
        print('\n***** CS3430: S24: Midterm01: Problem 03: Unit Test 02 ************')
        a = np.array([[1, 3, -1],
                      [0, 2,  6],
                      [0, 0, -15]],
                 dtype=float)
        b = np.array([[-4],
                      [10],
                      [-30]],
                     dtype=float)
        x = solve_lin_sys_with_bsubst(a, 3, b, 1)
        b0 = np.dot(a, x[:,0])
        assert np.allclose(b[:,0], b0)
        print('\n CS3430: S24: Midterm01: Problem 03: Unit Test 02 pass')

    ### ============== Problem 04 ============================

    def test_midterm01_prob_04_ut01(self):
        print('\n***** CS3430: S24: Midterm01: Problem 04: Unit Test 01 ************')
        a = np.array([[1, 0, 0],
                      [2, 1, 0],
                      [-1, 3, 1]],
                     dtype=float)
        b = np.array([[-4],
                      [2],
                      [4]],
                     dtype=float)
        x = solve_lin_sys_with_fsubst(a, 3, b, 1)
        b0 = np.dot(a, x[:,0])
        assert np.allclose(b[:,0], b0)
        print('\nCS3430: S24: Midterm01: Problem 04: Unit Test 01 pass')

    def test_midterm01_prob_04_ut02(self):
        print('\n***** CS3430: S24: Midterm01: Problem 04: Unit Test 02 ************')
        a = np.array([[2, 0, 0],
                      [2, 3, 0],
                      [-1, 3, 4]],
                     dtype=float)
        b = np.array([[-4],
                      [2],
                      [4]],
                     dtype=float)
        x = solve_lin_sys_with_fsubst(a, 3, b, 1)
        b0 = np.dot(a, x[:,0])
        assert np.allclose(b[:,0], b0)
        print('\nCS3430: S24: Midterm01: Problem 04: Unit Test 02 pass')        


    def test_midterm01_prob_04_ut04(self):
        print('\n***** CS3430: S24: Midterm01: Problem 04: Unit Test 04 ************')
        a = np.array([[12, 0, 0],
                      [2, 21, 0],
                      [-1, 3, 16]],
                     dtype=float)
        b = np.array([[-4, 10],
                      [ 2, 12],
                      [ 4, 21]],
                     dtype=float)
        x = solve_lin_sys_with_fsubst(a, 3, b, 2)
        b0 = np.dot(a, x[:,0])
        assert np.allclose(b[:,0], b0)
        b1 = np.dot(a, x[:,1])
        assert np.allclose(b[:,1], b1)        
        print('\nCS 3430: S24: Midterm01: Problem 04: Unit Test 04 pass')

    ### ============== Problem 05 ============================

    def test_midterm01_prob_05_ut01(self):
        print('\n***** CS3430: S24: Midterm01: Problem 05: Unit Test 01 ************')
        A = np.array([[ 73., 136., 173., 112.],
                      [ 61., 165., 146.,  14.],
                      [137.,  43., 183.,  73.],
                      [196.,  40., 144.,  31.]])
        b = np.array([[4.0],
                      [-1.0],
                      [3.0],
                      [5.0]])        
        x = solve_lin_sys_with_lud(A, 4, b, 1)
        assert np.allclose(np.dot(A, x), b)
        print('CS 3430: S24: Midterm01: Problem 05: Unit Test 01 pass')

    def test_midterm01_prob_05_ut02(self):
        print('\n***** CS3430: S24: Midterm01: Problem 05: Unit Test 02 ************')
        A = np.array([[ 83., 136., 173., 110.],
                      [ 71., 165., 146.,  12.],
                      [148.,  43., 183.,  71.],
                      [276.,  40., 144.,  29.]])
        b = np.array([[4.0, 10.0],
                      [-1.0, 11.0],
                      [3.0, 12.5],
                      [5.0, 78.5]])        
        x = solve_lin_sys_with_lud(A, 4, b, 2)
        assert np.allclose(np.dot(A, x[:,0]), b[:,0])
        assert np.allclose(np.dot(A, x[:,1]), b[:,1])
        print('CS 3430: S24: Midterm01: Problem 05: Unit Test 02 pass')

    def test_midterm01_prob_05_ut03(self):
        print('\n***** CS3430: S24: Midterm01: Problem 05: Unit Test 03 ************')
        A = np.array([[ 83., 136., 173., 110.],
                      [ 71., 165., 146.,  12.],
                      [148.,  43., 183.,  71.],
                      [276.,  40., 144.,  29.]])
        b = np.array([[4.0, 10.0, 275.25],
                      [-1.0, 11.0, 30.5],
                      [3.0, 12.5, 245.789],
                      [5.0, 78.5, -111.0]])        
        x = solve_lin_sys_with_lud(A, 4, b, 3)
        for c in range(3):
            assert np.allclose(np.dot(A, x[:,c]), b[:,c])
        print('CS 3430: S24: Midterm01: Problem 05: Unit Test 03 pass')

    def test_midterm01_prob_05_ut04(self):
        print('\n***** CS3430: S24: Midterm01: Problem 05: Unit Test 04 ************')
        A = np.array([[ 83., 136., 173., 110.],
                      [ 71., 165., 146.,  12.],
                      [148.,  43., 183.,  71.],
                      [276.,  40., 144.,  29.]])
        b = np.array([[4.0, 10.0, 275.25, 22.0],
                      [-1.0, 11.0, 30.5,  42.0],
                      [3.0, 12.5, 245.789, 44.0],
                      [5.0, 78.5, -111.0, 556.2]])        
        x = solve_lin_sys_with_lud(A, 4, b, 4)
        for c in range(4):
            assert np.allclose(np.dot(A, x[:,c]), b[:,c])
        print('CS 3430: S24: Midterm01: Problem 05: Unit Test 04 pass')

    def test_midterm01_prob_05_ut05(self):
        print('\n***** CS3430: S24: Midterm01: Problem 05: Unit Test 05 ************')
        A = np.array([[ 83., 136., 173., 110.],
                      [ 71., 165., 146.,  12.],
                      [148.,  43., 183.,  71.],
                      [276.,  40., 144.,  29.]])
        b = np.array([[4.0, 10.0, 275.25, 22.0, -22.0],
                      [-1.0, 11.0, 30.5,  42.0, -42.0],
                      [3.0, 12.5, 245.789, 44.0, -44.0],
                      [5.0, 78.5, -111.0, 556.2, -556.2]])        
        x = solve_lin_sys_with_lud(A, 4, b, 5)
        for c in range(5):
            assert np.allclose(np.dot(A, x[:,c]), b[:,c])
        print('CS 3430: S24: Midterm01: Problem 05: Unit Test 05 pass')

    ### ============== Problem 06 ============================
    ### No UTs for this problem

    ### ============== Problem 07 ============================
    ### No UTs for this problem

    ### ============== Problem 08 ============================
    ### No UTs for this problem

    ### ============== Problem 09 ============================
    ### No UTs for this problem

    ### ============== Problem 10 ============================

    def test_midterm01_land_allocation_ut(self):
        print('\n***** CS3430: S24: Midterm01: Land Allocation: Unit Test 01 ************')
        sol = farming_land_allocation()
        ## display the following values from your solution sol.
        ## I entered default negative values. They are not accurate.
        print('number of acres for crop A = {}'.format(0))
        print('number of acres for crop B = {}'.format(0))
        print('number of acres for crop C = {}'.format(sol[2]))
        print('p:  maximum profit = {}'.format(sol['p']))
        print('\n* CS3430: S24: Midterm01: Land Allocation: Unit Test 01 passed')
    
    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
