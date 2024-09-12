###############################################
# module: dra.py
# DRA abbreviates "differentiation rules
# applier."
# bugs to vladimir kulyukin in canvas.
###############################################

import numpy as np
from  const import const
from  var   import var
from  pwr   import pwr
from  prod  import prod
from  plus  import plus
from  maker import maker

class dra(object):
    ## ds abbreviates "data structure."
    ## diff is the top-level method
    ## that dispatches on specific cases
    ## depending on the type of ds.
    @staticmethod
    def diff(ds):
        if isinstance(ds, const):
            return dra.diff_const(ds)
        elif isinstance(ds, var):
            return dra.diff_var(ds)
        elif isinstance(ds, pwr):
            return dra.diff_pwr(ds)
        elif isinstance(ds, pwr):
            return dra.diff_const(ds)
        elif isinstance(ds, prod):
            return dra.diff_prod(ds)
        elif isinstance(ds, plus):
            return dra.diff_plus(ds)
        else:
            raise Exception('dra.diff({})'.format(str(ds)))

    @staticmethod
    def diff_const(ds):
        assert isinstance(ds, const)
        return maker.make_const(0.0)

    @staticmethod
    def diff_var(ds):
        assert isinstance(ds, var)
        return maker.make_const(1.0)

    @staticmethod
    def diff_pwr(ds):
        """ differentiate a pwr object """
        assert isinstance(ds, pwr)

        variable = ds.get_base()
        exponent = ds.get_deg()

        assert isinstance(variable, var)
        assert isinstance(exponent, const)

        # If the exponent is zero, return a constant with value 0.0
        if np.allclose(exponent.get_val(), 0.0):
            return maker.make_const(0.0)
        
        # Otherwise, differentiate the power rule
        else:
            updated_exponent = exponent.get_val() - 1

            new_power =  maker.make_pwr(variable.get_name(), updated_exponent)

            return maker.make_prod(maker.make_const(exponent.get_val()), new_power)
            

    @staticmethod
    def diff_prod(ds):
        """ differentiate a product object """
        assert isinstance(ds, prod)
        m1 = ds.get_mult1()
        m2 = ds.get_mult2()
        assert isinstance(m1, const)
        assert isinstance(m2, pwr)
        if np.allclose(m1.get_val(), 0.0):
            return maker.make_const(0.0)
        elif np.allclose(m2.get_deg().get_val(), 0.0):
            return maker.make_const(0.0)
        else:
            pwr_drv = dra.diff_pwr(m2)
            #print('pwr_drv = {}'.format(pwr_drv))
            assert isinstance(pwr_drv, const) or isinstance(pwr_drv, prod)
            if isinstance(pwr_drv, const):
                return pwr_drv
            elif isinstance(pwr_drv, prod):
                coeff = m1.get_val() * pwr_drv.get_mult1().get_val()
                return maker.make_prod(maker.make_const(coeff),
                                       maker.make_pwr(pwr_drv.get_mult2().get_base().get_name(),
                                                      pwr_drv.get_mult2().get_deg().get_val()))
            else:
                raise Exception('dra.diff_prod({})'.format(str(ds)))

    @staticmethod
    def diff_plus(ds):
        """ differentiate a plus object """
        assert isinstance(ds, plus)
        m1 = ds.get_elt1()
        m2 = ds.get_elt2()
        assert isinstance(m1, const) or isinstance(m1, prod) or isinstance(m1, plus)
        assert isinstance(m2, const) or isinstance(m2, prod)
        return maker.make_plus(dra.diff(m1), dra.diff(m2))
