#!/usr/bin/python

#########################################
# module: prod.py
# a representation of ax^r, where where
# x^r is a pwr object (see pwr.py)
# and a and r are consts (see const.py)
# a is multiplicand 1 and x^r is
# multiplicand 2.
# bugs to vladimir kulyukin in canvas.
#########################################

class prod(object):
    def __init__(self, mult1=None, mult2=None):
        self.__mult1__ = mult1
        self.__mult2__ = mult2

    def get_mult1(self):
        return self.__mult1__

    def get_mult2(self):
        return self.__mult2__

    def __str__(self):
        return '(' + str(self.__mult1__) + '*' + str(self.__mult2__) + ')'
