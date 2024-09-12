#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: cs3430_s24_hw04_uts.py
# description: unit tests for CS 3430: S24: Assignment 05
# bugs to vladimir kulyukin on canvas
##############################################################

import unittest
import numpy as np
from const import const
from var   import var
from pwr   import pwr
from prod  import prod
from plus  import plus
from maker import maker
from poly_parser import poly_parser
from dra         import dra
from lambdifier  import lambdifier
from tiny_de     import tiny_de
import sympy
import sympy.utilities
from nra import nra
import math

class cs3430_s22_hw05_uts(unittest.TestCase):

    ### ================ General Parser Tests =====================
    ### These unit tests show you how the parser works.

    def test_parser_ut01(self):
        s1 = '5x^10'
        e1 = poly_parser.parse_elt(s1)
        assert str(e1) == '(5.0*(x^10.0))'
        assert isinstance(e1, prod)
        assert isinstance(e1.get_mult1(), const)
        assert np.allclose(e1.get_mult1().get_val(), 5.0)
        assert isinstance(e1.get_mult2(), pwr)
        assert isinstance(e1.get_mult2().get_base(), var)
        assert e1.get_mult2().get_base().get_name() == 'x'
        assert isinstance(e1.get_mult2().get_deg(), const)
        assert np.allclose(e1.get_mult2().get_deg().get_val(), 10.0)

    def test_parser_ut02(self):
        s1 = '10.13x^-13.7'
        e1 = poly_parser.parse_elt(s1)
        assert str(e1) == '(10.13*(x^-13.7))'
        assert isinstance(e1, prod)
        assert isinstance(e1.get_mult1(), const)
        assert np.allclose(e1.get_mult1().get_val(), 10.13)
        assert isinstance(e1.get_mult2(), pwr)
        assert isinstance(e1.get_mult2().get_base(), var)
        assert e1.get_mult2().get_base().get_name() == 'x'
        assert isinstance(e1.get_mult2().get_deg(), const)
        assert np.allclose(e1.get_mult2().get_deg().get_val(), -13.7)

    def test_parser_ut03(self):
        s1 = '-10.13x^-13.7'
        e1 = poly_parser.parse_elt(s1)
        assert str(e1) == '(-10.13*(x^-13.7))'
        assert isinstance(e1, prod)
        assert isinstance(e1.get_mult1(), const)
        assert np.allclose(e1.get_mult1().get_val(), -10.13)
        assert isinstance(e1.get_mult2(), pwr)
        assert isinstance(e1.get_mult2().get_base(), var)
        assert e1.get_mult2().get_base().get_name() == 'x'
        assert isinstance(e1.get_mult2().get_deg(), const)
        assert np.allclose(e1.get_mult2().get_deg().get_val(), -13.7)

    def test_parser_ut04(self):
        s1 = '5x^2 + 10x^13'
        plus1 = poly_parser.parse_sum(s1)
        assert str(plus1) == '((5.0*(x^2.0))+(10.0*(x^13.0)))'
        assert isinstance(plus1, plus)
        elt1 = plus1.get_elt1()
        elt2 = plus1.get_elt2()
        assert isinstance(elt1, prod)
        assert isinstance(elt2, prod)
        assert isinstance(elt1.get_mult1(), const)
        assert isinstance(elt1.get_mult2(), pwr)
        assert isinstance(elt2.get_mult1(), const)
        assert isinstance(elt2.get_mult2(), pwr)
        assert elt1.get_mult2().get_base().get_name() == 'x'
        assert elt2.get_mult2().get_base().get_name() == 'x'
        assert np.allclose(elt1.get_mult1().get_val(), 5.0)
        assert np.allclose(elt2.get_mult1().get_val(), 10.0)
        assert np.allclose(elt1.get_mult2().get_deg().get_val(), 2.0)
        assert np.allclose(elt2.get_mult2().get_deg().get_val(), 13.0)

    def test_parser_ut05(self):
        s1 = '-5.11x^-2.3 + -10x^13'
        plus1 = poly_parser.parse_sum(s1)
        print(plus1)
        assert str(plus1) == '((-5.11*(x^-2.3))+(-10.0*(x^13.0)))'
        assert isinstance(plus1, plus)
        elt1 = plus1.get_elt1()
        elt2 = plus1.get_elt2()
        assert isinstance(elt1, prod)
        assert isinstance(elt2, prod)
        assert isinstance(elt1.get_mult1(), const)
        assert isinstance(elt1.get_mult2(), pwr)
        assert isinstance(elt2.get_mult1(), const)
        assert isinstance(elt2.get_mult2(), pwr)
        assert elt1.get_mult2().get_base().get_name() == 'x'
        assert elt2.get_mult2().get_base().get_name() == 'x'
        assert np.allclose(elt1.get_mult1().get_val(), -5.11)
        assert np.allclose(elt2.get_mult1().get_val(), -10.0)
        assert np.allclose(elt1.get_mult2().get_deg().get_val(), -2.3)
        assert np.allclose(elt2.get_mult2().get_deg().get_val(), 13.0)

    def test_parser_ut06(self):
        s1 = '5x^2 + 7x^1 + 11x^0'
        plus1 = poly_parser.parse_sum(s1)
        print(plus1)
        assert str(plus1) == '(((5.0*(x^2.0))+(7.0*(x^1.0)))+(11.0*(x^0.0)))'
        assert isinstance(plus1, plus)
        elt1 = plus1.get_elt1()
        elt2 = plus1.get_elt2()
        assert isinstance(elt1, plus)
        assert isinstance(elt2, prod)
        e1_elt1 = elt1.get_elt1()
        e1_elt2 = elt1.get_elt2()
        assert isinstance(e1_elt1, prod)
        assert isinstance(e1_elt2, prod)
        assert isinstance(e1_elt1.get_mult1(), const)
        assert isinstance(e1_elt1.get_mult2(), pwr)
        assert isinstance(e1_elt2.get_mult1(), const)
        assert isinstance(e1_elt2.get_mult2(), pwr)
        assert e1_elt1.get_mult2().get_base().get_name() == 'x'
        assert e1_elt2.get_mult2().get_base().get_name() == 'x'
        assert np.allclose(e1_elt1.get_mult1().get_val(), 5.0)
        assert np.allclose(e1_elt2.get_mult1().get_val(), 7.0)
        assert np.allclose(e1_elt1.get_mult2().get_deg().get_val(), 2.0)
        assert np.allclose(e1_elt2.get_mult2().get_deg().get_val(), 1.0)
        assert isinstance(elt2.get_mult1(), const)
        assert isinstance(elt2.get_mult2(), pwr)
        assert elt2.get_mult2().get_base().get_name() == 'x'        
        assert np.allclose(elt2.get_mult1().get_val(), 11.0)
        assert np.allclose(elt2.get_mult2().get_deg().get_val(), 0.0)

    def test_parser_ut07(self):
        s1 = '15x^3 + 7x^2 + -11x^1 + 13x^0'
        plus1 = poly_parser.parse_sum(s1)
        print(plus1)
        assert str(plus1) == '((((15.0*(x^3.0))+(7.0*(x^2.0)))+(-11.0*(x^1.0)))+(13.0*(x^0.0)))'
        assert isinstance(plus1, plus)
        elt1 = plus1.get_elt1()
        elt2 = plus1.get_elt2()
        assert isinstance(elt1, plus)
        assert isinstance(elt2, prod)
        e1_elt1 = elt1.get_elt1()
        e1_elt2 = elt1.get_elt2()
        assert isinstance(e1_elt1, plus)
        assert isinstance(e1_elt2, prod)

    ### Here's an example of how to use tiny_de class to parse a file.
    def test_parser_ut08(self):
        tde = tiny_de()
        poly_ds_lst = tde.parse_file('polys.txt')
        for i, pds in enumerate(poly_ds_lst):
            if i == 0:
                assert str(pds) == '(5.0*(x^2.0))'
            elif i == 1:
                assert str(pds) == '((3.0*(x^2.0))+(10.0*(x^1.0)))'
            elif i == 2:
                assert str(pds) == '((((10.0*(x^3.0))+(3.0*(x^2.0)))+(-2.0*(x^1.0)))+(-10.0*(x^0.0)))'
            elif i == 3:
                assert str(pds) == '((((((-14.13*(x^5.0))+(10.1*(x^4.0)))+(7.0*(x^3.0)))+(11.11*(x^2.0)))+(5.0*(x^1.0)))+(-12.0*(x^0.0)))'
            elif i == 4:
                assert str(pds) == '(((((13.0*(x^4.0))+(10.0*(x^3.0)))+(-7.0*(x^2.0)))+(11.0*(x^1.0)))+(-9.0*(x^0.0)))'
        

    ### =============== Problem 1 Tests ========================

    def test_prob01_ut01(self):
        s1 = '5x^2'        
        plus1 = poly_parser.parse_sum(s1)
        ldf1  = lambdifier.lambdify(plus1)
        x = sympy.symbols('x')
        f = 5*x**2
        sympy_ldf1 = sympy.utilities.lambdify((x), f)
        for i in range(10):
            assert np.allclose(ldf1(i), sympy_ldf1(i))

    def test_prob01_ut02(self):
        s1 = '5x^2 + 10x^1'
        plus1 = poly_parser.parse_sum(s1)
        ldf1  = lambdifier.lambdify(plus1)
        x = sympy.symbols('x')
        f = 5*x**2 + 10*x**1
        sympy_ldf1 = sympy.utilities.lambdify((x), f)        
        for i in range(10):
            assert np.allclose(ldf1(i), sympy_ldf1(i))

    def test_prob01_ut03(self):
        s1 = '5x^2 + 10x^1 + 5x^0'
        ## original function
        plus1 = poly_parser.parse_sum(s1)
        ## our lambidification of original function
        ldf1  = lambdifier.lambdify(plus1)
        ## sympy lambdification of original function
        x = sympy.symbols('x')
        f = 5*x**2 + 10*x**1 + 5*x**0
        sympy_ldf1 = sympy.utilities.lambdify((x), f)
        ## test if our lambidification is equivalent to sympy's
        for i in range(10):
            assert np.allclose(ldf1(i), sympy_ldf1(i))

    def test_prob01_ut04(self):
        tde = tiny_de()
        ldf_lst = tde.lambdify_file('polys.txt')
        x = sympy.symbols('x')
        for i, ldf in enumerate(ldf_lst):
            if i == 0:
                f = 5*x**2
                sympy_ldf = sympy.utilities.lambdify((x), f)
                for i in range(10):
                    assert np.allclose(ldf(i), sympy_ldf(i))
            elif i == 1:
                f = 3.0*x**2.0 + 10.0*x**1.0
                sympy_ldf = sympy.utilities.lambdify((x), f)
                for i in range(10):
                    assert np.allclose(ldf(i), sympy_ldf(i))
            elif i == 2:
                f = 10.0*x**3.0 + 3.0*x**2.0 + -2.0*x**1.0 + -10.0*x**0.0
                sympy_ldf = sympy.utilities.lambdify((x), f)
                for i in range(10):
                    assert np.allclose(ldf(i), sympy_ldf(i))
            elif i == 3:
                f = -14.13*x**5.0 + 10.1*x**4.0 + 7.0*x**3.0 + 11.11*x**2.0 + 5.0*x**1.0 + -12.0*x**0.0
                sympy_ldf = sympy.utilities.lambdify((x), f)
                for i in range(10):
                    assert np.allclose(ldf(i), sympy_ldf(i))
            elif i == 4:
                f = 13.0*x**4.0 + 10.0*x**3.0 + -7.0*x**2.0 + 11.0*x**1.0 + -9.0*x**0.0
                sympy_ldf = sympy.utilities.lambdify((x), f)
                for i in range(10):
                    assert np.allclose(ldf(i), sympy_ldf(i))

    ### ============ Problem 2 ===============================

    def test_prob02_ut01(self):
        s1 = '5x^0'
        plus1 = poly_parser.parse_sum(s1)
        assert str(plus1) == '(5.0*(x^0.0))'
        drv1 = dra.diff(plus1)
        assert isinstance(drv1, const)
        assert np.allclose(drv1.get_val(), 0.0)

    def test_prob02_ut02(self):
        s1 = '5x^1'
        plus1 = poly_parser.parse_sum(s1)
        assert str(plus1) == '(5.0*(x^1.0))'
        drv1 = dra.diff(plus1)
        assert str(drv1) == '(5.0*(x^0.0))'
        assert np.allclose(drv1.get_mult1().get_val(), 5.0)
        assert np.allclose(drv1.get_mult2().get_deg().get_val(), 0.0)
        drv_ = drv1
        for _ in range(1000):
            drv_ = dra.diff(drv_)
            assert isinstance(drv_, const)
            assert np.allclose(drv_.get_val(), 0.0)

    def test_diff_ut03(self):
        s1 = '5x^2'
        plus1 = poly_parser.parse_sum(s1)
        assert str(plus1) == '(5.0*(x^2.0))'
        drv1 = dra.diff(plus1)
        assert str(drv1) == '(10.0*(x^1.0))'
        assert np.allclose(drv1.get_mult1().get_val(), 10.0)
        assert np.allclose(drv1.get_mult2().get_deg().get_val(), 1.0)
        drv2 = dra.diff(drv1)
        assert str(drv2) == '(10.0*(x^0.0))'
        assert np.allclose(drv2.get_mult1().get_val(), 10.0)
        assert np.allclose(drv2.get_mult2().get_deg().get_val(), 0.0)
        drv_ = drv2
        for _ in range(1000):
            drv_ = dra.diff(drv_)
            assert isinstance(drv_, const)
            assert np.allclose(drv_.get_val(), 0.0)

    def test_diff_ut04(self):
        s1 = '5x^3'
        plus1 = poly_parser.parse_sum(s1)
        assert str(plus1) == '(5.0*(x^3.0))'
        drv = plus1
        for i in range(1, 4):
            drv = dra.diff(drv)
            if i == 1:
                assert str(drv) == '(15.0*(x^2.0))'
            elif i == 2:
                assert str(drv) == '(30.0*(x^1.0))'
            elif i == 3:
                assert str(drv) == '(30.0*(x^0.0))'
            elif i > 3:
                assert str(drv) == '0.0'

    def test_diff_ut05(self):
        s1 = '5x^-3'
        plus1 = poly_parser.parse_sum(s1)
        assert str(plus1) == '(5.0*(x^-3.0))'
        drv = plus1
        for i in range(1, 4):
            drv = dra.diff(drv)
            print('drv{} = {}'.format(i, drv))

    def test_diff_ut06(self):
        s1 = '5x^1 + 7x^0'
        plus1 = poly_parser.parse_sum(s1)
        drv = plus1
        for i in range(1, 4):
            drv = dra.diff(drv)
            if i == 1:
                assert str(drv) == '((5.0*(x^0.0))+0.0)'
            else:
                assert str(drv) == '(0.0+0.0)'
            print('diff_ut06: drv{} = {}'.format(i, drv))

    def test_diff_ut07(self):
        s1 = '5x^2 + 7x^1 + 2x^0'
        plus1 = poly_parser.parse_sum(s1)
        drv = plus1
        for i in range(1, 10):
            drv = dra.diff(drv)
            if i == 1:
                assert str(drv) == '(((10.0*(x^1.0))+(7.0*(x^0.0)))+0.0)'
            elif i == 2:
                assert str(drv) == '(((10.0*(x^0.0))+0.0)+0.0)'
            else:
                assert str(drv) == '((0.0+0.0)+0.0)'
            print('diff_ut07: drv{} = {}'.format(i, drv))

    ## ============ Problem 3 ===================

    def test_prob03_ut01(self):
        text = '1x^2'
        ni = 15
        zr = nra.zr1(text, 1.0, num_iters=ni)
        print('\ntest_nra_ut01: zr={}; num_iters={}'.format(zr,ni))
        assert nra.check_zr(text, zr)

    def test_prob03_ut02(self):
        text = '300x^7 + -6x^4 + -30x^3 + 45x^2 + 7x^1 + 10x^0'
        ni = 40
        zr = nra.zr1(text, 5.0, num_iters=ni)
        print('\ntest_nra_ut02: zr={}; num_iters={}'.format(zr, ni))
        assert nra.check_zr(text, zr)

    def test_prob03_ut03(self):
        text = '300x^7 + -6x^4 + -30x^3 + 45x^2 + 7x^1 + 10x^0'
        zr, ni = nra.zr2(text, 5.0)
        print('\ntest_nra_ut03: zr={}; num_iters={}'.format(zr, ni))
        assert nra.check_zr(text, zr)

    def test_prob03_ut04(self):
        text = '1x^2 + -2x^0'
        ni = 7
        zr = nra.zr1(text, 1.0, num_iters=ni)
        print('\ntest_nra_ut04: zr={}; num_iters={}'.format(zr, ni))
        assert nra.check_zr(text, zr)
        assert np.allclose(math.sqrt(2), zr)

    def test_prob03_ut05(self):
        text = '1x^2 + -3x^0'
        ni = 7
        zr = nra.zr1(text, 1.0, num_iters=ni)
        print('\ntest_nra_ut05: zr={}; num_iters={}'.format(zr, ni))
        assert nra.check_zr(text, zr)
        assert np.allclose(math.sqrt(3), zr)

    def test_prob03_ut06(self):
        text = '1x^2 + -5x^0'
        ni = 7
        zr = nra.zr1(text, 1.0, num_iters=ni)
        print('\ntest_nra_ut06: zr={}; num_iters={}'.format(zr, ni))
        assert nra.check_zr(text, zr)
        assert np.allclose(math.sqrt(5), zr)

    def test_prob03_ut07(self):
        text = '1x^2 + -7x^0'
        ni = 7
        zr = nra.zr1(text, 1.0, num_iters=ni)
        print('\ntest_nra_ut06: zr={}; num_iters={}'.format(zr, ni))
        assert nra.check_zr(text, zr)
        assert np.allclose(math.sqrt(7), zr)

    def test_prob03_ut07(self):
        text = '1x^2 + -11x^0'
        ni = 7
        zr = nra.zr1(text, 1.0, num_iters=ni)
        print('\ntest_nra_ut07: zr={}; num_iters={}'.format(zr, ni))
        assert nra.check_zr(text, zr)
        assert np.allclose(math.sqrt(11), zr)

    def test_prob03_ut08(self):
        text = '1x^2 + -13x^0'
        ni = 7
        zr = nra.zr1(text, 1.0, num_iters=ni)
        print('\ntest_nra_ut07: zr={}; num_iters={}'.format(zr, ni))
        assert nra.check_zr(text, zr)
        assert np.allclose(math.sqrt(13), zr)

    def test_prob03_ut09(self):
        for i in (2, 3,	5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71):
            text = '1x^2 + -{}x^0'.format(i)
            zr = nra.zr1(text, 1.0, num_iters=7)
            assert nra.check_zr(text, zr)
            assert np.allclose(math.sqrt(i), zr)
            print('\nour sqrt({}) = {}; math.sqrt({}) = {}'.format(i, zr, i, math.sqrt(i)))

    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
