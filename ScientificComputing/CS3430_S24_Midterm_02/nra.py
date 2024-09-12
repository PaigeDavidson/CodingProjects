
#############################################
# Module: nra.py
# Description: Newton-Raphson Algorithm
# bugs to vladimir kulyukin in canvas.
#############################################

import numpy as np
import math
from tiny_de import tiny_de

class nra(object):

    # 2 stopping conditions

    @staticmethod
    def zr1(text, x0, num_iters=3):
        #  create instance of the tiny_de class
        de = tiny_de()
        # find the function ds
        poly = de.parse(text)
        # initialize xn to the first approximation
        xn = x0
        # when we hit the number of iterations, return
        for _ in range(num_iters):
            f = de.lambdify(poly)
            fPrime = de.lambdify(de.diff(poly))

            xn = xn - f(xn) / fPrime(xn)

        return xn
        

    @staticmethod
    def zr2(text, x0, delta=0.0001):
         #  create instance of the tiny_de class
        de = tiny_de()
        # find the function ds
        poly = de.parse(text)
        # initialize xn to the first approximation
        xn = x0
        # initialize difference 
        difference = math.inf
        num_iterations = 0
        # if we either hit the desired error level exit loop and return
        while abs(difference) > delta:
            f = de.lambdify(poly)
            fPrime = de.lambdify(de.diff(poly))

            difference = xn - (xn - f(xn) / fPrime(xn))
            xn = xn - f(xn) / fPrime(xn)
            num_iterations += 1
            
        return xn, num_iterations

    @staticmethod
    def check_zr(text, zr):
        tde = tiny_de()
        f = tde.lambdify(tde.parse(text))
        return np.allclose(f(zr), 0.0)
