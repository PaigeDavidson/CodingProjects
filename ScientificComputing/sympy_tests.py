#######################################
# module: sympy_tests.py
# description: sample uses of sympy
# bugs to vladimir kulyukin in canvas
#######################################

from sympy              import symbols
from sympy.utilities    import lambdify
from sympy.core.symbol  import Symbol
from sympy.core.add     import Add
from sympy.core.numbers import Float
from sympy.core.numbers import Zero
import numpy as np

### ============= Differentiation with SymPy =====================

### define x to be a Symbol
x = symbols('x')
assert isinstance(x, Symbol)

### define a polynomial object
f = 10.0*x**3 - 5*x**2 + 10.0*x + 500.0
### next line prints out 'f = 10.0*x**3 - 5*x**2 + 10.0*x + 500.0'
print('f = {}'.format(f))
assert isinstance(f, Add)

### let's compute 1st derivative
df1 = f.diff()
### the next line prints out 'df1 = 30.0*x**2 - 10*x + 10.0'
print('df1 = {}'.format(df1))
assert isinstance(df1, Add)

### let's compute 2nd derivative
df2 = df1.diff()
### the next line prints out 'df2 = 60.0*x - 10'
print('df2 = {}'.format(df2))
assert isinstance(df2, Add)

### let's compute 3rd derivative
df3 = df2.diff()
### the next line prints out 'df3 = 60.0000000000000'
print('df3 = {}'.format(df3))
assert isinstance(df3, Float)

### let's compute 4th derivative
df4 = df3.diff()
### the next line prints out 'df4 = 0'
print('df4 = {}'.format(df4))
assert isinstance(df4, Zero)

### ============= Lambdification with SymPy =====================

### let's lambdify the original polynomial
### and evaluate it at 1.
lf = lambdify((x), f)
# lf(1) = 10.0*1**3 - 5*1**2 + 10.0*1 + 500.0 = 515
assert np.allclose(lf(1), 515)

### let's lambdify 1st derivative and evaluate it
### at 1.
ldf1 = lambdify((x), df1)
### ldf1(1) = 30.0*1**2 - 10*1 + 10.0 = 30
assert np.allclose(ldf1(1), 30)

### let's lambdify 2nd derivative and evaluate it
### at 1.
ldf2 = lambdify((x), df2)
### ldf2(1) = 60.0*1 - 10
assert np.allclose(ldf2(1), 50)

### let's lambdify 3rd derivative and evaluate it
### at 1.
ldf3 = lambdify((x), df3)
### ldf3(x) = 60.0 for all x.
for i in range(1000):
    assert np.allclose(ldf3(i), 60)

### let's lambdify 4th derivative and evaluate it
### at 1.
ldf4 = lambdify((x), df4)
### ldf4(x) = 0 for all x.
for i in range(1000):
    assert np.allclose(ldf4(i), 0)

### define a polynomial object
my_f = 5*x**-3
### next line prints out 'my_f = 10.0*x**3 - 5*x**2 + 10.0*x + 500.0'
print('my_f = {}'.format(my_f))
my_drv1 = my_f.diff()
print('my_drv1 = {}'.format(my_drv1))
my_drv2 = my_drv1.diff()
print('my_drv2 = {}'.format(my_drv2))

    










