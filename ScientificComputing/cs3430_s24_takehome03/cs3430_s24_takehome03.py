##############################################################
# module: cs3430_s24_takehome03.py
# description: submission file for CS 3430: S24: Takehome 03
# -----------------------------------------------------------
#
# YOUR NAME: Paige Davidson
# YOUR A# A02339425
#
# time spent was ~ 7 hours
# bugs to vladimir kulyukin in canvas
##############################################################

### I commented out my imports. You can add your imports
### as needed.

import unittest
import math
import numpy as np
import scipy as sp
import scipy.stats
from rmb import rmb
import matplotlib.pyplot as plt
from PIL import Image
from cs3430_s24_hw09 import *
from bin_id3 import bin_id3
from prng import *
from seqrand import *

### =================== Problem 1 =============================

def fourier_coeffs(f, num_coeffs=10, a=-math.pi, b=math.pi, romb=7):
    acoeffs, bcoeffs = [], []
    for i in range(num_coeffs):
        fcos = lambda x: f(x)*math.cos(i*x)
        ai = rmb.R_j_l(fcos, a, b, romb, romb)/math.pi
        acoeffs.append(ai)
        if i > 0:
            fsin = lambda x: f(x)*math.sin(i*x)
            bi = rmb.R_j_l(fsin, a, b, romb, romb)/math.pi
            bcoeffs.append(bi)

    return acoeffs, bcoeffs

### =================== Problem 2 =============================

def nth_partial_sum(x, acoeffs, bcoeffs):
    assert len(acoeffs) == len(bcoeffs)+1

    partialSum = nth_partial_sum_of_fourier_series(x, acoeffs, bcoeffs)

    return partialSum

def plot_function_and_nth_partial_sum(f, f_def_str, num_coeffs=10, num_points=1000,
                                      a=-math.pi, b=math.pi, romb=7):

    acos, bsin = fourier_coeffs(f, num_coeffs, a, b, romb=romb)

    xvals = np.linspace(a, b, num_points)
    yvals1 = np.array([f(x) for x in xvals])
    yvals2 = np.array([nth_partial_sum(x, acos, bsin) for x in xvals])

    fig1 = plt.figure(1)
    fig1.suptitle("{}: num_coeff={}".format(f_def_str, num_coeffs))
    plt.xlabel('x')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.xlim([a, b])
    plt.plot(xvals, yvals1, label="y=f(x)", c='r')
    plt.plot(xvals, yvals2, label='y=nth_partial_sum', c='b')        
    plt.legend(loc='best')
    plt.show()


### ================== Problem 4 ===========================

def gen_lcg(a, b, m, n, x0=0):

    lcg = prng.lcg(a, b, m, n, x0)()

    return lcg

### ================== Problem 5 ============================

def gen_xorshift_32(a, b, c, n, x0=1):
    
    xor = prng.xorshift(a, b, c, n, x0)()

    return xor
        
### ================== Problem 6 ============================

@staticmethod
def __get_byte(i, byte_index):
    i = int(i)
    return ((i >> (8 * byte_index)) % 256 + 256) % 256

@staticmethod
def __int_to_rgb(i):
    r = __get_byte(i, 0) / 255
    g = __get_byte(i, 1) / 255
    b = __get_byte(i, 2) / 255
    return [r, g, b]

def make_lcg_pix(a, b, m, n, seed=11235813):
    """
    returns an numpy array (i.e., np.array) of RGB 3-tuples extracted with 
    __int_to_rgb(i) from LCG random numbers generated with gen_lcg(a,b,m,n,x0=seed).
    """
    assert n > 0

    gen = gen_lcg(a, b, m, n, seed)

    array = np.array([next(gen) for _ in range(n)])

    img_data = np.zeros((n, 3))
        
    for i, j in enumerate(array):
        img_data[i] = __int_to_rgb(j)

    return img_data

def make_random_pil(pix, w, h, n, name='random_pil', save_flag=True):
    """
    makes a random PIL image and saves/shows it.
    """
    ## pix must be an np.array
    assert isinstance(pix, np.ndarray)
    img_pix = pix.reshape(h, w, 3)
    pil_img = Image.fromarray(img_pix, 'RGB')
    if save_flag:
        pil_img.save(name + '.png')
    else:
        pil_img.show()

### ========================== Problem 07 =======================================        

def make_xorshift_32_pix(a, b, c, n, seed=1):
    """
    returns an numpy array, i.e., np.array, of RGB 3-tuples extracted with 
    __int_to_rgb(i) from 32-bit XORShift random numbers generated with 
    gen_xorshift_32().
    """
    assert n > 0

    gen = gen_xorshift_32(a, b, c, n, seed)

    array = np.array([next(gen) for _ in range(n)])

    img_data = np.zeros((n, 3))
        
    for i, j in enumerate(array):
        img_data[i] = __int_to_rgb(j)

    return img_data

### ========================= Problem 08 =======================================

def make_equal_probs_table(lower=1, upper=2):
    """
    ranges from lower to upper in increments from 1 and
    assings the probability of 1/(upper-lower+1) to each
    number in the range.
    """
    nums = [i for i in range(lower, upper+1)]
    n = upper - lower + 1
    probs = {}
    for x in nums:
        probs[x] = 1/n
    return probs

def get_coin_flip_seqs(num_coin_flips):
    assert num_coin_flips > 0

    def generate_outcomes(prefix, flips_left):
        if flips_left == 0:
            outcomes.append(prefix)
        else:
            generate_outcomes(prefix + '1', flips_left - 1)
            generate_outcomes(prefix + '2', flips_left - 1)

    outcomes = []
    generate_outcomes('', num_coin_flips) 
    return outcomes

