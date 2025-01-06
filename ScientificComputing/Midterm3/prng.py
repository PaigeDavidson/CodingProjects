############################################
# module: prng.py
# description: pseudorandom number generator
#              for CS3430: S24: Assgnment 10
# YOUR NAME: Paige Davidson
# YOUR A-NUMBER: A02339425
#-------------------------------------------
# bugs to vladimir kulyukin in canvas
#############################################
from PIL import Image
import numpy as np
import matplotlib.colors as col
import random
import scipy.stats

class prng(object):

    @staticmethod
    def lcg(a, b, m, n, x0=0):
        """
        returns an lcg generator that generates n random numbers with linear congruential generator
        given a, b, m, n, and x0 (i.e., seed). 
        """
        #Xn+1 = (aXn + b) mod m
        def generator():
            Xn = x0
            counter = 0
            while counter < n:
                x = (a * Xn + b) % m
                yield x

                Xn = x
                counter += 1
        return generator
 
    @staticmethod
    def xorshift(a, b, c, n, x0=1):
        """
        returns a xorshift generator that generates n random numbers with xorshift
        given a, b, c, n, and x0 (i.e., seed). 
        """
        def leftShift(x, y):
            return (x << y) & 0xFFFFFFFF

        def rightShift(x, y):
            return (x >> y) & 0xFFFFFFFF
        
        def generator():
            B0 = x0
            counter = 0

            while counter < n:
                if counter == 0:
                    yield B0

                a0 = B0 ^ leftShift(B0, a)
                a1 = a0 ^ rightShift(a0, b)
                B1 = a1 ^ leftShift(a1, c)
                yield B1

                B0 = B1
                counter += 1

        return generator

    @staticmethod    
    def mersenne_twister(n, x0=1, lower=0, upper=1000):
        """
        returns a mersenne twister generator (the python generator) to generate n 
        random numbers in [lower, upper]
        given the seed x0 which defaults to 1.
        """
        random.seed(x0)
        def generator():
            for i in range(n):
                yield random.randint(lower, upper)

        return generator

    @staticmethod
    def gen_lcg_data(a, b, m, n, seed=0, option=1):
        lcgg = prng.lcg(a, b, m, n, x0=seed)()
        
        ### option 1) generate n lcg numbers.
        if option == 1:
            return np.array([next(lcgg) for _ in range(n)])

        ### option 2) generate n lcg numbers by
        ### varying the seed from i upto n-1.
        elif option == 2:
            data = np.zeros(n)
            for i in range(n):
                data[i] = next(prng.lcg(a, b, m, 1, x0=i)())
            return data
        
        ### option 3) generate n numbers with numpy arange.
        elif option == 3:
            return np.arange(n)

        else:
            raise Exception('prng.get_lcg_data(): option must be 1,2,3')

    ###xorshift(a, b, c, n, x0=1):        
    @staticmethod
    def gen_xorshift_data(a, b, c, n, seed=1, option=1):
        xsg = prng.xorshift(a, b, c, n, x0=seed)()

        if option == 1:
            return np.array([next(xsg) for _ in range(n)])
        
        elif option == 2:
            data = np.zeros(n)
            for i in range(n):
                data[i] = next(prng.xorshift(a, b, c, 1, x0=i)())
            return data
        
        elif option == 3:
            return np.arange(n)
        else: 
            raise Exception('prng.get_lcg_data(): option must be 1,2,3') 

    @staticmethod
    def gen_mersenne_twister_data(n, seed=1, lower=0, upper=1000, option=1):
        mtw = prng.mersenne_twister(n, x0=seed, lower=lower, upper=upper)()
        
        if option == 1:
            return np.array([next(mtw) for _ in range(n)])
        
        elif option == 2:
            data = np.zeros(n)
            for i in range(n):
                data[i] = next(prng.mersenne_twister(1, x0=i, lower=lower, upper=upper)())
            return data
        
        elif option == 3:
            return np.arange(n)
        else: 
            raise Exception('prng.get_lcg_data(): option must be 1,2,3') 
    
    @staticmethod
    def __get_byte(i, byte_index):
        i = int(i)
        return ((i >> (8 * byte_index)) % 256 + 256) % 256

    @staticmethod
    def __int_to_rgb(i):
        r = prng.__get_byte(i, 0) / 255
        g = prng.__get_byte(i, 1) / 255
        b = prng.__get_byte(i, 2) / 255
        return [r, g, b]

    @staticmethod
    def random_pil(data, w, h, n, name='random_pil', save_flag=True):
        """
        cooks a random PIL and saves/shows it.
        """
        img_data = np.zeros((n, 3))
        
        for i, j in enumerate(data):
            img_data[i] = prng.__int_to_rgb(j)

        img_data = img_data.reshape(h, w, 3)
        pil_img = Image.fromarray(img_data, 'RGB')
        
        if save_flag:
            pil_img.save(name + '.png')
        else:
            pil_img.show()



