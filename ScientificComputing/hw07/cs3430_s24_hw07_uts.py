#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: cs3430_s24_hw07_uts.py
# description: unit tests for CS 3430: S24: Assignment 07
# -----------------------------------------------------------
# bugs to vladimir kulyukin in canvas.
#############################################################

import unittest
import math
import numpy as np
from cdd import cdd
from rmb import rmb
import sympy as sp
from sympy import symbols
from sympy.utilities import lambdify
from rxp import rxp

class cs3430_s24_hw07_uts(unittest.TestCase):

    ### ================ Problem 1: Unit Tests =====================

    def test_hw07_example_6_2_cdd_pdf_ut01a(self):
        ### 0. define the approximate values (avs) of the 1st
        ###    derivatives of order 2 and 4 in CDD.pdf
        cdd_pdf_av_ord2 = -0.717344150
        cdd_pdf_av_ord4 = -0.717356108
        ## 1. define the sympy variables
        x = symbols('x')
        ## 2. define the sympy function
        sp_f = sp.cos(x)
        ## 3. compute the 1st derivative
        sp_drv1 = sp_f.diff()
        ## 4. lambdify the 1st derivative
        ldf_sp_drv1 = lambdify((x), sp_drv1)
        ## 5. get the true value of the 1st derivative
        ##    at x = 0.8.
        sp_tv = ldf_sp_drv1(0.8)
        ### 6. define the python function
        py_f = lambda x: math.cos(x)
        ## 7. compute approximate value av of order 2 at h=0.01
        av_ord2 = cdd.drv1_ord2(py_f, 0.8, 0.01)
        ## 8. compute approximate value av of order 2 at h=0.01
        av_ord4 = cdd.drv1_ord4(py_f, 0.8, 0.01)
        ## 9. make sure we are returning np.longdoubles
        assert isinstance(av_ord2, np.longdouble) and isinstance(av_ord4, np.longdouble)
        print('Sympy         TV = {}'.format(sp_tv))
        print('CDD.pdf Ord 2 AV = {}'.format(cdd_pdf_av_ord2))
        print('CDD.pdf Ord 4 AV = {}'.format(cdd_pdf_av_ord4))
        print('cdd.drv1_ord2 AV = {}'.format(av_ord2))
        print('cdd.drv1_ord4 AV = {}'.format(av_ord4))
        ## the magnitude of the error is small.        
        assert abs(av_ord2 - sp_tv) < 1.0e-3
        assert abs(av_ord4 - sp_tv) < 1.0e-5

    def test_hw07_example_6_2_cdd_pdf_ut01b(self):
        ## 1. define the sympy variables
        x = symbols('x')
        ## 2. define the sympy function
        sp_f = sp.cos(x)
        ## 3. compute the 1st derivative
        sp_drv1 = sp_f.diff()
        ## 4. lambdify the 1st derivative
        ldf_sp_drv1 = lambdify((x), sp_drv1)
        ## 5. get the true value of the 1st derivative
        ##    at x = 0.8.
        sp_tv = ldf_sp_drv1(0.8)
        ### 6. define the python function
        py_f = lambda x: math.cos(x)
        ## 7. compute approximate value av of order 2 at h=0.01
        h = 0.01
        for k in range(5):
            ## 8. compute approximate values av of orders 2 and 4 at h
            hv = h/(2**k)
            av_ord2 = cdd.drv1_ord2(py_f, 0.8, hv)
            av_ord4 = cdd.drv1_ord4(py_f, 0.8, hv)
            ## 9. make sure we are returning np.longdoubles
            assert isinstance(av_ord2, np.longdouble) and isinstance(av_ord4, np.longdouble)
            print('Sympy         TV = {}'.format(sp_tv))
            print('cdd.drv1_ord2 AV = {} at h = {}'.format(av_ord2, hv))
            print('cdd.drv1_ord4 AV = {} at h = {}'.format(av_ord4, hv))
        ## the magnitude of the error is small.            
        assert abs(av_ord2 - sp_tv) < 1.0e-5
        assert abs(av_ord4 - sp_tv) < 1.0e-7

    def test_hw07_example_6_4_cdd_pdf_ut01a(self):
        ### This is example 6.4, p. 340 in CDD.pdf.
        ### We define the value of their approximation given in that example.
        cdd_pdf_av_ord2 = -0.696690000
        ## 1. define the sympy variables
        x = symbols('x')
        ## 2. define the sympy function
        sp_f = sp.cos(x)
        ## 3. compute the 1st and 2nd derivatives
        sp_drv1 = sp_f.diff()
        sp_drv2 = sp_drv1.diff()
        ## 4. lambdify the 2nd derivative
        ldf_sp_drv2 = lambdify((x), sp_drv2)
        ## 5. get the true value of the 2nd derivative
        ##    at x = 0.8.
        sp_tv = ldf_sp_drv2(0.8)
        ### 6. define the python function
        py_f = lambda x: math.cos(x)
        ## 7. compute approximate value av of order 2 at h=0.01
        av_ord2 = cdd.drv2_ord2(py_f, 0.8, 0.01)
        ## 8. compute approximate value av of order 2 at h=0.01
        av_ord4 = cdd.drv2_ord4(py_f, 0.8, 0.01)
        ## 9. make sure we are returning np.longdoubles
        assert isinstance(av_ord2, np.longdouble) and isinstance(av_ord4, np.longdouble)
        print('Sympy         TV = {}'.format(sp_tv))
        print('CDD.pdf Ord 2 AV = {}'.format(cdd_pdf_av_ord2))
        print('cdd.drv2_ord2 AV = {}'.format(av_ord2))
        print('cdd.drv2_ord4 AV = {}'.format(av_ord4))
        ## the magnitude of the error is small.
        assert abs(sp_tv - av_ord2) < 1.0e-5
        assert abs(sp_tv - av_ord4) < 1.0e-7

    def test_hw07_example_6_4_cdd_pdf_ut01b(self):
        ### This is example 6.4, p. 340 in CDD.pdf.
        ## 1. define the sympy variables
        x = symbols('x')
        ## 2. define the sympy function
        sp_f = sp.cos(x)
        ## 3. compute the 1st and 2nd derivatives
        sp_drv1 = sp_f.diff()
        sp_drv2 = sp_drv1.diff()
        ## 4. lambdify the 2nd derivative
        ldf_sp_drv2 = lambdify((x), sp_drv2)
        ## 5. get the true value of the 2nd derivative
        ##    at x = 0.8.
        sp_tv = ldf_sp_drv2(0.8)
        ### 6. define the python function
        py_f = lambda x: math.cos(x)
        h = 0.01
        for k in range(5):
            hv = h/(2**k)
            ## 7. compute approximate value av of order 2 at hv
            av_ord2 = cdd.drv2_ord2(py_f, 0.8, hv)
            ## 8. compute approximate value av of order 2 at hv
            av_ord4 = cdd.drv2_ord4(py_f, 0.8, hv)
            ## 9. make sure we are returning np.longdoubles
            assert isinstance(av_ord2, np.longdouble) and isinstance(av_ord4, np.longdouble)
            print('Sympy         TV = {}'.format(sp_tv))
            print('cdd.drv2_ord2 AV = {} at h = {}'.format(av_ord2, hv))
            print('cdd.drv2_ord4 AV = {} at h = {}'.format(av_ord4, hv))
        ## the magnitude of the error is small.
        assert abs(sp_tv - av_ord2) < 1.0e-5
        assert abs(sp_tv - av_ord4) < 1.0e-7

    def test_hw07_example_6_2_cdd_pdf_ut01c(self):
        ## 1. define the sympy variables
        x = symbols('x')
        ## 2. define the sympy function
        sp_f = sp.cos(x)
        ## 3. compute the 1st derivative
        sp_drv1 = sp_f.diff()
        ## 4. lambdify the 1st derivative
        ldf_sp_drv1 = lambdify((x), sp_drv1)
        ## 5. get the true value of the 1st derivative
        ##    at x = 0.8.
        sp_tv = ldf_sp_drv1(0.8)
        ### 6. define the python function
        py_f = lambda x: math.cos(x)
        ## 7. compute approximate value av of order 2 at h=0.01
        h = 0.01
        av_n_ord2 = cdd.drv1_ord2(py_f, 0.8, h)
        av_n_ord4 = cdd.drv1_ord4(py_f, 0.8, h)
        for k in range(1,5):
            ## 8. compute approximate values av of orders 2 and 4 at h
            hv = h/(2**k)
            av_2n_ord2 = cdd.drv1_ord2(py_f, 0.8, hv)
            av_2n_ord4 = cdd.drv1_ord4(py_f, 0.8, hv)
            re_ord2 = rxp.r2(av_2n_ord2, av_n_ord2)
            re_ord4 = rxp.r2(av_2n_ord4, av_n_ord4)
            print('Sympy         TV = {}'.format(sp_tv))
            print('RE ORD 2 AV = {} at h = {}'.format(re_ord2, hv))
            print('RE ORD 4 AV = {} at h = {}'.format(re_ord4, hv))
            av_n_ord2 = av_2n_ord2
            av_n_ord4 = av_2n_ord4
        ## the magnitude of the error is small.            
        assert abs(re_ord2 - sp_tv) < 1.0e-12
        assert abs(re_ord4 - sp_tv) < 1.0e-12

    # ### This unit test uses AV_h = f(x+h)-f(x-h)/(2h) on
    # ### Slides 13--15 in Lecture 12 PDF.
    # ### This is the output in Python 3.6.7 on Bionic Beaver (Ubuntu 18.04 LTS).            
    # ### h = 0.1;	 AV_h = 153.8724011957411;	 Et = -1.5912266869476923
    # ### h = 0.05;	 AV_h = 152.67804999953697;	 Et = -0.3968754907435539
    # ### h = 0.025;	 AV_h = 152.38033526380121;	 Et = -0.09916075500780153
    # ### h = 0.0125;	 AV_h = 152.3059610664572;	 Et = -0.02478655766378779
    # ### h = 0.00625;	 AV_h = 152.28737092128597;	 Et = -0.006196412492556647
    def test_hw07_prob01_slide_15_lect_12a(self):    
        f = lambda x: 5.0*math.exp(2.5*x)
        x = symbols('x')
        sympy_f = 5.0*sp.exp(2.5*x)
        ## derivative of f
        df = sympy_f.diff()
        ldf = lambdify((x), df)
        tv = ldf(1.0)
        ## 1. compute approximate value AV; this is AV at h,
        ## h is half the step side, which means that the
        ## size of the interval over which we do the central
        ## divided difference is 2*h.
        h  = 0.1
        for i in range(5):
            ## cdd.drv1_ord2() computes the formula on Slide 07
            av = cdd.drv1_ord2(f, 1.0, h/(2**i))
            ## make sure you return np.longdouble for max precision
            assert isinstance(av, np.longdouble)
            ## compare av and tv at specified error level
            print('h = {};\t AV_h = {};\t Et = {}'.format(h/(2**i), av, tv-av))
        assert abs(tv-av) < 0.01

    # ### This unit test uses AV_h = f(x+h)-f(x-h)/(2h) on
    # ### Slides 13--15 in Lecture 12 PDF.
    # ### This is the output in Python 3.6.7 on Bionic Beaver (Ubuntu 18.04 LTS).            
    # ### h = 0.1;	 AV_h = 153.8724011957411;	 Et = -1.5912266869476923
    # ### h = 0.05;	 AV_h = 152.67804999953697;	 Et = -0.3968754907435539
    # ### h = 0.025;	 AV_h = 152.38033526380121;	 Et = -0.09916075500780153
    # ### h = 0.0125;	 AV_h = 152.3059610664572;	 Et = -0.02478655766378779
    # ### h = 0.00625;	 AV_h = 152.28737092128597;	 Et = -0.006196412492556647
    def test_hw07_prob01_slide_15_lect_12b(self):    
        py_f = lambda x: 5.0*math.exp(2.5*x)
        x = symbols('x')
        sympy_f = 5.0*sp.exp(2.5*x)
        ## derivative of f
        df = sympy_f.diff()
        ldf = lambdify((x), df)
        sp_tv = ldf(1.0)
        ## 1. compute approximate value AV; this is AV at h,
        ## h is half the step side, which means that the
        ## size of the interval over which we do the central
        ## divided difference is 2*h.
        h  = 0.01
        av_n_ord2 = cdd.drv1_ord2(py_f, 1.0, h)
        av_n_ord4 = cdd.drv1_ord4(py_f, 1.0, h)
        for k in range(5):
            hv = h/(2**k)
            av_2n_ord2 = cdd.drv1_ord2(py_f, 1.0, hv)
            av_2n_ord4 = cdd.drv1_ord4(py_f, 1.0, hv)
            re_ord2 = rxp.r2(av_2n_ord2, av_n_ord2)
            re_ord4 = rxp.r2(av_2n_ord4, av_n_ord4)
            print('Sympy         TV = {}'.format(sp_tv))
            print('RE ORD 2 AV = {} at h = {}'.format(re_ord2, hv))
            print('RE ORD 4 AV = {} at h = {}'.format(re_ord4, hv))
            av_n_ord2 = av_2n_ord2
            av_n_ord4 = av_2n_ord4
        assert abs(re_ord2 - sp_tv) < 1.0e-10
        assert abs(re_ord4 - sp_tv) < 1.0e-7

    ### =============== Problem 02 =========================

    ### This unit test is Example 1 in the Lecture 14 PDF.
    ### It tests the first five rows in Slide 11 in Lecture 14.
    ### AV_n in this case is comptued with the T Rule for
    ### an appropriate number of segments n into which we
    ### partition [a,b]. Remember that n = 2^(k-1).
    def test_hw07_prob02_slide_11_lect_14(self):
        f = lambda x: 5.0*x*math.exp(-2.0*x)
        a, b = 0.1, 1.3
        T_1_1 = rmb.T_k_1(f, a, b, 1)
        print('\nT_1_1 = {}'.format(T_1_1))
        assert np.allclose(T_1_1, np.longdouble((b - a)/2*(f(a) + f(b))))
        T_2_1 = rmb.T_k_1(f, a, b, 2)
        print('T_2_1 = {}'.format(T_2_1))        
        sum_2_1 = sum(f(a+i*(b-a)/2) for i in range(1, 2))
        assert np.allclose(T_2_1, np.longdouble((b - a)/(2*2)*(f(a) + 2*sum_2_1 + f(b))))
        T_3_1 = rmb.T_k_1(f, a, b, 3)
        print('T_3_1 = {}'.format(T_2_1))
        sum_3_1 = sum(f(a+i*(b-a)/4) for i in range(1, 4))
        assert np.allclose(T_3_1, np.longdouble((b - a)/(2*4)*(f(a) + 2*sum_3_1 + f(b))))
        T_4_1 = rmb.T_k_1(f, a, b, 4)
        print('T_4_1 = {}'.format(T_4_1))
        sum_4_1 = sum(f(a+i*(b-a)/8) for i in range(1, 8))
        assert np.allclose(T_4_1, np.longdouble((b-a)/(2*8)*(f(a) + 2*sum_4_1 + f(b))))
        T_5_1 = rmb.T_k_1(f, a, b, 5)
        print('T_5_1 = {}'.format(T_5_1))        
        sum_5_1 = sum(f(a+i*(b-a)/16) for i in range(1, 16))
        assert np.allclose(T_5_1, np.longdouble((b-a)/(2*16)*(f(a) + 2*sum_5_1 + f(b))))

    def test_hw07_prob02_slide_14_lect_14(self):
        ### sympy's value (cf. Slides 7,8 in Lecture 14
        sp_int_val = 0.8938650276524703
        f = lambda x: 5.0*x*math.exp(-2.0*x)
        a, b = 0.1, 1.3
        av_n = rmb.T_k_1(f, a, b, 1)
        n = 1
        for k in range(2, 10):
            av_2n = rmb.T_k_1(f, a, b, k)
            re = rxp.r2(av_2n, av_n)
            av_n = av_2n
            print('Sympy TV = {}'.format(sp_int_val))
            print('RE    AV = {} at n = {}'.format(re, n))
            n = 2**(k-1)
        assert abs(sp_int_val-re) < 1.0e-9

    ##This is example 2 in Lecture 14.
    def test_hw07_slide_18_lecture_14(self):
        sp_int_val = 11061.335535081103 ## cf. Slide 17, Lecture 14
        f = lambda t: 2000*math.log(140000/(140000 - 2100*t), math.e) - 9.8*t
        a, b = 8, 30
        av_n = rmb.T_k_1(f, a, b, 1)
        n = 1
        print('k=1, n=1, AV_n = {}'.format(av_n))
        for k in range(2, 10):
            av_2n = rmb.T_k_1(f, a, b, k)
            print('k={}, n={}, AV_n = {}'.format(k, 2**(k-1), av_2n))
            re = rxp.r2(av_2n, av_n)
            av_n = av_2n
            n = 2**(k-1)
            print('RE_{}_{} = {}'.format(2**(k-2), n, re))
        assert abs(sp_int_val-re) < 1.0e-7

    def test_hw07_prob02_ut01(self):
        def f(x):
            return math.e**(-(x**2.0))
        for j in range(1, 10):
            assert np.allclose(rmb.R_j_1(f, 0, 1, j), rmb.T_k_1(f, 0, 1, j))

    def test_hw07_prob02_ut02(self):
        def f(x):
            return math.e**(-(x**2.0))
        tv  = 0.7471804289095104
        av  = rmb.R_j_l(f, 0, 1, 2, 2)
        err = 1.0e-5
        assert abs(av-tv) < err

    def test_hw07_prob02_ut03(self):
        def f(x):
            return math.e**(-(x**2.0))
        tv  = 0.7468337098497524
        av  = rmb.R_j_l(f, 0, 1, 3, 3) 
        err = 1.0e-5
        assert abs(av-tv) < err

    def test_hw07_prob02_ut04(self):
        def f(x):
            return math.e**(-(x**2.0))
        err = 1.0e-5
        tv  = 0.7468241328124273
        ## Approximating integral of f(x) on [a=0, b=1] with R[10,10].
        av  = rmb.R_j_l(f, 0, 1, 10, 10)
        assert abs(tv - av) < err
    
    def test_hw07_prob02_ut05(self):
        def f(t):
            return 2000*math.log(140000.0/(140000.0 - 2100*t), math.e) - 9.8*t
        err = 1.e-5
        tv  = 11061.335535081103 ## this is sympy's value (cf. Slide 17, Lecture 14)
        ## Approximating integral of f(x) on [a=8, b=30].
        for j in range(1, 101):
            av  = rmb.R_j_l(f, 8, 30, j, j)
            if abs(tv - av) < err:
                print('R[{},{}] = {}'.format(j, j, av))
                break
        
    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
