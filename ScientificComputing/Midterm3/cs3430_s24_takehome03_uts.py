#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: cs3430_s24_takehome03_uts.py
# description: unit tests for CS 3430: S24: Takehome 03
# -----------------------------------------------------------
# bugs to vladimir kulyukin in canvas
#############################################################

import unittest
import numpy as np
import math
from cs3430_s24_takehome03 import fourier_coeffs
from cs3430_s24_takehome03 import nth_partial_sum
from cs3430_s24_takehome03 import plot_function_and_nth_partial_sum
from cs3430_s24_takehome03 import gen_lcg
from cs3430_s24_takehome03 import gen_xorshift_32
from cs3430_s24_takehome03 import make_lcg_pix
from cs3430_s24_takehome03 import make_random_pil
from cs3430_s24_takehome03 import make_xorshift_32_pix
from cs3430_s24_takehome03 import make_equal_probs_table
from cs3430_s24_takehome03 import get_coin_flip_seqs
from cs3430_s24_takehome03 import is_sufficiently_knuth_random
from cs3430_s24_takehome03 import get_sufficiently_knuth_random_coin_flip_seqs
from cs3430_s24_takehome03 import get_insufficiently_knuth_random_coin_flip_seqs
from cs3430_s24_takehome03 import get_die_throw_seqs
from cs3430_s24_takehome03 import get_sufficiently_knuth_random_die_throw_seqs
from cs3430_s24_takehome03 import get_insufficiently_knuth_random_die_throw_seqs
from cs3430_s24_takehome03 import learn_bin_id3_dt
from cs3430_s24_takehome03 import display_bin_id3_dt
from cs3430_s24_takehome03 import entropy
from cs3430_s24_takehome03 import gain
from bin_id3 import bin_id3


