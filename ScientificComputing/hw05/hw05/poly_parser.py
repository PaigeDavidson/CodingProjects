#!/usr/bin/python

#################################################
# module: poly_parser.py
# description: a parser that converts texts to
# polynomial sums or single product objects.
# bugs to vladimir dot kulyukin dot usu dot edu
#################################################

from maker import maker

class poly_parser(object):

    @staticmethod
    def parse_elt(elt):
        # let's make sure that elt is a string.
        assert isinstance(elt, str)
        cari = 0
        try:
            cari = elt.index('^')
        except ValueError:
            raise Exception('^ is not in ()'.format(elt))
        var_name = elt[cari-1:cari]
        a_val    = float(elt[:cari-1])
        r_val    = float(elt[cari+1:])
        a = maker.make_const(a_val)
        p = maker.make_pwr(var_name, r_val)
        return maker.make_prod(a, p)

    @staticmethod
    def parse_sum(poly_str):
        assert isinstance(poly_str, str)
        elts_and_signs = poly_str.split()
        if len(elts_and_signs) == 1:
            return poly_parser.parse_elt(elts_and_signs[0])
        elts = poly_parser.assoc_signs(elts_and_signs)
        #print('elts={}'.format(elts))
        if len(elts) == 2:
            return maker.make_plus(poly_parser.parse_elt(elts[0]),
                                   poly_parser.parse_elt(elts[1]))
        elif len(elts) > 2:
            parsed_sum = maker.make_plus(poly_parser.parse_elt(elts[0]),
                                         poly_parser.parse_elt(elts[1]))
            for i in range(2, len(elts)):
                parsed_sum = maker.make_plus(parsed_sum,
                                             poly_parser.parse_elt(elts[i]))
            return parsed_sum

    @staticmethod
    def assoc_signs(elts_and_signs):
        assert len(elts_and_signs) >= 1
        assert len(elts_and_signs) % 2 != 0
        rslt = [elts_and_signs[0]]
        for i in range(len(elts_and_signs)-1):
            if elts_and_signs[i] == '+':
                rslt.append(elts_and_signs[i+1])
            elif elts_and_signs[i] == '-':
                rslt.append('-' + elts_and_signs[i+1])
        return rslt

    
        
        

    
        
        
