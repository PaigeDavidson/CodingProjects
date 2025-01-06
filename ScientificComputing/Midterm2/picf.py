##################################################
# module: picf.py
# description: approximation of the number
# pi with the continued fraction (cf) on Slide 7
# in Lecture 16.
# ----------------------------------------
# bugs to vladimir kulyukin in Canvas.
###################################################

from rat import rat
import decimal

class picf(object):

    @staticmethod
    def N_i(i):
        """ 
        the i-th numerator in the continued fraction for
        pi on Slide 7 in Lecture 16.
        """
        # i starts at 1 and increments by 2
        # i is always squared
        num = 1
        if i == 1:
            return i
        else: 
            num = ((2 * i) - 1)
            return (num ** 2)

    @staticmethod
    def D_i(i):
        """ 
        the i-th denominator in the continued fraction for
        pi on Slide 7 in Lecture 16.
        """
        return 6

    @staticmethod
    def cf_rat(i):
        """
        The ratio component of the continued fraction of
        pi on Slide 7 in Lecture 16.
        """
        if i == 0:
            return rat(0, 1)

        # Initialize the numerator and denominator
        num = rat(picf.N_i(1), 1)
        den = rat(picf.D_i(1), 1)

        # Initialize the ratio with the first fraction
        fraction = rat(0, 1)

        for j in range(i, 1, -1):
            next_num = rat(picf.N_i(j), 1)
            next_den = rat(picf.D_i(j), 1)

            # Compute the new fraction
            newden = next_den.add(fraction)

            fraction = next_num.div(newden)

        den = den.add(fraction)

        ratio = num.div(den)

        return ratio

    @staticmethod
    def arx_rat(i):
        """
        approximates (arx) pi with the i-th continued fraction on Slide 7
        in Lecture 16 computed as a ratio (rat).
        """
        z = picf.cf_rat(i)
        const = rat(3, 1)

        return z.add(const)

    @staticmethod
    def arx_real(i, prec=20):
        """
        approximates (arx) pi with the i-th continued fraction on Slide 7
        in Lecture 16 computed as a real.
        """
        decimal.getcontext().prec = prec

        z = picf.cf_rat(i)
        const = rat(3, 1)
        num = z.add(const)

        top = decimal.Decimal(num.get_n())
        bot = decimal.Decimal(num.get_d())

        frac = top / bot

        return frac

    
    