class cs3430_s24_takehome03_uts(unittest.TestCase):

    ### ================ Problem 01 =====================

    def test_prob01_ut01(self):
        f = lambda x: x
        num_coeffs = 10
        a, b = -math.pi, math.pi
        romb = 7
        acoeffs, bcoeffs = fourier_coeffs(f, num_coeffs=num_coeffs, a=a, b=b, romb=romb)
        
        print('acoeffs = {}'.format(acoeffs))
        print('bcoeffs = {}'.format(bcoeffs))
        assert len(acoeffs) == num_coeffs
        assert len(bcoeffs) == num_coeffs-1

        cos_coeffs = [1.9167424470397265904e-16, -5.7726422949673784635e-16,
                      1.2853874331443990132e-16, 1.1243537818621695905e-16,
                      -1.4290534449404764451e-16, -1.4331328312308083276e-16,
                      -1.1599049573127165611e-17, -8.23647550419253166e-16,
                      1.2714402738692598178e-15, -6.0597117709531071945e-16]
        sin_coeffs = [2.0000000000088117395, -0.9999999807587440647,
                      0.66666626271204544054, -0.5000083904508157006,
                      0.4000293375982872722, -0.3334275124603605909,
                      0.28615674271760352997, -0.2491760026717393517,
                      0.21997872092842016044]

        ### I use pretty loose assertions to allow for numerical instability.
        for ac, cc in zip(acoeffs, cos_coeffs):
            assert abs(ac-cc) <= 1e-3
        for bc, sc in zip(bcoeffs, sin_coeffs):
            assert abs(bc-sc) <= 1e-3

    ## ================ Problem 02 =====================

    def test_prob02_ut01(self):
        f = lambda x: x
        num_coeffs = 20
        a, b = -math.pi, math.pi
        romb = 7
        acoeffs, bcoeffs = fourier_coeffs(f, num_coeffs=num_coeffs, a=a, b=b, romb=romb)
        for x in range(0, 10):
            print(nth_partial_sum(x, acoeffs, bcoeffs))

    ## ================ Problem 03 =====================


    def test_prob03_ut01(self):
        f = lambda x: x
        plot_function_and_nth_partial_sum(f, 'y=x', num_coeffs=20, num_points=1000,
                                          a=-math.pi, b=math.pi, romb=7)

    def test_prob03_ut02(self, num_points=1000, num_coeffs=3):
        f = lambda x: x**2
        plot_function_and_nth_partial_sum(f, 'y=x^2', num_coeffs=20, num_points=100,
                                          a=-math.pi, b=math.pi, romb=7)

    def test_prob03_ut03(self, num_points=1000, num_coeffs=3):
        f = lambda x: x**3
        plot_function_and_nth_partial_sum(f, 'y=x^3', num_coeffs=20, num_points=100,
                                          a=-math.pi, b=math.pi, romb=7)

    def test_prob03_ut04(self, num_points=1000, num_coeffs=3):
        f = lambda x: x+1
        plot_function_and_nth_partial_sum(f, 'y=x+1', num_coeffs=20, num_points=100,
                                          a=-math.pi, b=math.pi, romb=7)

    def test_prob03_ut04(self, num_points=1000, num_coeffs=3):
        f = lambda x: x**5
        plot_function_and_nth_partial_sum(f, 'y=x^5', num_coeffs=20, num_points=100,
                                          a=-math.pi, b=math.pi, romb=7)
    
    def test_prob03_ut05(self, num_points=1000, num_coeffs=3):
        f = lambda x: math.cos(x)        
        plot_function_and_nth_partial_sum(f, 'y=cosx', num_coeffs=20, num_points=100,
                                          a=-math.pi, b=math.pi, romb=7)
    
    def test_prob03_ut06(self, num_points=1000, num_coeffs=3):
        f = lambda x: math.cos(x) + 2*math.cos(2*x)
        plot_function_and_nth_partial_sum(f, 'y=cosx+2cos2x', num_coeffs=20, num_points=100,
                                          a=-math.pi, b=math.pi, romb=7)

    def test_prob03_ut07(self, num_points=1000, num_coeffs=3):        
        f = lambda x: math.cos(x) + 2*math.cos(2*x) + 3*math.cos(3*x) + 4*math.cos(4*x) + 5*math.cos(5*x)
        plot_function_and_nth_partial_sum(f, 'y=cosx+2cosx+3cos3x+4cos4x+5cos5x', num_coeffs=20, num_points=100,
                                          a=-math.pi, b=math.pi, romb=7)

    def test_prob03_ut08(self, num_points=1000, num_coeffs=3):        
        f = lambda x: math.cos(x) + math.sin(x)
        plot_function_and_nth_partial_sum(f, 'y=cosx+sinx', num_coeffs=20, num_points=100,
                                          a=-math.pi, b=math.pi, romb=7)

    def test_prob03_ut09(self, num_points=1000, num_coeffs=3):
        f = lambda x: math.cos(x) + math.sin(x) + 2*math.cos(2*x) + 2*math.sin(2*x)
        plot_function_and_nth_partial_sum(f, 'y=cosx+sinx+cos2x+sin2x',
                                          num_coeffs=20, num_points=100,
                                          a=-math.pi, b=math.pi, romb=7)

    def test_prob03_ut10(self, num_points=1000, num_coeffs=3):
        f = lambda x: math.cos(x) - math.sin(x) + 2*math.cos(2*x) - 2*math.sin(2*x)
        plot_function_and_nth_partial_sum(f, 'y=cosx-sinx+cos2x-sin2x',
                                          num_coeffs=20, num_points=100,
                                          a=-math.pi, b=math.pi, romb=7)

    ### ===================== Problem 04 ================================

    def test_prob04_ut01(self):
        a, b, m, n, seed = 214013, 2531011, 4294967296, 20, 11235
        num_rands = 3
        lcgg = gen_lcg(a, b, m, n, x0=seed)
        rns = [next(lcgg) for _ in range(num_rands)]
        my_rns = [2406967066, 1047613813, 1389674084]
        for r1, r2 in zip(rns, my_rns):
            assert np.allclose(r1,r2)

    def test_prob04_ut02(self):
        a, b, m, n, seed = 438293613, (2**13 + 13), 2**30, 20000000, 58132134
        num_rands = 5
        lcgg = gen_lcg(a, b, m, n, x0=seed)
        rns = [next(lcgg) for _ in range(num_rands)]
        my_rns = [894004411, 653477804, 851711049, 488650530, 897433991]        
        for r1, r2 in zip(rns, my_rns):
            np.allclose(r1,r2)

    def test_prob04_ut03(self):
        a, b, m, n, seed = 12132445, (2**17 + 17), 2**36, 30000000, 11235813            
        num_rands = 5
        lcgg = gen_lcg(a, b, m, n, x0=seed)
        rns = [next(lcgg) for _ in range(num_rands)]
        my_rns = [47161016386, 8056231947, 17658436624, 33015689697, 19855277774]        
        for r1, r2 in zip(rns, my_rns):
            np.allclose(r1,r2)

    ### ===================== Problem 05 ================================

    def test_prob05_ut01(self):
        a, b, c, n, seed = 1, 3, 10, 5, 1
        xsg = gen_xorshift_32(a, b, c, n, x0=seed)
        num_rands = 3        
        rns = [next(xsg) for _ in range(num_rands)]
        my_rns = [1, 3075, 5898885]
        for r1, r2 in zip(rns, my_rns):
            np.allclose(r1,r2)

    def test_prob05_ut02(self):
        a, b, c, n, seed = 1, 3, 10, 10, 3
        xsg = gen_xorshift_32(a, b, c, n, x0=seed)
        num_rands = 5
        rns = [next(xsg) for _ in range(num_rands)]
        my_rns = [3, 5125, 15598478, 1342456832, 3680195968]
        for r1, r2 in zip(rns, my_rns):
            np.allclose(r1,r2)

    def test_prob05_ut03(self):
        a, b, c, n, seed = 1, 3, 10, 20, 5
        xsg = gen_xorshift_32(a, b, c, n, x0=seed)
        num_rands = 7        
        rns = [next(xsg) for _ in range(num_rands)]
        my_rns = [5, 14350, 17039632, 3043023702, 2438222917, 2819504982, 2801864773]
        assert len(rns) == num_rands
        for r1, r2 in zip(rns, my_rns):
            np.allclose(r1,r2)

    ### ========================== Problem 06 ================================

    def test_prob06_ut01(self):
        a, b, m, seed = 214013, 2531011, 4294967296, 11235
        for x in (23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67):
            # 1. x is the width and the height of a square PIL image
            # 2. let's generate random pixels
            n = x**2
            pix = make_lcg_pix(a, b, m, n, seed=seed)
            # 3. let's save the random image
            make_random_pil(pix, x, x, n, name='my_random_lcg_pil_{}'.format(x), save_flag=True)

    ### ========================== Problem 07 ================================

    def test_prob07_ut01(self):
        a, b, c, seed = 1, 3, 10, 1
        for x in (23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67):
            # 1. x is the width and the height of a square PIL image
            # 2. let's generate random pixels
            n = x**2
            pix = make_xorshift_32_pix(a, b, c, n, seed=seed)
            # 3. let's save the random image
            make_random_pil(pix, x, x, n, name='my_random_xor32_pil_{}'.format(x), save_flag=True)

    ### ========================== Problem 08 ================================

    def test_prob08_ut01(self):
        num_coin_flips = 3
        coin_flip_universe = get_coin_flip_seqs(num_coin_flips)
        pt = make_equal_probs_table(1,2)
        sufficiently_random_seqs = set(('211', '121', '221', '112', '212', '122'))
        srs = set([s for s in coin_flip_universe if is_sufficiently_knuth_random(s, pt)])
        ## this assertion tests the set-theoretic difference between
        ## the set sufficiently_random_seqs and the set srs.
        ## the two sets in classical set theory are considered "equal" if
        ## their difference is the empty set, i.e., there is no difference
        ## between the two: all elements of one set are in the other, and
        ## vice versa.
        assert len(srs.difference(sufficiently_random_seqs)) == 0

    def test_prob08_ut02(self):
        num_coin_flips = 4
        coin_flip_universe = get_coin_flip_seqs(num_coin_flips)
        pt = make_equal_probs_table(1,2)
        sufficiently_random_seqs = set(('2111', '1112', '2122', '1121', '1222', '1211', '2221', '2212'))
        srs = set([s for s in coin_flip_universe if is_sufficiently_knuth_random(s, pt)])
        assert len(srs.difference(sufficiently_random_seqs)) == 0

    def test_prob08_ut03(self):
        num_coin_flips = 5
        coin_flip_universe = get_coin_flip_seqs(num_coin_flips)
        pt = make_equal_probs_table(1,2)
        sufficiently_random_seqs = set(('12221', '21221', '11212', '22122', '12121', '21112',
                                        '12111', '12122', '12212', '21222', '12222', '22121',
                                        '11221', '11122', '12112', '11211', '11121', '12211',
                                        '11222', '22111', '21121', '21211', '21122', '11112',
                                        '21212', '21111', '22212', '22221', '22211', '22112'))
        srs = set([s for s in coin_flip_universe if is_sufficiently_knuth_random(s, pt)])
        assert len(srs.difference(sufficiently_random_seqs)) == 0

    def test_prob08_ut04(self):
        num_coin_flips = 10
        ### let's take a deep breath ...
        coin_flip_universe = get_coin_flip_seqs(num_coin_flips)
        pt = make_equal_probs_table(1,2)
        non_random_seq_count = 0
        for s in coin_flip_universe:
             if not is_sufficiently_knuth_random(s, pt):
                 non_random_seq_count += 1
        ### ... and exhale!
        assert non_random_seq_count == 364 ## out of 1024

    def test_prob08_ut05(self):
        num_coin_flips = 15
        ### let's take a deeper breath ...
        coin_flip_universe = get_coin_flip_seqs(num_coin_flips)
        pt = make_equal_probs_table(1,2)
        non_random_seq_count = 0
        for s in coin_flip_universe:
             if not is_sufficiently_knuth_random(s, pt):
                 non_random_seq_count += 1
        ### ... and exhale! I'm still breathing, which is good!
        assert non_random_seq_count == 3882 ## out of 32,768

    # my own unit test to check the sufficient and infufficiently random sequences
    def test_prob08_ut05(self):
        srs=get_sufficiently_knuth_random_coin_flip_seqs(3)
        print(srs)
        isrs=get_insufficiently_knuth_random_coin_flip_seqs(3)
        assert len(srs) + len(isrs) == 2**3

    ### ========================== Problem 09 ================================

    def test_prob09_ut01(self):
        num_die_throws = 3
        die_throw_universe = get_die_throw_seqs(num_die_throws)
        pt = make_equal_probs_table(1,6)
        srs  = get_sufficiently_knuth_random_die_throw_seqs(num_die_throws)
        isrs = get_insufficiently_knuth_random_die_throw_seqs(num_die_throws)
        num_srs = len(srs)
        num_isrs = len(isrs)
        assert num_srs + num_isrs == 6**3
        assert num_srs == 210
        ### the devil is in the insufficiently random details.
        assert '666' in isrs

    def test_prob09_ut02(self):
        num_die_throws = 5
        die_throw_universe = get_die_throw_seqs(num_die_throws)
        pt = make_equal_probs_table(1,6)
        srs  = get_sufficiently_knuth_random_die_throw_seqs(num_die_throws)
        isrs = get_insufficiently_knuth_random_die_throw_seqs(num_die_throws)
        num_srs  = len(srs)
        num_isrs = len(isrs)
        assert num_srs + num_isrs == 6**5
        assert num_srs == 6600
        for sr in ('55165', '33225', '23634', '34556', '46116', '26636'):
            assert sr in srs
        for isr in ('66266', '65423', '56314', '32614', '53426', '16661'):
            assert isr in isrs

    def test_prob09_ut03(self):
        num_die_throws = 7
        ## Another deep breath...
        die_throw_universe = get_die_throw_seqs(num_die_throws)
        pt = make_equal_probs_table(1,6)
        srs  = get_sufficiently_knuth_random_die_throw_seqs(num_die_throws)
        isrs = get_insufficiently_knuth_random_die_throw_seqs(num_die_throws)
        num_srs  = len(srs)
        num_isrs = len(isrs)
        assert num_srs + num_isrs == 6**7
        assert num_srs == 226800
        for sr in ('4313223', '5325531', '4356624', '2524661', '2112525'):
            assert sr in srs
        for isr in ('1432563', '1412444', '5333335', '4452344', '1154263'):
            assert isr in isrs
        ### ... and exhale!

    ### =================== Problem 10 ===============================

    def test_prob10_ut01(self):
        dt_root_node = learn_bin_id3_dt('play_tennis_takehome03.csv')
        display_bin_id3_dt(dt_root_node)

    def test_prob10_ut02(self):
        dt_root_node = learn_bin_id3_dt('play_tennis_takehome03.csv')
        display_bin_id3_dt(dt_root_node)

    def test_prob10_ut03(self):
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis_takehome03.csv')
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        H = entropy(examples, 'PlayTennis', avt)
        print('H = {}'.format(H))
        for attrib in (colnames[1:-1]):
            print('Gain({}) = {}'.format(attrib, gain(examples, 'PlayTennis', attrib, avt)))

    ### ================== Problem 11 ==================================
    ### no unit tests for this problem.
            
    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
