#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: cs3430_s24_hw08_uts.py
# description: unit tests for CS 3430: S24: Assignment 08
# -----------------------------------------------------------
# bugs to vladimir kulyukin in canvas.
#############################################################

import unittest
import decimal
import math
from rat import rat
from picf import picf
from ecf  import ecf
from cpi import cpi

### STR_E and STR_PI globals are used in some unit tests.
### Euler's number with the first 85 digits of the mantissa in a string.
STR_E  = '2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713'
# math.e  2.718281828459045 -- the value of math.e with a 15-digit mantissa
### Pi with the fist 85 digits of the mantissa in a string.
STR_PI = '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280'
# math.pi 3.141592653589793 -- the value of math.pi with a 15-digit mantissa

class cs3430_s24_hw08_uts(unittest.TestCase):

    ### =============== Testing Rats =========================

    def test_rat_01(self):
        r1 = rat(2, 1)
        r2 = rat(3, 1)
        s1 = r1.add(r2)
        s2 = r2.add(r1)
        assert s1.get_n() == s2.get_n() == 5
        assert s1.get_d() == s2.get_d() == 1
        assert str(s1) == '5/1'

    def test_rat_02(self):
        r1 = rat(6, 1)
        r2 = rat(9, 6)
        s1 = r1.add(r2)
        s2 = r2.add(r1)
        assert s1.get_n() == s2.get_n() == 15
        assert s1.get_d() == s1.get_d() == 2
        assert str(s1) == '15/2'
        assert str(s2) == '15/2'

    def test_rat_03(self):
        r1 = rat(6, 1)
        r2 = rat(25, 6)
        s1 = r1.add(r2)
        s2 = r2.add(r1)
        assert str(s1) == '61/6'
        assert str(s2) == '61/6'

    def test_rat_04(self):
        r1 = rat(1, 1)
        r2 = rat(420, 61)
        d1 = r1.div(r2)
        assert str(d1) == '61/420'

    def test_rat_05(self):
        r1 = rat(10, 3)
        r2 = rat(11, 7)
        m1 = r1.mult(r2)
        m2 = r2.mult(r1)
        assert str(m1) == '110/21'
        assert str(m2) == '110/21'
        assert str(rat.flip(m1)) == '21/110'
        assert str(rat.flip(m2)) == '21/110'


    ## =============== Capturing the E Rat ==================

    def test_ecf_ut_01(self):
        ## 1st e rat captured
        e_rat1 = ecf.arx_rat(1)
        assert e_rat1.get_n() == 3
        assert e_rat1.get_d() == 1

        ## 2nd e rat captured
        e_rat2 = ecf.arx_rat(2)
        assert e_rat2.get_n() == 8
        assert e_rat2.get_d() == 3

        # 3rd e rat captured
        e_rat3 = ecf.arx_rat(3)
        assert e_rat3.get_n() == 11
        assert e_rat3.get_d() == 4

        ## 4th e rat captured
        e_rat4 = ecf.arx_rat(4)
        assert e_rat4.get_n() == 19
        assert e_rat4.get_d() == 7

        ## 5th e rat captured
        e_rat5 = ecf.arx_rat(5)
        assert e_rat5.get_n() == 87
        assert e_rat5.get_d() == 32

        ## 7th e rat captured
        e_rat7 = ecf.arx_rat(7)
        assert str(e_rat7) == '193/71'

        ## 5th e rat captured
        e_rat13 = ecf.arx_rat(13)
        assert str(e_rat13) == '49171/18089'

    ## I kept the number of iterations in test_ecf_ut_02() to 100 when I ran
    ## the unit test on my laptop.
    ## with prec=20, I get 2.7182818284590452354
    ## with prec=30, I get 2.71828182845904523536028747135
    ## with prec=40, I get 2.718281828459045235360287471352662497757
    ## with prec=50, I get 2.7182818284590452353602874713526624977572470937000
    ## STR_E digits:       2.7182818284590452353602874713526624977572470936999
    ## with prec=70, I get 2.718281828459045235360287471352662497757247093699959574966967627724077
    ## STR_E digits:       2.718281828459045235360287471352662497757247093699959574966967627724076
    ## with prec=80, I get 2.7182818284590452353602874713526624977572470936999595749669676277240766303535476
    ## STR_E digits:       2.7182818284590452353602874713526624977572470936999595749669676277240766303535475
    ## with prec=86, I get 2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945714
    ## STR_E digits        2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713
    ## The last approximation is spot on except for the last digit on the mantissa
    def test_ecf_ut_02(self, prec=86):
        decimal.getcontext().prec = prec
        math_e = decimal.Decimal(math.e)
        err = 0
        num_iters = 100
        for i in range(1, num_iters):
            cf_e = ecf.arx_real(i, prec=prec)
            err = abs(cf_e - math_e)
            #print('math.e = {}'.format(math_e))
            #print('cf_e   = {}'.format(cf_e))
            #print('error  = {}'.format(err))
        assert err < 1.0e-10

    ## When I ran test_ecf_ut_03() on my laptop, the for-loop in broke at iteration i = 77 on
    ## with precision set to 90. In other words,
    ## all 85 digits of the mantissa, when converted to a string, coincided with
    ## all 85 digits of STR_E
    def test_ecf_ut_03(self, prec=90):
        decimal.getcontext().prec = prec
        for i in range(100):
            cf_e = ecf.arx_real(i, prec=prec)
            #print(STR_E[2:][:80])
            #print(str(cf_e)[2:][:80])
            if STR_E[2:][:85] == str(cf_e)[2:][:85]:
                print('i == {}'.format(i))
                break
        assert STR_E[2:][:85] == str(cf_e)[2:][:85]

    ### =============== Capturing the Pi Rat ==================

    def test_pi_rat_ut_01(self):
        ## 1st pi rat captured
        pi_rat_1 = picf.arx_rat(1)
        assert pi_rat_1.get_n() == 19
        assert pi_rat_1.get_d() == 6

        ## 2nd pi rat captured
        pi_rat_2 = picf.arx_rat(2)
        assert pi_rat_2.get_n() == 47
        assert pi_rat_2.get_d() == 15

        ## 3rd pi rat captured
        pi_rat_3 = picf.arx_rat(3)
        assert pi_rat_3.get_n() == 1321
        assert pi_rat_3.get_d() == 420

        ## 4th pi rat captured
        pi_rat_4 = picf.arx_rat(4)
        assert pi_rat_4.get_n() == 989
        assert pi_rat_4.get_d() == 315

    ### In test_picf_ut_01(), these are the results
    ### I got on my laptop:
    ### num_iters = 100, pi = 3.1415929035585527643
    ### STR_PI    =           3.1415926535897932384
    ### num_iters = 200, pi = 3.1415926848388167504
    ### num_iters = 300, pi = 3.1415926628489239013
    ### num_iters = 500, pi = 3.1415926555897832386
    ### math.pi             = 3.141592653589793
    def test_picf_ut_01(self, prec=20):
        decimal.getcontext().prec=prec
        for i in range(500):
            pi_cf = picf.arx_real(i, prec=prec)
        assert abs(decimal.Decimal(math.pi) - pi_cf) < 1.0e-7

    ### test_cpi_ut_01() tests the Chudnovsky algorithm.
    ### when I ran it on [1,30] at prec=96, I got the first 85 digits
    ### of the mantissa correctly. I give the both below. 
    # PI_1_30 = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280
    # STR_PI  = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280
    def test_cpi_ut_01(self):
        PI_1_30 = cpi.arx_real(30,prec=86)
        print(PI_1_30)
        decimal.getcontext().prec=30
        assert abs(decimal.Decimal(math.pi) - PI_1_30) < 1.0e-5
        
    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
