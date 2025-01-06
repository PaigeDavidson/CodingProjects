#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: cs3430_s24_miterm02_uts.py
# description: unit tests for CS 3430: S24: Midterm 02
# -----------------------------------------------------------
# bugs to vladimir kulyukin on canvas
#############################################################

import unittest
import numpy as np
from cs3430_s24_midterm02 import diff_file
from cs3430_s24_midterm02 import zero_root
from cs3430_s24_midterm02 import detect_pil_edge_pixels
from cs3430_s24_midterm02 import cdd_drv1_ord2
from cs3430_s24_midterm02 import cdd_drv1_ord4
from cs3430_s24_midterm02 import cdd_drv2_ord2
from cs3430_s24_midterm02 import cdd_drv2_ord4
from cs3430_s24_midterm02 import romberg_integral
from cs3430_s24_midterm02 import richardson_2
from cs3430_s24_midterm02 import e_cont_frac_rat
from cs3430_s24_midterm02 import e_cont_frac_real
from cs3430_s24_midterm02 import pi_cont_frac_rat
from cs3430_s24_midterm02 import pi_cont_frac_real
from cs3430_s24_midterm02 import chudnovsky_pi
import sympy
import sympy.utilities
import math
import decimal

class cs3430_s24_midterm02_uts(unittest.TestCase):

    ### ================ Problem 01 =====================

    def test_prob01_ut01(self):
        x = sympy.symbols('x')
        pf0  = 10*x**2 + 3*x**1 + 9
        dpf0 = pf0.diff()
        fdpf0 = sympy.utilities.lambdify((x), dpf0)
        pf1   = 5*x**2 + -2*x + 8
        dpf1  = pf1.diff()
        fdpf1 = sympy.utilities.lambdify((x), dpf1)
        pf2   = 2*x**3 + -2*x**2 + 3*x + 4
        dpf2  = pf2.diff()
        fdpf2 = sympy.utilities.lambdify((x), dpf2)
        
        diffs = diff_file('polys_01.txt')
        for x in range(10):
            assert np.allclose(diffs[0](x), fdpf0(x))
        for x in range(10):
            assert np.allclose(diffs[1](x), fdpf1(x))
        for x in range(10):
            assert np.allclose(diffs[2](x), fdpf2(x))

    def test_prob01_ut02(self):
        x = sympy.symbols('x')
        pf0  = 14*x**3 + 10*x**2 - 2*x - 7
        dpf0 = pf0.diff()
        fdpf0 = sympy.utilities.lambdify((x), dpf0)
        pf1   = 11*x**5 + 4*x**3 - 7*x - 3
        dpf1  = pf1.diff()
        fdpf1 = sympy.utilities.lambdify((x), dpf1)
        pf2   = 14*x**7 + 10*x**4 + 5*x**3  + 11*x**2 + 5*x - 20
        dpf2  = pf2.diff()
        fdpf2 = sympy.utilities.lambdify((x), dpf2)
        
        diffs = diff_file('polys_02.txt')
        for x in range(10):
            assert np.allclose(diffs[0](x), fdpf0(x))
        for x in range(10):
            assert np.allclose(diffs[1](x), fdpf1(x))
        for x in range(10):
            assert np.allclose(diffs[2](x), fdpf2(x))

    def test_prob01_ut03(self):
        x = sympy.symbols('x')
        pf0  = 13*x**4 + 10*x**3 - 7*x**2 + 8*x - 9
        dpf0 = pf0.diff()
        fdpf0 = sympy.utilities.lambdify((x), dpf0)
        pf1   = 21*x**3 - 152*x**2 + 18*x - 25
        dpf1  = pf1.diff()
        fdpf1 = sympy.utilities.lambdify((x), dpf1)
        pf2   = 2*x**6 + 2*x**5 + 2*x**4 + 2*x**3 + 2*x**2 + 2*x + 2
        dpf2  = pf2.diff()
        fdpf2 = sympy.utilities.lambdify((x), dpf2)
        pf3   = x**8 - 2*x**7 + 3*x**6 - 4*x**5 + 5*x**4 - 6*x**3 + 7*x**2 - 8*x + 9
        dpf3  = pf3.diff()
        fdpf3 = sympy.utilities.lambdify((x), dpf3)
        
        diffs = diff_file('polys_03.txt')
        for x in range(10):
            assert np.allclose(diffs[0](x), fdpf0(x))
        for x in range(10):
            assert np.allclose(diffs[1](x), fdpf1(x))
        for x in range(10):
            assert np.allclose(diffs[2](x), fdpf2(x))
        for x in range(10):
            assert np.allclose(diffs[3](x), fdpf3(x))

    ### ================ Problem 02 =====================

    def test_prob02_ut01(self):
        poly_text = '10x^2 + 3x^1 - 9x^0'
        x = sympy.symbols('x')
        pf  = 10*x**2 + 3*x - 9
        fpf = sympy.utilities.lambdify((x), pf)        
        zr = zero_root(poly_text, num_iters=5)
        assert np.allclose(fpf(zr), 0)

    def test_prob02_ut02(self):
        poly_text = '120x^7 + -3x^4 + -15x^3 + 41x^2 + 7x^1 + 10x^0'
        x = sympy.symbols('x')
        pf  = 120*x**7 - 3*x**4 - 15*x**3 + 41*x**2 + 7*x + 10
        fpf = sympy.utilities.lambdify((x), pf)        
        zr = zero_root(poly_text, num_iters=30)
        assert np.allclose(fpf(zr), 0)

    def test_prob02_ut03(self):
        poly_text = '1x^3 - 17x^0'
        x = sympy.symbols('x')
        pf  = x**3 - 17
        fpf = sympy.utilities.lambdify((x), pf)        
        zr = zero_root(poly_text, num_iters=30)
        assert np.allclose(fpf(zr), 0)

    def test_prob02_ut04(self):
        poly_text = '1x^5 - 171x^0'
        x = sympy.symbols('x')
        pf  = x**5 - 171
        fpf = sympy.utilities.lambdify((x), pf)        
        zr = zero_root(poly_text, num_iters=30)
        assert np.allclose(fpf(zr), 0)

    def test_prob02_ut05(self):
        poly_text = '1x^7 - 13x^0'
        x = sympy.symbols('x')
        pf  = x**7 - 13
        fpf = sympy.utilities.lambdify((x), pf)        
        zr = zero_root(poly_text, num_iters=30)
        assert np.allclose(fpf(zr), 0)

    ### ================ Problem 03 =====================

    def test_prob03_ut01(self):
        detect_pil_edge_pixels('imgs/ornament_01.jpg', 'out_imgs/ornament_01.jpg',
                               default_delta=1.0, magn_thresh=70)

    def test_prob03_ut02(self):
        detect_pil_edge_pixels('imgs/ornament_02.jpg', 'out_imgs/ornament_02.jpg',
                               default_delta=1.0, magn_thresh=70)

    def test_prob03_ut03(self):
        detect_pil_edge_pixels('imgs/ornament_03.jpg', 'out_imgs/ornament_03.jpg',
                               default_delta=1.0, magn_thresh=70)

    def test_prob03_ut04(self):
        detect_pil_edge_pixels('imgs/ornament_04.jpg', 'out_imgs/ornament_04.jpg',
                               default_delta=1.0, magn_thresh=70)

    def test_prob03_ut05(self):
        detect_pil_edge_pixels('imgs/night.jpg', 'out_imgs/night.jpg',
                               default_delta=1.0, magn_thresh=50)

    ### =============== Problems 04 and 05 ===============================

    def test_prob04_05_ut01(self):
        x = sympy.symbols('x') # define the sympy variables
        sp_f = sympy.cos(x) # define the sympy function
        sp_drv1 = sp_f.diff() # compute the 1st derivative
        ldf_sp_drv1 = sympy.utilities.lambdify((x), sp_drv1) ## lambdify the 1st derivative
        sp_tv = ldf_sp_drv1(0.8) # get sympy value of 1st deriv at x = 0.8
        py_f = lambda x: math.cos(x) # define the python function
        ## compute approximate value av of order 2 at h=0.01
        h = 0.01
        for k in range(5):
            ## compute approximate values av of orders 2 and 4 at h
            hv = h/(2**k)
            av_ord2 = cdd_drv1_ord2(py_f, 0.8, hv)
            av_ord4 = cdd_drv1_ord4(py_f, 0.8, hv)
            ## make sure we are returning np.longdoubles
            assert isinstance(av_ord2, np.longdouble) and isinstance(av_ord4, np.longdouble)
            print('Sympy         TV = {}'.format(sp_tv))
            print('cdd.drv1_ord2 AV = {} at h = {}'.format(av_ord2, hv))
            print('cdd.drv1_ord4 AV = {} at h = {}'.format(av_ord4, hv))
        ## the magnitude of the error is small.            
        assert abs(av_ord2 - sp_tv) < 1.0e-5
        assert abs(av_ord4 - sp_tv) < 1.0e-7

    def test_prob04_05_ut02(self):
        ### define the value of their approximation given in that example.
        cdd_pdf_av_ord2 = -0.696690000
        x = sympy.symbols('x') ## define the sympy variables
        sp_f = sympy.cos(x) ## define the sympy function
        sp_drv1 = sp_f.diff() ## compute the 1st and 2nd derivatives
        sp_drv2 = sp_drv1.diff()
        ldf_sp_drv2 = sympy.utilities.lambdify((x), sp_drv2) ## lambdify the 2nd derivative
        sp_tv = ldf_sp_drv2(0.8) ## get the true value of the 2nd derivative at x = 0.8.
        py_f = lambda x: math.cos(x) ## define the python function
        av_ord2 = cdd_drv2_ord2(py_f, 0.8, 0.01) ## compute approximate value av of order 2 at h=0.01
        av_ord4 = cdd_drv2_ord4(py_f, 0.8, 0.01) ## compute approximate value av of order 4 at h=0.01
        ## make sure we are returning np.longdoubles
        assert isinstance(av_ord2, np.longdouble) and isinstance(av_ord4, np.longdouble)
        print('Sympy         TV = {}'.format(sp_tv))
        print('CDD.pdf Ord 2 AV = {}'.format(cdd_pdf_av_ord2))
        print('cdd.drv2_ord2 AV = {}'.format(av_ord2))
        print('cdd.drv2_ord4 AV = {}'.format(av_ord4))
        ## the magnitude of the error is small.
        assert abs(sp_tv - av_ord2) < 1.0e-5
        assert abs(sp_tv - av_ord4) < 1.0e-7

    ### =============== Problems 06 - 07 ===============================

    ### cf. Slides 7,8 in Lecture 14.
    def test_prob06_07_ut01(self):
        sp_int_val = 0.8938650276524703
        f = lambda x: 5.0*x*math.exp(-2.0*x)
        a, b = 0.1, 1.3
        av_n = romberg_integral(f, a, b, 1, 1)
        n = 1
        for k in range(2, 10):
            av_2n = romberg_integral(f, a, b, k, 1)
            re = richardson_2(av_2n, av_n)
            av_n = av_2n
            print('Sympy TV = {}'.format(sp_int_val))
            print('RE    AV = {} at n = {}'.format(re, n))
            n = 2**(k-1)
        assert abs(sp_int_val-re) < 1.0e-9

    ### cf. Slides 7,8 in Lecture 14.        
    def test_prob06_07_ut02(self):
        sp_int_val = 0.8938650276524703
        f = lambda x: 5.0*x*math.exp(-2.0*x)
        a, b = 0.1, 1.3
        av_n = romberg_integral(f, a, b, 1, 1)
        n = 1
        for k in range(2, 10):
            av_2n = romberg_integral(f, a, b, k, 1)
            re = richardson_2(av_2n, av_n)
            av_n = av_2n
            print('Sympy TV = {}'.format(sp_int_val))
            print('RE    AV = {} at n = {}'.format(re, n))
            n = 2**(k-1)
        assert abs(sp_int_val-re) < 1.0e-9

    ### This is example 2 in Lecture 14.
    def test_prob06_07_ut03(self):
        sp_int_val = 11061.335535081103 ## cf. Slide 17, Lecture 14
        f = lambda t: 2000*math.log(140000/(140000 - 2100*t), math.e) - 9.8*t
        a, b = 8, 30
        av_n = romberg_integral(f, a, b, 1, 1)
        n = 1
        print('k=1, n=1, AV_n = {}'.format(av_n))
        for k in range(2, 10):
            av_2n = romberg_integral(f, a, b, k, 1)
            print('k={}, n={}, AV_n = {}'.format(k, 2**(k-1), av_2n))
            re = richardson_2(av_2n, av_n)
            av_n = av_2n
            n = 2**(k-1)
            print('RE_{}_{} = {}'.format(2**(k-2), n, re))
        assert abs(sp_int_val-re) < 1.0e-7

    def test_prob06_07_ut04(self):
        def f(x):
            return math.e**(-(x**2.0))
        tv  = 0.7471804289095104
        av  = romberg_integral(f, 0, 1, 2, 2)
        err = 1.0e-5
        assert abs(av-tv) < err

    def test_prob06_07_ut05(self):
        def f(x):
            return math.e**(-(x**2.0))
        tv  = 0.7468337098497524
        av  = romberg_integral(f, 0, 1, 3, 3) 
        err = 1.0e-5
        assert abs(av-tv) < err

    def test_prob06_07_ut06(self):
        def f(x):
            return math.e**(-(x**2.0))
        err = 1.0e-5
        tv  = 0.7468241328124273
        ## Approximating integral of f(x) on [a=0, b=1] with R[10,10].
        av  = romberg_integral(f, 0, 1, 10, 10)
        assert abs(tv - av) < err
    
    def test_prob06_prob07_ut07(self):
        def f(t):
            return 2000*math.log(140000.0/(140000.0 - 2100*t), math.e) - 9.8*t
        err = 1.e-5
        tv  = 11061.335535081103 ## this is sympy's value (cf. Slide 17, Lecture 14)
        ## Approximating integral of f(x) on [a=8, b=30].
        for j in range(1, 101):
            av  = romberg_integral(f, 8, 30, j, j)
            if abs(tv - av) < err:
                print('R[{},{}] = {}'.format(j, j, av))
                break
        assert abs(tv - av) < err

    def test_prob06_prob07_ut08(self):
        def f(x):
            assert -1 <= x <= 1
            return math.sqrt(1 - x**2)
        err = 1.e-5
        tv  = math.pi/2
        for j in range(1, 101):
            av  = romberg_integral(f, -1, 1, j, j)
            if abs(tv - av) < err:
                print('R[{},{}] = {}'.format(j, j, av))
                break
        assert abs(tv - av) < err

    ### =============== Problems 08 ===============================

    def test_prob08_ut01(self, prec=86):
        # 2/1
        e_rat_0 = e_cont_frac_rat(0)
        assert e_rat_0.get_n() == 2
        assert e_rat_0.get_d() == 1

        # 3/1
        e_rat_1 = e_cont_frac_rat(1)
        assert e_rat_1.get_n() == 3
        assert e_rat_1.get_d() == 1

        # 8/3
        e_rat_2 = e_cont_frac_rat(2)
        assert e_rat_2.get_n() == 8
        assert e_rat_2.get_d() == 3

        # 11/4
        e_rat_3 = e_cont_frac_rat(3)
        assert e_rat_3.get_n() == 11
        assert e_rat_3.get_d() == 4

        # 19/7
        e_rat_4 = e_cont_frac_rat(4)
        assert e_rat_4.get_n() == 19
        assert e_rat_4.get_d() == 7

        # 87/32
        e_rat_5 = e_cont_frac_rat(5)
        assert e_rat_5.get_n() == 87
        assert e_rat_5.get_d() == 32

        # 106/39        
        e_rat_6 = e_cont_frac_rat(6)
        assert e_rat_6.get_n() == 106
        assert e_rat_6.get_d() == 39

        # 193/71
        e_rat_7 = e_cont_frac_rat(7)
        assert e_rat_7.get_n() == 193
        assert e_rat_7.get_d() == 71

        # 1264/465
        e_rat_8 = e_cont_frac_rat(8)
        assert e_rat_8.get_n() == 1264
        assert e_rat_8.get_d() == 465

        # 1457/536
        e_rat_9 = e_cont_frac_rat(9)
        assert e_rat_9.get_n() == 1457
        assert e_rat_9.get_d() == 536

    def test_prob08_ut02(self):
        decimal.getcontext().prec = 20
        math_e = decimal.Decimal(math.e)
        ecf = e_cont_frac_real(100, prec=20)
        assert abs(math_e - ecf) < 1.0e-5

    ### ================ Problem 09 =================================
    
    def test_prob09_ut_01(self):
        ## 0th pi rat captured
        pi_rat_0 = pi_cont_frac_rat(0)
        assert pi_rat_0.get_n() == 3
        assert pi_rat_0.get_d() == 1
        
        ## 1st pi rat captured
        pi_rat_1 = pi_cont_frac_rat(1)
        assert pi_rat_1.get_n() == 19
        assert pi_rat_1.get_d() == 6

        ## 2nd pi rat captured
        pi_rat_2 = pi_cont_frac_rat(2)
        assert pi_rat_2.get_n() == 47
        assert pi_rat_2.get_d() == 15

        ## 3rd pi rat captured
        pi_rat_3 = pi_cont_frac_rat(3)
        assert pi_rat_3.get_n() == 1321
        assert pi_rat_3.get_d() == 420

        ## 4th pi rat captured
        pi_rat_4 = pi_cont_frac_rat(4)
        assert pi_rat_4.get_n() == 989
        assert pi_rat_4.get_d() == 315

    ### In test_picf_ut_02(), these are the results
    ### I got on my laptop:
    ### num_iters = 100, pi = 3.1415929035585527643
    ### STR_PI    =           3.1415926535897932384
    ### num_iters = 200, pi = 3.1415926848388167504
    ### num_iters = 300, pi = 3.1415926628489239013
    ### num_iters = 500, pi = 3.1415926555897832386
    ### math.pi             = 3.141592653589793
    def test_prob09_ut_02(self):
        pi_cf = pi_cont_frac_real(500, prec=20)
        math_pi = decimal.Decimal(math.pi)
        assert abs(math_pi - pi_cf) < 1.0e-7

    ### ================= Problem 10 =============================
    ## this unit test is from hw08
    ## when I ran it on [1,30] at prec=86, I got the first 85 digits
    ## of the mantissa correctly. You should pass this test at err < 1.0e-5
    def test_prob10_ut_01(self):
        PI_1_30 = chudnovsky_pi(30,prec=86)
        decimal.getcontext().prec=30
        assert abs(decimal.Decimal(math.pi) - PI_1_30) < 1.0e-5
 
    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
