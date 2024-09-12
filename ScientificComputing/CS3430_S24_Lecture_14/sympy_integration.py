########################################
# module: sympy_intergration.py
# sympy integration values for
# Example 1 (cf. Slide 7) and
# Example 2 (cf. Slide 16) in
# Lecture 14 PDF.
# bugs to vladimir kulyukin in Canvas
########################################

import sympy as sp
from sympy import symbols
from sympy.utilities import lambdify
import numpy as np

x = symbols('x')
### 1. integrate the function
intf =  sp.integrate(5*x*sp.exp(-2.0*x), x)
### 2. lambidfy the function
lintf = lambdify((x), intf)
### 3. evaluate the definition integrate on
###    [0.1, 1.3]
sp_int_val = lintf(1.3) - lintf(0.1)
### sympy_integral_value = 0.8938650276524703
print('sp_int_val = {}'.format(sp_int_val))

t = symbols('t')
### 1. integrate the function
intf2 =  sp.integrate(2000*sp.ln(140000.0/(140000 - 2100*t)) - 9.8*t)
### 2. lambdify the function
lintf2 = lambdify((t), intf2)
### 3. evaluate the integral on [8, 30].
sp_int_val = lintf2(30) - lintf2(8)
print('sp_int_val = {}'.format(sp_int_val))
print('sp_int_val = {}'.format(np.longdouble(sp_int_val)))
