#!/usr/bin/python

#################################################
# module: lambdifier.py
# description: a lambdfifier module of
# a tiny diff engine.
# bugs to vladimir kulyukin in canvas
#################################################

from const import const
from var   import var
from pwr   import pwr
from prod  import prod
from plus  import plus
from maker import maker

class lambdifier(object):

    @staticmethod
    def lambdify(ds):
        """convert a const/var/pwr/prod/plyus object to a Python function."""
        if isinstance(ds, const):
            return lambdifier.lambdify_const(ds)
        elif isinstance(ds, var):
            return lambdifier.lambdify_var(ds)
        elif isinstance(ds, pwr):
            return lambdifier.lambdify_pwr(ds)
        elif isinstance(ds, prod):
            return lambdifier.lambdify_prod(ds)
        elif isinstance(ds, plus):
            return lambdifier.lambdify_plus(ds)
        else:
            raise Exception('Unknown type of ds {}'.format(ds))

    @staticmethod
    def lambdify_const(ds):
        """convert a const object to Py function."""
        assert isinstance(ds, const)
        return lambda x: ds.get_val()

    @staticmethod
    def lambdify_var(ds):
        """convert a var object to Py function."""        
        assert isinstance(ds, var)
        return lambda x: x

    @staticmethod
    def lambdify_pwr(ds):
        """convert a pwr object to a Py function."""
        assert isinstance(ds, pwr)
        assert isinstance(ds.get_base(), var)
        assert isinstance(ds.get_deg(), const)
        def f(x):
            bf = lambdifier.lambdify(ds.get_base())
            df = lambdifier.lambdify(ds.get_deg())
            return bf(x)**df(x)
        return f
    
    @staticmethod
    def lambdify_prod(ds):
        """convert a prod object to Py function."""                
        assert isinstance(ds, prod)
        assert isinstance(ds.get_mult1(), const)
        assert isinstance(ds.get_mult2(), pwr)
        def f(x):
            f1 = lambdifier.lambdify(ds.get_mult1())
            f2 = lambdifier.lambdify(ds.get_mult2())
            return f1(x) * f2(x)
        return f
    
    @staticmethod
    def lambdify_plus(ds):
        """convert a binary plus object to a Py function."""
        assert isinstance(ds, plus)
        assert isinstance(ds.get_elt1(), const) or isinstance(ds.get_elt1(), prod) or isinstance(ds.get_elt1(), plus)
        assert isinstance(ds.get_elt2(), const) or isinstance(ds.get_elt2(), prod)

        f1 = lambdifier.lambdify(ds.get_elt1())
        f2 = lambdifier.lambdify(ds.get_elt2())
        
        def f(x):
            return f1(x) + f2(x)
        return f



    
    
