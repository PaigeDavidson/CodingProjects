#######################################
# module: rmb.py
# description: Romberg Intergration
# ---------------------------------
# bugs to vladimir kulyukin in Canvas
#######################################

import numpy as np
import math

class rmb(object):

    ### The formula is on Slide 08 in Lecture 13 PDF.
    @staticmethod
    def T_k_1(f, a, b, k):
        """
        Trapezoidal Rule of Definite Integral Approximation.
        f is a function; 
        a is the lower boundary of the interval;
        b is the upper boundary of the interval; 
        k is such that n = 2**(k-1), where n is the number of sub-intervals into 
          [a,b] is  partitioned;
        it defines the number of intervals (e.g., k=0, then n=1, k=1, n=2, etc.)
        """
        assert k > 0
        n = 2 ** (k-1)
        h = (b-a)/(2 * n)

        mySum = sum(f(a+i*(b-a)/n) for i in range(1, n))

        integralAprox = h * (f(a) + (2 * mySum) + f(b))

        return np.longdouble(integralAprox)
    
    @staticmethod
    def R_j_1(f, a, b, j):
        assert j > 0
        n = 2 ** (j-1)
        h = (b-a)/(2 * n)

        mySum = sum(f(a+i*(b-a)/n) for i in range(1, n))

        integralAprox = h * (f(a) + (2 * mySum) + f(b))

        return np.longdouble(integralAprox)

    @staticmethod
    def R_j_l(f, a, b, j, l):
        """
        Computes the value at the node R[j,l] in the Romberg Lattice
        to approximate the definite integral of f over [a, b] according
        to the formula in Slide 23, Lecture 14.
        """    
        # Initialize the arrays for dynamic programming
        array1 = [rmb.T_k_1(f, a, b, k) for k in range(1, j + 1)]
        array2 = [0] * j  # Initialize array2 with zeros

        # Perform dynamic programming to compute Romberg lattice values
        for col_index in range(2, l + 1):
            for k in range(1, j):
                prev_value = array1[k]
                prev_prev_value = array1[k - 1]
                curr_value = prev_value + (prev_value - prev_prev_value) / ((4 ** (col_index - 1)) - 1)
                array2[k] = curr_value
            array1, array2 = array2, array1  # update array1 and array2

        # Return the value at node R[j,l]
        return array1[-1]

