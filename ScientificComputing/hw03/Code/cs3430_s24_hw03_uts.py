#############################################################
# module: cs3430_s24_hw03_uts.py
# description: unit tests for CS 3430: S24: Assignment 03
# bugs to vladimir kulyukin in Canvas
##############################################################

import unittest
import numpy as np
import numpy.linalg
from cs3430_s24_hw03 import line_ip, find_line_ips, max_obj_fun, min_obj_fun
from cs3430_s24_hw03 import plot_problem_2_constraints, plot_problem_3_constraints
from cs3430_s24_hw03 import plot_problem_4_constraints
from cs3430_s24_hw03 import problem_2, problem_3, problem_4

class cs3430_s24_hw03_uts(unittest.TestCase):

    @staticmethod
    def check_line_ip(line1, line2, ip, err=0.1e-11):
        assert ip is not None
        A1, B1, C1 = line1
        A2, B2, C2 = line2
        x, y = ip[0, 0], ip[1, 0]
        assert np.allclose(abs((A1*x + B1*y) - C1), err)
        assert np.allclose(abs((A2*x + B2*y) - C2), err)
        return True

    ### ================ Problem 1: Unit Tests =====================

    def test_hw03_prob01_ut01(self):
        print('\n***** CS3430: S24: HW03: Problem 01: Unit Test 01 ************')

        #line1: 4x + 3y = 480
        line1 = (4.0, 3.0, 480.0)
        #line2: 3x + 6y = 720
        line2 = (3.0, 6.0, 720.0)
        ip12 = line_ip(line1, line2)
        cs3430_s24_hw03_uts.check_line_ip(line1, line2, ip12)

        #line3: 1x + 0y = 0
        line3 = (1, 0, 0)
        #line4: 0x + 1y = 0
        line4 = (0, 1, 0)
        ip12 = line_ip(line3, line4)
        cs3430_s24_hw03_uts.check_line_ip(line3, line4, ip12)

        ip13 = line_ip(line1, line3)
        cs3430_s24_hw03_uts.check_line_ip(line1, line3, ip13)

        ip31 = line_ip(line3, line1)
        cs3430_s24_hw03_uts.check_line_ip(line3, line1, ip31)

        ip14 = line_ip(line1, line4)
        cs3430_s24_hw03_uts.check_line_ip(line1, line4, ip14)

        ip41 = line_ip(line4, line1)
        cs3430_s24_hw03_uts.check_line_ip(line4, line1, ip41)

        ip23 = line_ip(line2, line3)
        cs3430_s24_hw03_uts.check_line_ip(line2, line3, ip23)

        ip32 = line_ip(line3, line2)
        cs3430_s24_hw03_uts.check_line_ip(line3, line2, ip32)

        ip24 = line_ip(line2, line4)
        cs3430_s24_hw03_uts.check_line_ip(line2, line4, ip24)

        ip42 = line_ip(line4, line2)
        cs3430_s24_hw03_uts.check_line_ip(line4, line2, ip42)

        print('CS 3430: S24: HW03: Problem 01: Unit Test 01: pass')

    def test_hw03_prob01_ut02(self):
        print('\n***** CS3430: S24: HW03: Problem 01: Unit Test 02 ************')
        line1 = (1,  0, 1)
        line2 = (1, -2, 0)
        line3 = (3,  4, 12)
        
        ip12 = line_ip(line1, line2)
        cs3430_s24_hw03_uts.check_line_ip(line1, line2, ip12)
        ip21 = line_ip(line2, line1)
        cs3430_s24_hw03_uts.check_line_ip(line2, line1, ip21)

        ip13 = line_ip(line1, line3)
        cs3430_s24_hw03_uts.check_line_ip(line1, line3, ip13)
        ip31 = line_ip(line3, line1)
        cs3430_s24_hw03_uts.check_line_ip(line3, line1, ip31)

        ip23 = line_ip(line2, line3)
        cs3430_s24_hw03_uts.check_line_ip(line2, line3, ip23)
        ip32 = line_ip(line3, line2)
        cs3430_s24_hw03_uts.check_line_ip(line3, line2, ip32)
        
        print('\nCS 3430: S24: HW03: Problem 01: Unit Test 02: pass')

    def test_hw03_prob01_ut03(self):
        print('\n***** CS3430: S24: HW03: Problem 01: Unit Test 03 ************')        
        line1 = (1,  0, 1)
        line2 = (1, -2, 0)
        line3 = (3,  4, 12)
        ips = find_line_ips([line1, line2, line3])
        f = lambda x, y: 10.0*x + 5.0*y
        ip, v = max_obj_fun(f, ips)
        err = 0.1e-11        
        assert np.allclose(abs(ip[0,0] - 2.4), err)
        assert np.allclose(abs(ip[1,0] - 1.2), err)
        assert np.allclose(abs(v - 30.0), err)
        print('\nCS3430: S24: HW03: Problem 01: Unit Test 03 pass')

    def test_hw03_prob01_ut04(self):
        print('\n***** CS3430: S24: HW03: Problem 01: Unit Test 04 ************')
        line1 = (4, 3, 480)
        line2 = (3, 6, 720)
        line3 = (1, 0, 0)
        line4 = (0, 1, 0)
        ips = find_line_ips([line1, line2, line3, line4])
        obj_fun = lambda x, y: 5.0*x + 4.0*y
        ip, v = max_obj_fun(obj_fun, ips)
        err = 0.1e-11
        assert np.allclose(abs(ip[0,0] - 240.0), err)
        assert np.allclose(abs(ip[1,0] - 0.0), err)
        assert np.allclose(abs(v - 1200.0), err)
        print('\nCS3430: S24: HW03: Problem 01: Unit Test 04 pass')

    def test_hw03_prob01_ut05(self):
        print('\n***** CS3430: S24: HW03: Problem 01: Unit Test 05 ************')
        line1 = (4, 3, 480)
        line2 = (3, 6, 720)
        line3 = (1, 0, 0)
        line4 = (0, 1, 0)
        ips = find_line_ips([line1, line2, line3, line4])
        obj_fun = lambda x, y: 5.0*x + 4.0*y
        ip, v = min_obj_fun(obj_fun, ips)
        err = 0.1e-11
        assert np.allclose(abs(ip[0,0] - 0.0), err)
        assert np.allclose(abs(ip[1,0] - 0.0), err)
        assert np.allclose(abs(v - 0.0), err)
        print('\nCS3430: S24: HW03: Problem 01: Unit Test 05 pass')

    ### ========================= Problem 02 ====================================        

    def test_hw03_prob02_ut01(self):
        print('\n***** CS3430: S24: HW03: Problem 02: Unit Test 01 ************')
        plot_problem_2_constraints()
        x, y, p = problem_2()
        err = 0.1e-11
        assert np.allclose(abs(p - 13.0), err)
        assert np.allclose(abs(x - 2.0), err)
        assert np.allclose(abs(y - 7.0), err)
        print('\n CS3430: S24: HW03: Problem 02: Unit Test 01 ************')
    
    def test_hw03_prob03_ut01(self):
        print('\n***** CS3430: S24: HW03: Problem 03: Unit Test 01 ************')
        plot_problem_3_constraints()
        x, y, p = problem_3()
        err = 0.1e-11
        assert np.allclose(abs(p - 20.0/3.0), err)
        assert np.allclose(abs(x - 4.0/3.0), err)
        assert np.allclose(abs(y - 16.0/3.0), err)
        print('\nCS3430: S24: HW03: Problem 03 Unit Test 01 ************')

    def test_hw03_prob04_ut01(self):
        print('\n***** CS3430: S24: HW03: Problem 04: Unit Test 01 ************')
        plot_problem_4_constraints()
        x, y, p = problem_4()
        err = 0.1e-11
        assert np.allclose(abs(p - 650.0), err)
        assert np.allclose(abs(x - 100.0), err)
        assert np.allclose(abs(y - 50.0), err)
        print('\nCS3430: S24: HW03: Problem 04: Unit Test 01 ************')

    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
    pass

