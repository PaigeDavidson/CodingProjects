##################################################
# module: rat.py
# description: simple class for mainpulating
# ratios (rats).
# ----------------------------------------
# bugs to vladimir kulyukin in Canvas.
###################################################

class rat(object):

    @staticmethod
    def gcd(a, b):
        """
        greatest commond divisor of a and b.
        """
        assert b > 0 or b < 0
        while b:
            q = a // b
            a, b = b, a % b
        return a

    @staticmethod
    def flip(r):
        """
        exchange the numerator and denominator of rat r.
        """
        assert isinstance(r, rat)
        assert r.get_n() > 0 or r.get_n() < 0
        return rat(r.get_d(), r.get_n())

    def __init__(self, n, d):
        """
        a rat consist of a numerator n and a denominator d.
        d cannot be 0.
        """
        assert d < 0 or d > 0
        gcd = rat.gcd(n, d)
        self.__n = n // gcd
        self.__d = d // gcd

    def get_n(self):
        """
        self rat returns its numerator.
        """
        return self.__n

    def get_d(self):
        """
        self rat returns its denominator.
        """
        return self.__d


    def add(self, r):
        """
        rat r is added to self rat to
        to give birth to a new sum rat.
        """
        assert isinstance(r, rat)
        new_rats_d = self.__d * r.get_d()
        new_rats_n = self.__n * r.get_d() + r.get_n() * self.__d
        d = rat.gcd(new_rats_n, new_rats_d)
        return rat(new_rats_n // d, new_rats_d // d)

    def mult(self, r):
        """
        rat r is multiplied with self rat to
        give birth to a new product rat.
        """
        assert isinstance(r, rat)
        new_rats_d = self.__d * r.get_d()
        new_rats_n = self.__n * r.get_n()
        d = rat.gcd(new_rats_n, new_rats_d)        
        return rat(new_rats_n // d, new_rats_d // d)

    def div(self, r):
        """
        self rat r is divided by rat r
        to give birth to a new quotient rat.
        """
        assert isinstance(r, rat)
        return self.mult(rat.flip(r))

    def __str__(self):
        """
        self rat gets linearized as a string.
        """
        return str(self.__n) + "/" + str(self.__d)
