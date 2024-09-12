#################################################
# module: ecf.py
# description: approximation of the number
# E with the continued fraction (cf) on Slide 6
# in Lecture 16.
# ----------------------------------------
# bugs to vladimir kulyukin in Canvas.
##################################################

from rat import rat
import decimal

class ecf(object):

    @staticmethod
    def N_i(i):
        assert i > 0
        """ 
        the i-th numerator in the continued fraction for
        e on Slide 6 in Lecture 16.
        """
        return 1
        

    @staticmethod
    def D_i(i):
        """ 
        the i-th denominator in the continued fraction for
        e on Slide 6 in Lecture 16.
        """
        # 1, 2, 1, 1, 4, 1, 1, 6
        if i == 1 or i == 2:
            return i
        else:
            i = i-2
            if i % 3 == 0:
                return (i // 3) * 2 + 2
            else: return 1


    @staticmethod
    def cf_rat(i):
        """
        The ratio component of the continued fraction of
        e on Slide 6 in Lecture 16.
        """
        if i == 0:
            return rat(0, 1)

        # Initialize the numerator and denominator
        num = rat(ecf.N_i(1), 1)
        den = rat(ecf.D_i(1), 1)

        # Initialize the ratio with the first fraction
        fraction = rat(0, 1)

        for j in range(i, 1, -1):
            next_num = rat(ecf.N_i(j), 1)
            next_den = rat(ecf.D_i(j), 1)

            # Compute the new fraction
            newden = next_den.add(fraction)
            
            fraction = next_num.div(newden)

        den = den.add(fraction)

        ratio = num.div(den)

        return ratio

    @staticmethod
    def arx_rat(i):
        """
        approximates (arx) e with the i-th continued fraction on Slide 6
        in Lecture 16 computed as a ratio (rat).
        """
        z = ecf.cf_rat(i)
        const = rat(2, 1)

        return z.add(const)

    @staticmethod
    def arx_real(i, prec=20):
        """
        approximates (arx) e with the i-th continued fraction on Slide 6
        in Lecture 16 computed as a real.
        """
        z = ecf.cf_rat(i)
        const = rat(2, 1)
        num = z.add(const)

        decimal.getcontext().prec = prec

        top = decimal.Decimal(num.get_n())
        bot = decimal.Decimal(num.get_d())

        frac = top / bot

        return frac
