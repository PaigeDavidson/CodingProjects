#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: cs3430_s24_midterm02.py
# Paige Davidson
# A02339245
# WRITE THE TIME IT TOOK YOU TO COMPLETE THIS EXAM.
# 3 hours
##############################################################

### put your imports from your previous/current assignments.
### These are the imports that I used to implement my solutions.
### Modify these as you see fit.
"""
from   tiny_de     import tiny_de     ## homework 05
from   nra import nra                 ## homework 05
from   cs3430_s24_hw06 import *       ## homework 06
from   cdd import cdd                 ## homework 07
from   rmb import rmb                 ## homework 07
from   rxp import rxp                 ## homework 07
from   rat import rat                 ## homework 08
from   picf import picf               ## homework 08
from   ecf  import ecf                ## homework 08
from   cpi import cpi                 ## homework 08
import sympy
import sympy.utilities
import math
from PIL import Image
import decimal
"""

from   tiny_de import tiny_de    ## homework 05
from   nra import nra            ## homework 05
import   cs3430_s24_hw06           ## homework 06
from   cdd import cdd                ## homework 07
from   rmb import rmb                 ## homework 07
from   rxp import rxp                ## homework 07
from   rat import rat                ## homework 08
from   picf import picf               ## homework 08
from   ecf  import ecf                ## homework 08
from   cpi import cpi                 ## homework 08
import sympy
import sympy.utilities
import math
from PIL import Image
import decimal


### ================ Problem 01 ========================

def diff_file(file_path):
    tde = tiny_de()
    diffList = tde.lambdify_diff_file(file_path)
    return diffList

### ================ Problem 02 ========================

def zero_root(poly_text, num_iters=5):
    return nra.zr1(poly_text, 1.0, num_iters)

### ================ Problem 03 =========================

def detect_pil_edge_pixels(in_imgpath, out_imgpath, default_delta=1.0, magn_thresh=20):
    input  = Image.open(in_imgpath)
    output = cs3430_s24_hw06.dex_pil(input, default_delta, magn_thresh)
    output.save(out_imgpath)


### ================ Problem 04 =========================

def cdd_drv1_ord2(f, x, h):
    return cdd.drv1_ord2(f, x, h)

def cdd_drv1_ord4(f, x, h):
    return cdd.drv1_ord4(f, x, h)

### ================ Problem 05 =========================

def cdd_drv2_ord2(f, x, h):
    return cdd.drv2_ord2(f, x, h)

def cdd_drv2_ord4(f, x, h):
    return cdd.drv2_ord4(f, x, h)

### ================ Problem 06 =========================

def romberg_integral(f, a, b, j, l):
    return rmb.R_j_l(f, a, b, j, l)

### ================ Problem 07 =========================

def richardson_2(av_2n, av_n):
    return rxp.r2(av_2n, av_n)

### ================ Problem 08 =========================

def e_cont_frac_rat(i):
    assert i >= 0
    return ecf.arx_rat(i)

def e_cont_frac_real(i, prec=20):
    assert i >= 0
    decimal.getcontext().prec=prec
    return ecf.arx_real(i, prec)

### ================  Problem 09 =========================

def pi_cont_frac_rat(i):
    assert i >= 0
    return picf.arx_rat(i)

def pi_cont_frac_real(i, prec=20):
    assert i >= 0
    decimal.getcontext().prec=prec
    return picf.arx_real(i, prec)

### ================= Problem 10 ==========================

def chudnovsky_pi(n, prec=20):
    return cpi.arx_real(n, prec)


