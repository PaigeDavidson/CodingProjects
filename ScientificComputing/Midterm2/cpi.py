
#########################################
# module: cpi.py
# description: Pi approximation with the
# Chudnovsky algorithm.
# ----------------------------------------
# bugs to vladimir kulyukin in Canvas.
#########################################

import decimal
import math

class cpi(object):

    C_1 = 426880 * math.sqrt(10005)
    C_2 = 13591409
    C_3 = 10939058860032000
    C_4 = 545140134

    @staticmethod
    def binary_split(a, b):
        """
        do the binary splitting of the inteval [a,b] for
        the Chudnovsky algorithm.
        """

        C_2 = cpi.C_2
        C_3 = cpi.C_3
        C_4 = cpi.C_4

        # IF a == b + 1 ## this is the base case: unit interval no need to split.
        if b == a + 1:
            Pab = -(6*a-1)*(2*a-1)*(6*a-5)  # Corrected multiplication operators
            Qab = cpi.C_3 * (a**3)
            Rab = Pab * (cpi.C_4 * a + cpi.C_2)
        # ELSE ## this is the recursive case
        else:
            m = (a + b) // 2 ## we split in the middle and
            Pam, Qam, Ram = cpi.binary_split(a, m) ## 1) recurse on [a,m]
            Pmb, Qmb, Rmb = cpi.binary_split(m, b) ## 2) recurse on [m,b]

            ## we assemble the results by multiplying P’s and Q,s
            ## and computing the R.
            Pab = Pam * Pmb
            Qab = Qam * Qmb
            Rab = Qmb * Ram + Pam * Rmb

        return Pab, Qab, Rab


    @staticmethod
    def arx_real(n, prec=10):
        """
        approximate (arx) the real value of pi by binary splitting on the interval [1, n], n>1,
        with the Chudnovsky algorithm at a given value of precision prec.
        """
        #CHUDNOVSKY_PI(1, n)
        # ASSERT n > 1
        # P1n, Q1n, R1n = BINARY_SPLIT(1, n)
        # RETURN (C_1 * Q1n) / (C_2 * Q1n + R1n)

        C_1 = cpi.C_1
        C_2 = cpi.C_2

        assert n > 1
        decimal.getcontext().prec=prec  
        P1n, Q1n, R1n = cpi.binary_split(1, n)  

        # convert to decimal so you don't get an overflow error
        c1 = decimal.Decimal(C_1)
        q1 = decimal.Decimal(Q1n)
        c2 = decimal.Decimal(C_2)
        r1 = decimal.Decimal(R1n)

        return (c1 * q1) / (c2 * q1 + r1)

