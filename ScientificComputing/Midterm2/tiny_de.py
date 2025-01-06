#!/usr/bin/python

#################################################
# module: tiny_de.py
# description: a a tiny diffirentiation engine (de).
# bugs to vladimir kulyukin in canvas
#################################################

from poly_parser import poly_parser
from lambdifier  import lambdifier
from dra         import dra

class tiny_de(object):

    def parse(self, text):
        """parse text into a const/var/pwr/prod/plus object."""
        return poly_parser.parse_sum(text)

    def lambdify(self, ds):
        """convert a data structure ds to Py function."""
        return lambdifier.lambdify(ds)

    def diff(self, ds):
        """differentiate a data structure ds."""
        return dra.diff(ds)

    def parse_file(self, file_path):
        """
        return a list of data structures from polynimals in a file file_path.
        the file contains one polynomial text per line
        """
        with open(file_path, 'r') as inf:
            return [self.parse(ln) for ln in inf.readlines()
                    if len(ln) > 0]

    def lambdify_file(self, file_path):
        """
        returns a list of lambdified polynomials given in a file file_path.
        """
        with open(file_path, 'r') as inf:
            return [self.lambdify(self.parse(ln)) for ln in inf.readlines()
                    if len(ln) > 0]            

    def lambdify_diff_file(self, file_path):
        """
        returns a list of lambdified differentiated polynomials in a file file_path.
        """
        with open(file_path, 'r') as inf:
            return [self.lambdify(self.diff(self.parse(ln))) for ln in inf.readlines()
                    if len(ln) > 0]

    
    
