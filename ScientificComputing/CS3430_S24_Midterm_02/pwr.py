#!/usr/bin/python

#############################################
# module: pwr.py
# a representation of a power object;
# a power object is x^r, where x is
# a variable (see var.py) and r is
# a real const (see const.py).
# in a power object x^r, x is the base
# and r is the degree.
# bugs to vladimir kulyukin in canvas
#############################################

class pwr(object):
    def __init__(self, base=None, deg=None):
        self.__base__ = base
        self.__deg__  = deg

    def get_base(self):
        return self.__base__

    def get_deg(self):
        return self.__deg__

    def __str__(self):
        return '(' + str(self.__base__) + '^' + str(self.__deg__) + ')'
