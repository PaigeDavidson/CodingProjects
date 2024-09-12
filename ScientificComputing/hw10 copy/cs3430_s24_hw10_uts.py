#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: cs3430_s24_hw10_uts.py
# description: unit tests for CS 3430: S24: Assignment 10
# -----------------------------------------------------------
# bugs to vladimir kulyukin in canvas
#############################################################

import unittest
from prng import prng
from seqrand import *
import numpy as np
import random

class cs3430_s24_hw10_uts(unittest.TestCase):
    
    # def __check_uniqueness(self, rns):
    #     """
    #     True if all numbers in rns are unique.
    #     """
    #     return len(set(rns)) == len(rns)

    # @staticmethod
    # def __scale(data, a, b):
    #     """
    #     scale data to be in [a, b].
    #     """
    #     assert a < b
    #     b_a = (b-a)
    #     min_d, max_d = np.min(data), np.max(data)
    #     norm = max_d - min_d
    #     return np.array([int(b_a*((d - min_d)/norm) + a) for d in data])

    # ### ================ Problem 01 =====================    

    # def test_hw10_prob01_ut03(self):
    #     a, b, m, n, seed = 214013, 2531011, 4294967296, 20, 11235
    #     lcgg = prng.lcg(a, b, m, n, x0=seed)()
    #     rns = [next(lcgg) for _ in range(n)]
    #     print('LCG random numbers: {}'.format(rns))
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique')

    # def test_hw10_prob01_ut04(self):
    #     a, b, m, n, seed = 214013, 2531011, 4294967296, 20, 11235
    #     lcgg = prng.lcg(a, b, m, n, x0=seed)()
    #     rns = [next(lcgg) for _ in range(n)]
    #     print('LCG random numbers: {}'.format(rns))
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique')

    # def test_hw10_prob01_ut05(self):
    #     a, b, m, n, seed = 214013, 2531011, 4294967296, 10000000, 11235
    #     lcgg = prng.lcg(a, b, m, n, x0=seed)()
    #     rns = [next(lcgg) for _ in range(n)]
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique')

    # def test_hw10_prob01_ut06(self):
    #     a, b, m, n, seed = 438293613, (2**13 + 13), 2**30, 20000000, 58132134
    #     lcgg = prng.lcg(a, b, m, n, x0=seed)()
    #     rns = [next(lcgg) for _ in range(n)]
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique')

    # def test_hw10_prob01_ut07(self):
    #     a, b, m, n, seed = 12132445, (2**17 + 17), 2**36, 30000000, 11235813
    #     lcgg = prng.lcg(a, b, m, n, x0=seed)()
    #     rns = [next(lcgg) for _ in range(n)]
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique')

    # def test_hw10_prob01_ut08(self):
    #     a, b, m, n, seed = 181465474592829, (2**19 + 19), 2**48, 40000000, 3581311224
    #     lcgg = prng.lcg(a, b, m, n, x0=seed)()
    #     rns = [next(lcgg) for _ in range(n)]
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique')

    # def test_hw10_prob01_ut09(self):
    #     a, b, m, n, seed = 454339144066433781, (2**23 + 23), 2**60, 50000000, 3582241311
    #     lcgg = prng.lcg(a, b, m, n, x0=seed)()
    #     rns = [next(lcgg) for _ in range(n)]
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique')

    # def test_hw10_prob01_ut10(self):
    #     a, b, c, n, seed = 1, 3, 10, 5, 1
    #     xsg = prng.xorshift(a, b, c, n, x0=seed)()
    #     rns = [next(xsg) for _ in range(n)]
    #     print('XORSHIFT random numbers: {}'.format(rns))
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique')


    # def test_hw10_prob01_ut11(self):
    #     a, b, c, n, seed = 1, 3, 10, 10, 3
    #     xsg = prng.xorshift(a, b, c, n, x0=seed)()
    #     rns = [next(xsg) for _ in range(n)]
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique')

    # def test_hw10_prob01_ut12(self):
    #     a, b, c, n, seed = 1, 3, 10, 20, 5
    #     xsg = prng.xorshift(a, b, c, n, x0=seed)()
    #     rns = [next(xsg) for _ in range(n)]
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique')        

    # def test_hw10_prob01_ut13(self):
    #     a, b, c, n, seed = 1, 3, 10, 1000000, 7
    #     xsg = prng.xorshift(a, b, c, n, x0=seed)()
    #     rns = [next(xsg) for _ in range(n)]
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique')

    # def test_hw10_prob01_ut14(self):
    #     a, b, c, n, seed = 2, 5, 15, 1000000, 13
    #     xsg = prng.xorshift(a, b, c, n, x0=seed)()
    #     rns = [next(xsg) for _ in range(n)]
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique')

    # def test_hw10_prob01_ut15(self):
    #     a, b, c, n, seed = 3, 23, 25, 2000000, 17
    #     xsg = prng.xorshift(a, b, c, n, x0=seed)()
    #     rns = [next(xsg) for _ in range(n)]
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique')

    # def test_hw10_prob01_ut16(self):
    #     a, b, c, n, seed = 5, 9, 28, 20000000, 19
    #     xsg = prng.xorshift(a, b, c, n, x0=seed)()
    #     rns = [next(xsg) for _ in range(n)]
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique')

    # def test_hw10_prob01_ut17(self):
    #     a, b, c, n, seed = 7, 13, 25, 30000000, 23
    #     xsg = prng.xorshift(a, b, c, n, x0=seed)()
    #     rns = [next(xsg) for _ in range(n)]
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique...')

    # def test_hw10_prob01_ut18(self):
    #     a, b, c, n, seed = 13, 3, 27, 50000000, 113
    #     xsg = prng.xorshift(a, b, c, n, x0=seed)()
    #     rns = [next(xsg) for _ in range(n)]
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique...')

    # def test_hw10_prob01_ut19(self):
    #     a, b, c, n, seed = 13, 3, 27, 50000000, 117
    #     xsg = prng.xorshift(a, b, c, n, x0=seed)()
    #     rns = [next(xsg) for _ in range(n)]
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique...')

    # def test_hw10_prob01_ut20(self):
    #     seed, start, stop, n = 1, 0, 1000, 5
    #     mtw = prng.mersenne_twister(n, x0=seed, lower=start, upper=stop)()
    #     rns = [next(mtw) for _ in range(n)]
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique...')

    # def test_hw10_prob01_ut21(self):
    #     seed, start, stop, n = 1, 0, 1000, 10
    #     mtw = prng.mersenne_twister(n, x0=seed, lower=start, upper=stop)()
    #     rns = [next(mtw) for _ in range(n)]
    #     print('Mersenne Twister random numbers: {}'.format(rns))
    #     assert len(rns) == n
    #     if self.__check_uniqueness(rns):
    #         print('all random numbers are unique...')

    # ### ================ Problem 02 =================================

    # def test_hw10_prob02_ut01(self):
    #     pim = get_mantissa('pi.txt') 
    #     v, pv = chisquare_str_digit_seq(pim, seq_start=0, seq_end=10)
    #     assert 7.9 < v < 8.1
    #     assert 0.52 < pv < 0.54

    # def test_hw10_prob02_ut02(self):
    #     em = get_mantissa('e.txt') 
    #     v, pv = chisquare_str_digit_seq(em, seq_start=0, seq_end=10)
    #     assert 15.9 < v < 16.1
    #     assert 0.05 < pv < 0.07

    # def test_hw10_prob02_ut03(self):
    #     pim = get_mantissa('pi.txt') 
    #     v, pv = chisquare_str_digit_seq(pim, seq_start=3, seq_end=16)
    #     assert 9.2 < v < 9.4
    #     assert 0.39 < pv < 0.42

    # def test_hw10_prob02_ut04(self):
    #     em = get_mantissa('e.txt') 
    #     v, pv = chisquare_str_digit_seq(em, seq_start=3, seq_end=16)
    #     assert 9.2 < v < 9.4
    #     assert 0.39 < pv < 0.42
    
    ### ================ Problem 03 =====================================

    ### I got b/w 80% and 100% on all these tests. 
    def test_hw10_prob03_ut01(self):
        count, percent = chisquare_mersenne_twister(seq_len=10, num_experiments=10)
        print('count   = {}'.format(count))
        print('percent = {}'.format(percent))

    def test_hw10_prob03_ut02(self):
        count, percent = chisquare_mersenne_twister(seq_len=20, num_experiments=100)
        print('count   = {}'.format(count))
        print('percent = {}'.format(percent))

    def test_hw10_prob03_ut03(self):
        count, percent = chisquare_mersenne_twister(seq_len=20, num_experiments=1000)
        print('count   = {}'.format(count))
        print('percent = {}'.format(percent))
        
    def test_hw10_prob03_ut04(self):
        count, percent = chisquare_mersenne_twister(seq_len=30, num_experiments=1000)
        print('count   = {}'.format(count))
        print('percent = {}'.format(percent))
        
    def test_hw10_prob03_ut05(self):
        count, percent = chisquare_mersenne_twister(seq_len=40, num_experiments=1000)
        print('count   = {}'.format(count))
        print('percent = {}'.format(percent))

    def test_hw10_prob03_ut06(self):
        count, percent = chisquare_mersenne_twister(seq_len=50, num_experiments=1000)
        print('count   = {}'.format(count))
        print('percent = {}'.format(percent))

    def test_hw10_prob03_ut07(self):
        count, percent = chisquare_mersenne_twister(seq_len=50, num_experiments=1000)
        print('count   = {}'.format(count))
        print('percent = {}'.format(percent))
    
    ### ================ Problem 04 =====================================

    ### Let's swallow a few random PILs.

    ## this UT should generate the left image on slide 14, Lecture 21
    # def test_hw10_prob04_ut01(self):
    #     w, h = 600, 600
    #     n = h * w
    #     a, b, m, seed = 214013, 2531011, 4294967291, 0
    #     data = prng.gen_lcg_data(a, b, m, n, seed=seed, option=1)
    #     prng.random_pil(data, w, h, n, name='random_pil_01', save_flag=True)

    # ### this UT should generate the right image on Slide 14 in Lecture 21.
    # def test_hw10_prob04_ut02(self):
    #     w, h = 600, 600
    #     n = h * w
    #     a, b, m, seed = 214013, 2531011, 4294967291, 0
    #     data = prng.gen_lcg_data(a, b, m, n, seed=seed, option=2)
    #     prng.random_pil(data, w, h, n, name='random_pil_02', save_flag=True)

    # def test_hw10_prob04_ut03(self):
    #     w, h = 600, 600
    #     n = h * w
    #     a, b, m, seed = 214013, 2531011, 4294967291, 0
    #     data = prng.gen_lcg_data(a, b, m, n, seed=seed, option=3)
    #     prng.random_pil(data, w, h, n, name='random_pil_03', save_flag=True)

    # ## this UT should generate the image with LCG a, b, m, seed = 12132445, (2**17 + 17), 2**36, 11235813
    # def test_hw10_prob04_ut04(self):
    #     w, h = 600, 600
    #     n = h * w
    #     a, b, m, seed = 12132445, (2**17 + 17), 2**36, 11235813        
    #     data = prng.gen_lcg_data(a, b, m, n, seed=seed, option=1)
    #     prng.random_pil(data, w, h, n, name='random_pil_04', save_flag=True)

    # ### this UT generates the image with LCG a, b, m, seed in [0,600^2-1], (2**17 + 17), 2**36, 11235813
    # def test_hw10_prob04_ut05(self):
    #     w, h = 600, 600
    #     n = h * w
    #     a, b, m, seed = 12132445, (2**17 + 17), 2**36, 11235813        
    #     data = prng.gen_lcg_data(a, b, m, n, seed=seed, option=2)
    #     prng.random_pil(data, w, h, n, name='random_pil_05', save_flag=True)        

    # ## this UT generates the image with XORSHIFT seed=1 and a=1,b=3,c=10.
    # def test_hw10_prob04_ut06(self):
    #     w, h = 600, 600
    #     n = h * w
    #     a, b, c, seed = 1, 3, 10, 1
    #     data = prng.gen_xorshift_data(a, b, c, n, seed=seed, option=1)
    #     prng.random_pil(data, w, h, n, name='random_pil_06', save_flag=True)                

    # ### this UT generates the image with XORSHIFT seed in [1, 600^2] and a=1,b=3,c=10.
    # ### this image should look less "random" than the one above.
    # def test_hw10_prob04_ut07(self):
    #     w, h = 600, 600
    #     n = h * w
    #     a, b, c = 1, 3, 10,
    #     data = prng.gen_xorshift_data(a, b, c, n, option=2)
    #     prng.random_pil(data, w, h, n, name='random_pil_07', save_flag=True)                        

    # ### this UT generates 1024x1024 image with XORSHIFT seed=13 and a=2,b=5,c=15.
    # def test_hw10_prob04_ut08(self):
    #     w, h = 1024, 1024
    #     n = h * w
    #     a, b, c, seed = 2, 5, 15, 13
    #     data = prng.gen_xorshift_data(a, b, c, n, seed=seed, option=1)
    #     prng.random_pil(data, w, h, n, name='random_pil_08', save_flag=True)                                

    # ### this UT generates 1024x1024 image with XORSHIFT seed in [1, 1024^2], a=2,b=5,c=15.
    # def test_hw10_prob04_ut09(self):
    #     w, h = 1024, 1024
    #     n = h * w
    #     a, b, c, seed = 2, 5, 15, 13
    #     data = prng.gen_xorshift_data(a, b, c, n, seed=seed, option=2, )
    #     prng.random_pil(data, w, h, n, name='random_pil_09', save_flag=True)
        
    # ### this UT generates 1024x1024 image with XORSHIFT seed=19, a=2,b=5,c=15.
    # def test_hw10_prob04_ut10(self):
    #     w, h = 1024, 1024
    #     n = h * w
    #     a, b, c, seed = 5, 9, 28, 19
    #     data = prng.gen_xorshift_data(a, b, c, n, seed=seed, option=1)
    #     prng.random_pil(data, w, h, n, name='random_pil_10', save_flag=True)

    # ## this UT generates 1024x1024 image with mersenne twister seed=1, start=0, stop=1000
    # def test_hw10_prob04_ut11(self):
    #     w, h = 1024, 1024
    #     n = h * w
    #     seed, start, stop = 1, 0, 1000
    #     data = prng.gen_mersenne_twister_data(n, seed=seed, option=1)
    #     prng.random_pil(data, w, h, n, name='random_pil_11', save_flag=True)        

    # ## this UT generates 1024x1024 image with mersenne twister seed=[0, 1024^2-1], start=0, stop=1000
    # ## this image should look very similar to the one generated by the previous method.
    # def test_hw10_prob04_ut12(self):
    #     w, h = 1024, 1024
    #     n = h * w
    #     start, stop = 0, 1000
    #     data = prng.gen_mersenne_twister_data(n, option=2)
    #     prng.random_pil(data, w, h, n, name='random_pil_12', save_flag=True)

    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