def get_coin_flip_seqs_aux(num_coin_flips):
    assert num_coin_flips >= 0
    # your code here
    """
    I wasn't sure what to implement for this functon since it wasn't mentioned in the 
    CS 3430: S24: Scientific Computing Takehome Exam 03 PDF?
    """
    def generate_outcomes(prefix, flips_left):
        if flips_left == 0:
            outcomes.append(prefix)
        else:
            generate_outcomes(prefix + '1', flips_left - 1)
            generate_outcomes(prefix + '2', flips_left - 1)

    outcomes = []
    generate_outcomes('', num_coin_flips) 
    return outcomes

def is_sufficiently_knuth_random(str_digit_seq, probs):
    assert 0 <= 0 < len(str_digit_seq) <= len(str_digit_seq)

    # calculate pval with chisquared
    substring = str_digit_seq[0:len(str_digit_seq)]
    sublen = len(substring)
    Y_counts = [substring.count(str(d)) for d in range(1, len(probs) + 1)]  
    E_counts = [sublen * probs[d] for d in range(1, len(probs) + 1)] 
    v, pv = scipy.stats.chisquare(Y_counts, E_counts)

    # if p-value is in [0.1, 0.9]) return true
    return 0.1 <= pv <= 0.9

def get_sufficiently_knuth_random_coin_flip_seqs(num_coin_flips):
    assert num_coin_flips > 0
    
    outcomes = get_coin_flip_seqs(num_coin_flips)
    pt = make_equal_probs_table(1,2)

    random = []

    for outcome in outcomes:
        if is_sufficiently_knuth_random(outcome, pt):
            random.append(outcome)

    return random


def get_insufficiently_knuth_random_coin_flip_seqs(num_coin_flips):
    assert num_coin_flips > 0
    
    outcomes = get_coin_flip_seqs(num_coin_flips)
    pt = make_equal_probs_table(1,2)

    notrandom = []

    for outcome in outcomes:
        if not is_sufficiently_knuth_random(outcome, pt):
            notrandom.append(outcome)

    return notrandom

### ========================= Problem 09 =======================================

def get_die_throw_seqs(num_die_throws):
    assert num_die_throws > 0

    def generate_outcomes(prefix, throws_left):
        if throws_left == 0:
            outcomes.append(prefix)
        else:
            for i in range(1, 7):
                generate_outcomes(prefix + str(i), throws_left - 1)

    outcomes = []
    generate_outcomes('', num_die_throws)
    return outcomes

def get_die_throw_seqs_aux(num_die_throws):
    assert num_die_throws >= 0    
    """
    I wasn't sure what to implement for this functon since it wasn't mentioned in the 
    CS 3430: S24: Scientific Computing Takehome Exam 03 PDF?
    """

    def generate_outcomes(prefix, throws_left):
        if throws_left == 0:
            outcomes.append(prefix)
        else:
            for i in range(1, 7):
                generate_outcomes(prefix + str(i), throws_left - 1)

    outcomes = []
    generate_outcomes('', num_die_throws)
    return outcomes

def get_sufficiently_knuth_random_die_throw_seqs(num_die_throws):
    assert num_die_throws > 0
    outcomes = get_die_throw_seqs(num_die_throws)
    pt = make_equal_probs_table(1,6)

    random = []

    for outcome in outcomes:
        if is_sufficiently_knuth_random(outcome, pt):
            random.append(outcome)

    return random

def get_insufficiently_knuth_random_die_throw_seqs(num_die_throws):
    assert num_die_throws > 0
    outcomes = get_die_throw_seqs(num_die_throws)
    pt = make_equal_probs_table(1,6)

    random = []

    for outcome in outcomes:
        if not is_sufficiently_knuth_random(outcome, pt):
            random.append(outcome)

    return random
        
### ========================= Problem 10 =======================================

def learn_bin_id3_dt(examples_file_path):
    # your code here
    exArray, colNames = bin_id3.parse_csv_file_into_examples(examples_file_path)
    attribs = set(colNames[1:])
    avt = bin_id3.construct_attrib_values_from_examples(exArray, colNames[1:])
    target_attrib = 'PlayTennis'
    root = bin_id3.fit(exArray, target_attrib, attribs, avt, False)

    return root

def display_bin_id3_dt(dtr):

    bin_id3.display_id3_node(dtr, '')

def gain(examples, target_attrib, attrib, avt):

    return bin_id3.gain(examples, target_attrib, attrib, avt)

def entropy(examples, target_attrib, avt):

    return bin_id3.entropy(examples, target_attrib, avt)

### ========================= Problem 11 =======================================

"""
Type your answers to Problem 11 below. Huffman Trees can be typeset as follows:

           {A,B}:2
            /\
           /  \
       {A}:1  {B}:1

Let's assume, in order to reduce typing, that a left branch always emits 0
and a right branch -- 1. Thus, in the above Huffman tree, encode(A) = 0 and
encode(B) = 1; decode(0) = A and decode(1) = B.

a) 

        
                {*,A,B,C}:4(n)
                    0/\1
                    /  \
                   /    \
          {*, A}:2n       {B,C}:2n  
           0/\1             0/\1
           /  \             /  \
       {*}:n  {A}:n     {B}:n  {C}:n

b) Endcode: 
    A = 01
    B = 10
    C = 11
    AB = 0110
    AC = 0111

c)
    A Huffman Tree will emit the same number of bits for each symbol if each of the k symbols is a leaf node eg it has no children.
    A Huffman tree emits the same number of bits for every symbol if and only if the number of symbols is 2n, n > 0. 
    If there is an odd number of nodes, a tree that emits the same number of bits for each symbol can be created by
    adding dummy nodes with the same frequencies in order to retain a balanced tree like I did above.  
"""

