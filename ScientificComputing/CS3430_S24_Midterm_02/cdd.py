#####################################################
# module: cdd.py
# description: Python implementations of some of the
# central divided difference (CDD) formulas
# from Ch. 6 in "Numerical Methods Using MATLAB"
# 4th edition by J. Mathews and K. Fink.
# The PDF of the relevant sections of
# this chapter is included in the zip archive
# of this assignment. I also included it
# in the zip archive of Lecture 12 in Canvas when
# we discussed CDD for the first time.
# ---------------------------------------------
# bugs to vladimir kulyukin in canvas
######################################################

import numpy as np

class cdd(object):

    ### --- CDD of First and Second Derivatives Order 2 ----
    @staticmethod
    def drv1_ord2(f, x, h):
        """
        An implementation of formula 1 in Table 6.3, p. 339 in 
        CDD.pdf. This formula uses CDD to approximate
        f'(x), i.e., derivative 1 (hence drv1 in the name of
        the method), and the estimated error of the approximation
        is O(h^2), where h is the stepsize. Hence, order 2 (ord2) 
        in the name of the method.
        f is a Python function of 1 argument; x is the value
        where we estimate f'(x); h is the step size.
        """
        #f`(x0) = (f(x+h)-f(x-h))/(2h)
        num = f(x+h) - f(x-h)
        denom = 2 * h
        return np.longdouble(num/denom)

    @staticmethod
    def drv2_ord2(f, x, h):
        """
        An implementation of formula 2 in Table 6.3, p. 339 in 
        CDD.pdf. This formula uses CDD to approximate
        f''(x), i.e., derivative 2 (hence drv2 in the name of
        the method), and the estimated error of the approximation
        is O(h^2), where h is the stepsize. Hence, order 2 (ord2) 
        in the name of the method.
        f is a Python function of 1 argument; x is the value
        where we estimate f''(x); h is the step size.
        """
        #f``(x0) = (f(x+1)-2f(0)+f(x-h))/h^2
        a = f(x+h)
        b = 2 * f(x)
        c = f(x-h)
        numer = a - b + c
        denom = h ** 2
        return np.longdouble(numer / denom)

    ### --- CDD of First and Second Derivatives Order 4 ----    
    @staticmethod
    def drv1_ord4(f, x, h):
        """
        An implementation of formula 1 in Table 6.4, p. 339 in 
        CDD.pdf. This formula uses CDD to approximate
        f'(x), i.e., derivative 1 (hence drv1 in the name of
        the method), and the estimated error of the approximation
        is O(h^4), where h is the stepsize. Hence, order 4 (ord4) 
        in the name of the method.
        f is a Python function of 1 argument; x is the value
        where we estimate f'(x); h is the step size.
        """
        # f`(x0)=(-f(x+2h)+8f(x+h) - 8f(x-h)+ f(x-2h))/12h
        # f`(x) = a + b - c + d / denom
        a = -1 * f(x + (2 * h))
        b = 8 * f(x + h)
        c = 8 * f(x-h)
        d = f(x - (2 * h))

        numer = a + b - c + d
        denom = 12 * h

        return np.longdouble(numer/denom)


    @staticmethod
    def drv2_ord4(f, x, h):
        """
        An implementation of formula 2 in Table 6.4, p. 339 in 
        CDD.pdf. This formula uses CDD to approximate
        f''(x), i.e., derivative 2 (hence drv2 in the name of
        the method), and the estimated error of the approximation
        is O(h^4), where h is the stepsize. Hence, order 4 (ord4) 
        in the name of the method.
        f is a Python function of 1 argument; x is the value
        where we estimate f''(x); h is the step size.
        """
        #f``(x0) = (-f(x+2h) + 16f(x+h) - 30f(0) + 16f(x-h) = f(x-2h))/12h^2
        a = -1 * f(x + (2 * h))
        b = 16 * f(x+h)
        c = 30 * f(x)
        d = 16 * f(x-h)
        e = f(x - (2 * h))

        numer = a + b - c + d - e
        denom = 12 * (h ** 2)

        return np.longdouble(numer / denom)


    

    

    

    
        
    
