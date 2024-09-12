#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: cs3430_s24_hw01_uts.py
# description: unit tests for CS 3430: S24: Assignment 01
# bugs to vladimir kulyukin in canvas
##############################################################

import unittest
import numpy as np
import numpy.linalg
from cs3430_s24_hw01 import cs3430_s24_hw_01_prob_1_1, cs3430_s24_hw_01_prob_1_2
from cs3430_s24_hw01 import cs3430_s24_hw_01_prob_1_3, cs3430_s24_hw_01_prob_1_4
from cs3430_s24_hw01 import leibnitz_det
from cs3430_s24_hw01 import cramers_rule

class cs3430_s24_hw01_uts(unittest.TestCase):

    ### ================ Problem 1: Unit Tests =====================
    
    def test_hw01_prob_1_1(self):
        print('\nCS 3430: S24: HW01: Problem 1.1: Unit Test...')
        try:
            A, x, b = cs3430_s24_hw_01_prob_1_1()
            assert np.allclose(np.dot(A, x), b)
        except Exception as e:
            print(e)
            assert 1 == 0
        print('CS 3430: S24: HW01: Problem 1.1: Unit Test: pass')

    def test_hw01_prob_1_2(self):
        print('\nCS 3430: S24: HW01: Problem 1.2: Unit Test...')
        try:
            A, x, b = cs3430_s24_hw_01_prob_1_2()
            assert np.allclose(np.dot(A, x), b)
        except Exception as e:
            print(e)
            assert 1 == 0
        print('CS 3430: S24: HW01: Problem 1.2: Unit Test: pass')

    def test_hw01_prob_1_3(self):
        print('\nCS 3430: S24: HW01: Problem 1.3: Unit Test...')
        try:
            A, x, b = cs3430_s24_hw_01_prob_1_3()
            assert np.allclose(np.dot(A, x), b)
        except Exception as e:
            print(e)
            assert 1 == 0
        print('CS 3430: S24: HW01: Problem 1.3: Unit Test: pass')

    def test_hw01_prob_1_4(self):
        print('\nCS 3430: S24: HW01: Problem 1.4: Unit Test...')
        try:
            A, x, b = cs3430_s24_hw_01_prob_1_4()
            assert np.allclose(np.dot(A, x), b)
        except Exception as e:
            print(e)
            assert 1 == 0
        print('CS 3430: S24: HW01: Problem 1.4: Unit Test: pass')

    ### ================ Problem 2: Unit Tests =====================

    def test_cs3430_s24_hw01_prob_2_ut_01(self):
        print('\nCS 3430: S24: HW01: Problem 2: Unit Test 01...')
        A = np.array([[2, 1, 3],
                      [4, 1, 2],
                      [1, 2, -3]],
                     dtype=float)
        assert np.allclose(leibnitz_det(A), np.linalg.det(A))
        print('CS 3430: S24: HW01: Problem 2: Unit Test 01: pass')

    def test_cs3430_s24_hw01_prob_2_ut_02(self):
        print('\nCS 3430: S24: HW01: Problem 2: Unit Test 02...')
        A = np.array([[2., 1., 0., 1.],
                      [3., 2., 1., 2.],
                      [4., 0., 1., 4.],
                      [1., 0., 2., 1.]])
        assert np.allclose(leibnitz_det(A), np.linalg.det(A))
        print('CS 3430: S24: HW01: Problem 2: Unit Test 02: pass')

    def test_cs3430_s24_hw01_prob_2_ut_03(self):
        print('\nCS 3430: S24: HW01: Problem 2: Unit Test 03...')
        A = np.array([[ 5., -2.,  4., -1.],
                      [ 0.,  1.,  5.,  2.],
                      [ 1.,  2.,  0.,  1.],
                      [-3.,  1., -1.,  1.]])
        assert np.allclose(leibnitz_det(A), np.linalg.det(A))
        print('CS 3430: S24: HW01: Problem 2: Unit Test 03: pass')

    def test_cs3430_s24_hw01_prob_2_ut_04(self):
        print('\nCS 3430: S24: HW01: Problem 2: Unit Test 04...')
        A = np.array([[ 3.,  2.,  0.,  1.,  3.],
                      [-2.,  4.,  1.,  2.,  1.],
                      [ 0., -1.,  0.,  1., -5.],
                      [-1.,  2.,  0., -1.,  2.],
                      [ 0.,  0.,  0.,  0.,  2.]])
        assert np.allclose(leibnitz_det(A), np.linalg.det(A))
        print('CS 3430: S24: HW01: Problem 2: Unit Test 04: pass')

    # def test_cs3430_s24_hw01_prob_2_ut_05(self):
    #     print('\nCS 3430: S24: HW01: Problem 2: Unit Test 05...')
    #     A = np.array([[446., 163.,  59., 129., 393., 483., 271.,  27., 384.,  58.],
    #                   [258., 116., 272., 401., 332., 216., 158., 211., 361., 236.],
    #                   [ 68., 498., 471.,  81., 178., 167., 166., 399., 484., 422.],
    #                   [338.,  38., 274., 476.,  99., 370., 322., 459., 151., 163.],
    #                   [380., 106., 421., 314., 425., 332.,  10., 135., 448., 407.],
    #                   [456., 270., 317., 268.,   3., 394., 250., 354., 135., 310.],
    #                   [330., 452., 456., 137., 457.,  37., 421.,   5., 357., 165.],
    #                   [294., 457., 147.,   1., 278., 474., 368., 138., 222., 122.],
    #                   [231.,   1., 184., 318., 315., 433., 434.,  76.,  71.,  34.],
    #                   [129., 307., 479., 350., 103., 485., 243., 160., 245., 407.]])
    #     assert np.allclose(leibnitz_det(A), np.linalg.det(A))
    #     print('CS 3430: S24: HW01: Problem 2: Unit Test 05: pass')

    ### ================ Problem 3: Unit Tests =====================

    def test_cs3430_s24_hw01_prob_3_ut01(self):
        print('\nCS3430: S24: HW01: Problem 03: Unit Test 01...')
        A = np.array([[0, 1, -3],
                      [2, 3, -1],
                      [4, 5, -2]],
                     dtype=float)
        b = np.array([[-5],
                      [7],
                      [10]], dtype=float)
        x  = cramers_rule(A, b)
        assert np.allclose(np.dot(A, x), b)
        print('CS 3430: S22: HW01: Problem 03: Unit Test 01: pass')


    def test_hw01_prob03_ut02(self):
        print('\nCS3430: S24: HW01: Problem 03: Unit Test 02...')
        A = np.array(
            [[2, -1, 3],
             [3,  0, 2],
             [-2, 1, 4]],
            dtype=float)
        b = np.array([[4],
                      [5],
                      [6]],
                     dtype=float)
        x  = cramers_rule(A, b)
        assert np.allclose(np.dot(A, x), b)
        print('CS 3430: S24: HW01: Problem 03: Unit Test 02: pass')

    def test_hw01_prob03_ut03(self):
        print('\nCS3430: S24: HW01: Problem 03: Unit Test 03...')
        A = np.array([[ 73., 136., 173., 112.],
                      [ 61., 165., 146.,  14.],
                      [137.,  43., 183.,  73.],
                      [196.,  40., 144.,  31.]])
        b = np.array([[3],
                      [1],
                      [10],
                      [1]],
                     dtype=float)
        x  = cramers_rule(A, b)
        assert np.allclose(np.dot(A, x), b)
        print('CS 3430: S24: HW01: Problem 03: Unit Test 03: pass')


    def test_hw01_prob03_ut04(self):
        print('\nCS3430: S24: HW01: Problem 03: Unit Test 04...')
        A = np.array([[162., 118., 111., 133.],
                      [ 64.,  37.,  33., 165.],
                      [ 38.,   4., 107.,  86.],
                      [ 98.,  35.,  67., 107.]])
        b = np.array([[10],
                      [15],
                      [200],
                      [140]],
                     dtype=float)
        x = cramers_rule(A, b)
        assert np.allclose(np.dot(A, x), b)
        print('CS 3430: S24: HW01: Problem 03: Unit Test 04: pass')

    # def test_hw01_prob03_ut05(self):
    #     print('\nCS3430: S24: HW01: Problem 03: Unit Test 05...')
    #     A = np.array([[446., 163.,  59., 129., 393., 483., 271.,  27., 384.,  58.],
    #                   [258., 116., 272., 401., 332., 216., 158., 211., 361., 236.],
    #                   [ 68., 498., 471.,  81., 178., 167., 166., 399., 484., 422.],
    #                   [338.,  38., 274., 476.,  99., 370., 322., 459., 151., 163.],
    #                   [380., 106., 421., 314., 425., 332.,  10., 135., 448., 407.],
    #                   [456., 270., 317., 268.,   3., 394., 250., 354., 135., 310.],
    #                   [330., 452., 456., 137., 457.,  37., 421.,   5., 357., 165.],
    #                   [294., 457., 147.,   1., 278., 474., 368., 138., 222., 122.],
    #                   [231.,   1., 184., 318., 315., 433., 434.,  76.,  71.,  34.],
    #                   [129., 307., 479., 350., 103., 485., 243., 160., 245., 407.]],
    #                  dtype=float)
    #     b = np.array([[1],
    #                   [2],
    #                   [3],
    #                   [4],
    #                   [5],
    #                   [6],
    #                   [7],
    #                   [8],
    #                   [9],
    #                   [10]],
    #                  dtype=float)
    #     x  = cramers_rule(A, b)
    #     assert np.allclose(np.dot(A, x), b)
    #     print('CS 3430: S24: HW01: Problem 03: Unit Test 05: pass')
        
    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
