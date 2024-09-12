#!/usr/bin/python

###########################################
# module: maker.py
# a factor class to generate const, var,
# pwr, prod, and sum objects.
# bugs to vladimir dot kulyukin in canvas
###########################################

from const import const
from var import var
from pwr import pwr
from prod import prod
from plus import plus

class maker(object):

    @staticmethod
    def make_var(var_name):
        assert isinstance(var_name, str)
        return var(var_name)

    @staticmethod
    def make_const(val):
        assert isinstance(val, float)
        return const(val)

    @staticmethod
    def make_pwr(var_name, d):
        assert isinstance(var_name, str)
        assert isinstance(d, float) 
        return pwr(maker.make_var(var_name), maker.make_const(d))

    @staticmethod
    def make_prod(mult1, mult2):
        assert isinstance(mult1, const)
        assert isinstance(mult2, pwr)
        return prod(mult1, mult2)

    @staticmethod
    def make_plus(elt1, elt2):
        assert isinstance(elt1, const) or isinstance(elt1, prod) or isinstance(elt1, plus)
        assert isinstance(elt2, const) or isinstance(elt2, prod)
        return plus(elt1, elt2)


