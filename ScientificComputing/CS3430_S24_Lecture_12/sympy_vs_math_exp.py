########################################################
# module: sympy_vs_math_exp.py
# description: examples for CS3430: S24: Lecture 12
# bugs to vladimir kulyukin in canvas.
########################################################

import sympy as sp
import numpy as np
import math
from sympy           import symbols
from sympy.utilities import lambdify

### ================ Example 1 =========================

x = symbols('x')
f = 5.0*sp.exp(2.5*x)
df = f.diff()
ldf = lambdify((x), df)
sav = ldf(1.0)
mav = 12.5*math.e**(2.5*1.0)
nav = 12.5*np.exp(2.5*1.0)

print('sympy av = {}'.format(sav))
print('math  av = {}'.format(mav))
print('numpy av = {}'.format(nav))

assert np.allclose(sav, mav) and np.allclose(sav, nav)
assert sav == nav
## this assertion fails
## assert sav == mav or nav == mav

### ================ Example 2 =========================

num2 = sp.sin((sp.sqrt(x**2 + x)) / (sp.cos(x) - x))**2
dnm2 = sp.sin((sp.sqrt(x) - 1) / (sp.sqrt(x**2 + 1)))
f2   =  num2 / dnm2
df2  = f2.diff()
ldf2 = lambdify((x), df2)
sav2 = ldf2(0.05)
print('sav2 = {}'.format(sav2))






