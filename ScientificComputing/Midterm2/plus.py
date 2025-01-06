#!/usr/bin/python

##################################################################################################
# module: plus.py
# We represent polynomials with arbirarily many binary sums. A binary sum has exactly 2 summands
# referred to as element 1 (elt1) and element 2 (elt2). In the simplest case, a polynomial is
# just one product, e.g., \verb|'5x^2'| or \verb|'10x^-2'|. Then,
# we can build a polynomial out of 2 product objects. If we need 3 product
# objects in a polynomial, we use one binary sum for the first two
# product objects to make a binary sum and then use another binary sum with
# the first binary sum and the third product object. Then,
# inductively, on to 4 products, 5, etc. 
# bugs to vladimir kulyukin via canvas.
####################################################################################################

class plus(object):
    def __init__(self, elt1=None, elt2=None):
        self.__elt1__ = elt1
        self.__elt2__ = elt2

    def get_elt1(self):
        return self.__elt1__

    def get_elt2(self):
        return self.__elt2__

    def __str__(self):
        return '(' + str(self.__elt1__) + '+' + str(self.__elt2__) + ')'
