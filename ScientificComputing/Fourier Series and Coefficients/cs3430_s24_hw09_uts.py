##################################################################
# module: cs3430_s22_hw08_uts.py
# description: unit tests CS 3430: S24: Assignment 09
# ---------------------------------------------------------------
# bugs to vladimir kulyukin in canvas.
##################################################################

'''
This is for problem 3
Muscical note frequences from https://en.wikipedia.org/wiki/Piano_key_frequencies

A7 - 3520.000
G7 - 3135.963 
E7 - 2637.020
D7 - 2349.318
----------

A6 - 1760.000
G6 - 1567.982 
E6 - 1318.510 
D6 - 1174.659
----------

A5 - 880.0000
G5 - 783.9909 
E5 - 659.2551
D5 - 587.3295
----------

A4 - 440 Hz
G4 - 391.9954 Hz
D4 - 293.6648 Hz
E4 - 329.6276 Hz
----------

A3 - 220.0000
G3 - 195.9977
E3 - 164.8138
D3 - 146.8324
----------

A2 - 110.0000
G2 - 97.99886
E2 - 82.40689
D2 - 73.41619
----------

A1 - 55.00000
G1 - 48.99943
E1 - 41.20344
D1 - 36.70810
----------
'''

import unittest
import math
import numpy as np
import matplotlib.pyplot as plt

from cs3430_s24_hw09 import nth_partial_sum_of_fourier_series
from cs3430_s24_hw09 import read_wavfile
from cs3430_s24_hw09 import recover_fourier_coeffs_in_range
from cs3430_s24_hw09 import plot_recovered_coeffs
from rmb import rmb

class cs3430_s24_hw08_uts(unittest.TestCase):

    # ### ================= Problems 1 and 2 =======================

    # """
    # ----------------------------------------------------------------------------------------
    # test_nth_partial_sum_fun_00() shows the approximation with the Fourier series of 
    # f(x)=x on [-pi, pi]; the coeffs are computed with Rombergs. 
    # -----------------------------------------------------------------------------------------
    # """
    # def test_nth_partial_sum_fun_00(self, num_points=1000, num_coeffs=20):
    #     f = lambda x: x
    #     a, b = -math.pi, math.pi
    #     cos_coeffs, sin_coeffs = [], []
    #     for i in range(num_coeffs):
    #         fcos = lambda x: f(x)*math.cos(i*x)
    #         ai = rmb.R_j_l(fcos, a, b, 7, 7)/math.pi
    #         cos_coeffs.append(ai)
    #         if i > 0:
    #             fsin = lambda x: f(x)*math.sin(i*x)
    #             bi = rmb.R_j_l(fsin, a, b, 7, 7)/math.pi
    #             sin_coeffs.append(bi)
    #     xvals = np.linspace(a, b, num_points)
    #     yvals1 = np.array([f(x) for x in xvals])
    #     yvals2 = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs) for x in xvals])
    #     fig1 = plt.figure(1)
    #     fig1.suptitle('y=x; num_coeff={}'.format(num_coeffs))
    #     plt.xlabel('x')
    #     plt.ylabel('y')
    #     plt.grid()
    #     plt.xlim([a, b])
    #     plt.plot(xvals, yvals1, label='y=x', c='r')
    #     plt.plot(xvals, yvals2, label='y=nth_partial_sum', c='b')        
    #     plt.legend(loc='best')
    #     plt.show()

    """
    ----------------------------------------------------------------------------------------
    test_plot_error_fun_00() shows the true error of the approximation of the Fourier series of 
    f(x)=x on [-pi, pi]; the coeffs are computed with Rombergs. 
    -----------------------------------------------------------------------------------------
    """
    # def test_plot_error_fun_00(self, num_points=1000, num_coeffs=20):
    #     f = lambda x: x
    #     a, b = -math.pi, math.pi
    #     cos_coeffs = []
    #     sin_coeffs = []
    #     for i in range(num_coeffs):
    #         fcos = lambda x: f(x)*math.cos(i*x)
    #         ai = rmb.R_j_l(fcos, a, b, 7, 7)/math.pi
    #         cos_coeffs.append(ai)
    #         if i > 0:
    #             fsin = lambda x: f(x)*math.sin(i*x)
    #             bi = rmb.R_j_l(fsin, a, b, 7, 7)/math.pi
    #             sin_coeffs.append(bi)
    #     xvals = np.linspace(a, b, num_points)
    #     gt_vals = np.array([f(x) for x in xvals])
    #     approx_vals = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs)
    #                             for x in xvals])
    #     err_vals  = [gtav[0]- gtav[1] for gtav in zip(gt_vals, approx_vals)]
    #     fig1 = plt.figure(1)
    #     fig1.suptitle('True Error for y=x; on [{:.2f}, {:.2f}]; num_coeffs={}'.format(a, b, num_coeffs))
    #     plt.xlabel('x')
    #     plt.ylabel('True Error of y=x')
    #     plt.grid()
    #     plt.plot(xvals, err_vals, label='err', c='b')    
    #     plt.legend(loc='best')
    #     plt.show()

    """
    ----------------------------------------------------------------------------------------
    test_nth_partial_sum_fun_01() shows the approximation with the Fourier series of 
    f(x)=x^2 on [-pi, pi]; the coeffs are computed with Rombergs. 
    -----------------------------------------------------------------------------------------
    """
    def test_nth_partial_sum_fun_01(self, num_points=1000, num_coeffs=3):
        f = lambda x: x**2
        a, b = -math.pi, math.pi
        cos_coeffs, sin_coeffs = [], []
        for i in range(num_coeffs):
            fcos = lambda x: f(x)*math.cos(i*x)
            ai = rmb.R_j_l(fcos, a, b, 7, 7)/math.pi
            cos_coeffs.append(ai)
            if i > 0:
                fsin = lambda x: f(x)*math.sin(i*x)
                bi = rmb.R_j_l(fsin, a, b, 7, 7)/math.pi
                sin_coeffs.append(bi)
        xvals = np.linspace(a, b, num_points)
        yvals1 = np.array([f(x) for x in xvals])
        yvals2 = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs) for x in xvals])
        fig1 = plt.figure(1)
        fig1.suptitle('y=x; num_coeff={}'.format(num_coeffs))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid()
        plt.xlim([a, b])
        plt.plot(xvals, yvals1, label='y=x', c='r')
        plt.plot(xvals, yvals2, label='y=nth_partial_sum', c='b')        
        plt.legend(loc='best')
        plt.show()

    """
    ----------------------------------------------------------------------------------------
    test_plot_error_fun_01() shows the true error of the approximation of the Fourier series of 
    f(x)=x^2 on [-pi, pi]; the coeffs are computed with Rombergs. 
    -----------------------------------------------------------------------------------------
    """
    # def test_plot_error_fun_01(self, num_points=1000, num_coeffs=3):
    #     f = lambda x: x**2
    #     a, b = -math.pi, math.pi
    #     cos_coeffs = []
    #     sin_coeffs = []
    #     for i in range(num_coeffs):
    #         fcos = lambda x: f(x)*math.cos(i*x)
    #         ai = rmb.R_j_l(fcos, a, b, 7, 7)/math.pi
    #         cos_coeffs.append(ai)
    #         if i > 0:
    #             fsin = lambda x: f(x)*math.sin(i*x)
    #             bi = rmb.R_j_l(fsin, a, b, 7, 7)/math.pi
    #             sin_coeffs.append(bi)
    #     xvals = np.linspace(a, b, num_points)
    #     gt_vals = np.array([f(x) for x in xvals])
    #     approx_vals = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs)
    #                             for x in xvals])
    #     err_vals  = [gtav[0]- gtav[1] for gtav in zip(gt_vals, approx_vals)]
    #     fig1 = plt.figure(1)
    #     fig1.suptitle('True Error for y=x; on [{:.2f}, {:.2f}]; num_coeffs={}'.format(a, b, num_coeffs))
    #     plt.xlabel('x')
    #     plt.ylabel('True Error of y=x')
    #     plt.grid()
    #     plt.plot(xvals, err_vals, label='err', c='b')    
    #     plt.legend(loc='best')
    #     plt.show()

    # """
    # ----------------------------------------------------------------------------------------
    # test_nth_partial_sum_fun_02() shows the approximation with the Fourier series of 
    # f(x)=x^3 on [-pi, pi]; the coeffs are computed with Rombergs. 
    # -----------------------------------------------------------------------------------------
    # """
    # def test_nth_partial_sum_fun_02(self, num_points=1000, num_coeffs=20):
    #     f = lambda x: x**3
    #     a, b = -math.pi, math.pi
    #     cos_coeffs, sin_coeffs = [], []
    #     for i in range(num_coeffs):
    #         fcos = lambda x: f(x)*math.cos(i*x)
    #         ai = rmb.R_j_l(fcos, a, b, 7, 7)/math.pi
    #         cos_coeffs.append(ai)
    #         if i > 0:
    #             fsin = lambda x: f(x)*math.sin(i*x)
    #             bi = rmb.R_j_l(fsin, a, b, 7, 7)/math.pi
    #             sin_coeffs.append(bi)
    #     xvals = np.linspace(a, b, num_points)
    #     yvals1 = np.array([f(x) for x in xvals])
    #     yvals2 = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs) for x in xvals])
    #     fig1 = plt.figure(1)
    #     fig1.suptitle('y=x; num_coeff={}'.format(num_coeffs))
    #     plt.xlabel('x')
    #     plt.ylabel('y')
    #     plt.grid()
    #     plt.xlim([a, b])
    #     plt.plot(xvals, yvals1, label='y=x', c='r')
    #     plt.plot(xvals, yvals2, label='y=nth_partial_sum', c='b')        
    #     plt.legend(loc='best')
    #     plt.show()

    # """
    # ----------------------------------------------------------------------------------------
    # test_plot_error_fun_02() shows the true error of the approximation of the Fourier series of 
    # f(x)=x^3 on [-pi, pi]; the coeffs are computed with Rombergs. 
    # -----------------------------------------------------------------------------------------
    # """
    # def test_plot_error_fun_02(self, num_points=1000, num_coeffs=20):
    #     f = lambda x: x**3
    #     a, b = -math.pi, math.pi
    #     cos_coeffs = []
    #     sin_coeffs = []
    #     for i in range(num_coeffs):
    #         fcos = lambda x: f(x)*math.cos(i*x)
    #         ai = rmb.R_j_l(fcos, a, b, 7, 7)/math.pi
    #         cos_coeffs.append(ai)
    #         if i > 0:
    #             fsin = lambda x: f(x)*math.sin(i*x)
    #             bi = rmb.R_j_l(fsin, a, b, 7, 7)/math.pi
    #             sin_coeffs.append(bi)
    #     xvals = np.linspace(a, b, num_points)
    #     gt_vals = np.array([f(x) for x in xvals])
    #     approx_vals = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs)
    #                             for x in xvals])
    #     err_vals  = [gtav[0]- gtav[1] for gtav in zip(gt_vals, approx_vals)]
    #     fig1 = plt.figure(1)
    #     fig1.suptitle('True Error for y=x; on [{:.2f}, {:.2f}]; num_coeffs={}'.format(a, b, num_coeffs))
    #     plt.xlabel('x')
    #     plt.ylabel('True Error of y=x')
    #     plt.grid()
    #     plt.plot(xvals, err_vals, label='err', c='b')    
    #     plt.legend(loc='best')
    #     plt.show()

        
    # """
    # ----------------------------------------------------------------------------------------
    # test_nth_partial_sum_fun_03() shows the approximation with the Fourier series of 
    # f(x)=x+1 on [-pi, pi]; the coeffs are computed with Rombergs. 
    # -----------------------------------------------------------------------------------------
    # """
    # def test_nth_partial_sum_fun_03(self, num_points=1000, num_coeffs=20):
    #     f = lambda x: x+1
    #     a, b = -math.pi, math.pi
    #     cos_coeffs, sin_coeffs = [], []
    #     for i in range(num_coeffs):
    #         fcos = lambda x: f(x)*math.cos(i*x)
    #         ai = rmb.R_j_l(fcos, a, b, 7, 7)/math.pi
    #         cos_coeffs.append(ai)
    #         if i > 0:
    #             fsin = lambda x: f(x)*math.sin(i*x)
    #             bi = rmb.R_j_l(fsin, a, b, 7, 7)/math.pi
    #             sin_coeffs.append(bi)
    #     xvals = np.linspace(a, b, num_points)
    #     yvals1 = np.array([f(x) for x in xvals])
    #     yvals2 = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs) for x in xvals])
    #     fig1 = plt.figure(1)
    #     fig1.suptitle('y=x; num_coeff={}'.format(num_coeffs))
    #     plt.xlabel('x')
    #     plt.ylabel('y')
    #     plt.grid()
    #     plt.xlim([a, b])
    #     plt.plot(xvals, yvals1, label='y=x', c='r')
    #     plt.plot(xvals, yvals2, label='y=nth_partial_sum', c='b')        
    #     plt.legend(loc='best')
    #     plt.show()

    # """
    # ----------------------------------------------------------------------------------------
    # test_plot_error_fun_03() shows the true error of the approximation of the Fourier series of 
    # f(x)=x+1 on [-pi, pi]; the coeffs are computed with Rombergs. 
    # -----------------------------------------------------------------------------------------
    # """
    # def test_plot_error_fun_03(self, num_points=1000, num_coeffs=20):
    #     f = lambda x: x + 1
    #     a, b = -math.pi, math.pi
    #     cos_coeffs = []
    #     sin_coeffs = []
    #     for i in range(num_coeffs):
    #         fcos = lambda x: f(x)*math.cos(i*x)
    #         ai = rmb.R_j_l(fcos, a, b, 7, 7)/math.pi
    #         cos_coeffs.append(ai)
    #         if i > 0:
    #             fsin = lambda x: f(x)*math.sin(i*x)
    #             bi = rmb.R_j_l(fsin, a, b, 7, 7)/math.pi
    #             sin_coeffs.append(bi)
    #     xvals = np.linspace(a, b, num_points)
    #     gt_vals = np.array([f(x) for x in xvals])
    #     approx_vals = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs)
    #                             for x in xvals])
    #     err_vals  = [gtav[0]- gtav[1] for gtav in zip(gt_vals, approx_vals)]
    #     fig1 = plt.figure(1)
    #     fig1.suptitle('True Error for y=x; on [{:.2f}, {:.2f}]; num_coeffs={}'.format(a, b, num_coeffs))
    #     plt.xlabel('x')
    #     plt.ylabel('True Error of y=x')
    #     plt.grid()
    #     plt.plot(xvals, err_vals, label='err', c='b')    
    #     plt.legend(loc='best')
    #     plt.show()

    # """
    # ----------------------------------------------------------------------------------------
    # test_nth_partial_sum_fun_04() shows the approximation with the Fourier series of 
    # f(x)=x**5 on [-pi, pi]; the coeffs are computed with Rombergs. 
    # -----------------------------------------------------------------------------------------
    # """
    # def test_nth_partial_sum_fun_04(self, num_points=1000, num_coeffs=20):
    #     f = lambda x: x**5
    #     a, b = -math.pi, math.pi
    #     cos_coeffs, sin_coeffs = [], []
    #     for i in range(num_coeffs):
    #         fcos = lambda x: f(x)*math.cos(i*x)
    #         ai = rmb.R_j_l(fcos, a, b, 7, 7)/math.pi
    #         cos_coeffs.append(ai)
    #         if i > 0:
    #             fsin = lambda x: f(x)*math.sin(i*x)
    #             bi = rmb.R_j_l(fsin, a, b, 7, 7)/math.pi
    #             sin_coeffs.append(bi)
    #     xvals = np.linspace(a, b, num_points)
    #     yvals1 = np.array([f(x) for x in xvals])
    #     yvals2 = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs) for x in xvals])
    #     fig1 = plt.figure(1)
    #     fig1.suptitle('y=x; num_coeff={}'.format(num_coeffs))
    #     plt.xlabel('x')
    #     plt.ylabel('y')
    #     plt.grid()
    #     plt.xlim([a, b])
    #     plt.plot(xvals, yvals1, label='y=x', c='r')
    #     plt.plot(xvals, yvals2, label='y=nth_partial_sum', c='b')        
    #     plt.legend(loc='best')
    #     plt.show()

    # """
    # ----------------------------------------------------------------------------------------
    # test_plot_error_fun_04() shows the true error of the approximation of the Fourier series of 
    # f(x)=^5 on [-pi, pi]; the coeffs are computed with Rombergs. 
    # -----------------------------------------------------------------------------------------
    # """
    # def test_plot_error_fun_04(self, num_points=1000, num_coeffs=20):
    #     f = lambda x: x**5
    #     a, b = -math.pi, math.pi
    #     cos_coeffs = []
    #     sin_coeffs = []
    #     for i in range(num_coeffs):
    #         fcos = lambda x: f(x)*math.cos(i*x)
    #         ai = rmb.R_j_l(fcos, a, b, 7, 7)/math.pi
    #         cos_coeffs.append(ai)
    #         if i > 0:
    #             fsin = lambda x: f(x)*math.sin(i*x)
    #             bi = rmb.R_j_l(fsin, a, b, 7, 7)/math.pi
    #             sin_coeffs.append(bi)
    #     xvals = np.linspace(a, b, num_points)
    #     gt_vals = np.array([f(x) for x in xvals])
    #     approx_vals = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs)
    #                             for x in xvals])
    #     err_vals  = [gtav[0]- gtav[1] for gtav in zip(gt_vals, approx_vals)]
    #     fig1 = plt.figure(1)
    #     fig1.suptitle('True Error for y=x; on [{:.2f}, {:.2f}]; num_coeffs={}'.format(a, b, num_coeffs))
    #     plt.xlabel('x')
    #     plt.ylabel('True Error of y=x')
    #     plt.grid()
    #     plt.plot(xvals, err_vals, label='err', c='b')    
    #     plt.legend(loc='best')
    #     plt.show()
        
    # """
    # ----------------------------------------------------------------------------------------
    # test_nth_partial_sum_fun_05() shows the approximation with the Fourier series of 
    # f(x)=cos(x) on [-pi, pi]; the coeffs are computed with Rombergs. 
    # -----------------------------------------------------------------------------------------
    # """
    # def test_nth_partial_sum_fun_05(self, num_points=1000, num_coeffs=20):
    #     f = lambda x: math.cos(x)
    #     a, b = -math.pi, math.pi
    #     cos_coeffs, sin_coeffs = [], []
    #     for i in range(num_coeffs):
    #         fcos = lambda x: f(x)*math.cos(i*x)
    #         ai = rmb.R_j_l(fcos, a, b, 7, 7)/math.pi
    #         cos_coeffs.append(ai)
    #         if i > 0:
    #             fsin = lambda x: f(x)*math.sin(i*x)
    #             bi = rmb.R_j_l(fsin, a, b, 7, 7)/math.pi
    #             sin_coeffs.append(bi)
    #     xvals = np.linspace(a, b, num_points)
    #     yvals1 = np.array([f(x) for x in xvals])
    #     yvals2 = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs) for x in xvals])
    #     fig1 = plt.figure(1)
    #     fig1.suptitle('y=x; num_coeff={}'.format(num_coeffs))
    #     plt.xlabel('x')
    #     plt.ylabel('y')
    #     plt.grid()
    #     plt.xlim([a, b])
    #     plt.plot(xvals, yvals1, label='y=x', c='r')
    #     plt.plot(xvals, yvals2, label='y=nth_partial_sum', c='b')        
    #     plt.legend(loc='best')
    #     plt.show()


    # """
    # ----------------------------------------------------------------------------------------
    # test_plot_error_fun_05() shows the true error of the approximation of the Fourier series of 
    # f(x)=cos(x) on [-pi, pi].
    # -----------------------------------------------------------------------------------------
    # """
    # def test_plot_error_fun_05(self, num_points=1000, num_coeffs=20):
    #     f = lambda x: math.cos(x)
    #     a, b = -math.pi, math.pi
    #     cos_coeffs = []
    #     sin_coeffs = []
    #     for i in range(num_coeffs):
    #         fcos = lambda x: f(x)*math.cos(i*x)
    #         ai = rmb.R_j_l(fcos, a, b, 7, 7)/math.pi
    #         cos_coeffs.append(ai)
    #         if i > 0:
    #             fsin = lambda x: f(x)*math.sin(i*x)
    #             bi = rmb.R_j_l(fsin, a, b, 7, 7)/math.pi
    #             sin_coeffs.append(bi)
    #     xvals = np.linspace(a, b, num_points)
    #     gt_vals = np.array([f(x) for x in xvals])
    #     approx_vals = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs)
    #                             for x in xvals])
    #     err_vals  = [gtav[0]- gtav[1] for gtav in zip(gt_vals, approx_vals)]
    #     fig1 = plt.figure(1)
    #     fig1.suptitle('True Error for y=x; on [{:.2f}, {:.2f}]; num_coeffs={}'.format(a, b, num_coeffs))
    #     plt.xlabel('x')
    #     plt.ylabel('True Error of y=x')
    #     plt.grid()
    #     plt.plot(xvals, err_vals, label='err', c='b')    
    #     plt.legend(loc='best')
    #     plt.show()


    # """
    # ----------------------------------------------------------------------------------------
    # test_nth_partial_sum_fun_06() shows the approximation with the Fourier series of 
    # f(x)=cos(x) + 2cos(2x); on [-pi, pi]; the coeffs are computed with Rombergs. 
    # -----------------------------------------------------------------------------------------
    # """
    # def test_nth_partial_sum_fun_06(self, num_points=1000, num_coeffs=20):
    #     f = lambda x: math.cos(x) + 2*math.cos(2*x)
    #     a, b = -math.pi, math.pi
    #     cos_coeffs, sin_coeffs = [], []
    #     for i in range(num_coeffs):
    #         fcos = lambda x: f(x)*math.cos(i*x)
    #         ai = rmb.R_j_l(fcos, a, b, 7, 7)/math.pi
    #         cos_coeffs.append(ai)
    #         if i > 0:
    #             fsin = lambda x: f(x)*math.sin(i*x)
    #             bi = rmb.R_j_l(fsin, a, b, 7, 7)/math.pi
    #             sin_coeffs.append(bi)
    #     xvals = np.linspace(a, b, num_points)
    #     yvals1 = np.array([f(x) for x in xvals])
    #     yvals2 = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs) for x in xvals])
    #     fig1 = plt.figure(1)
    #     fig1.suptitle('y=x; num_coeff={}'.format(num_coeffs))
    #     plt.xlabel('x')
    #     plt.ylabel('y')
    #     plt.grid()
    #     plt.xlim([a, b])
    #     plt.plot(xvals, yvals1, label='y=x', c='r')
    #     plt.plot(xvals, yvals2, label='y=nth_partial_sum', c='b')        
    #     plt.legend(loc='best')
    #     plt.show()

    # """
    # ----------------------------------------------------------------------------------------
    # test_plot_error_fun_06() shows the true error of the approximation of the Fourier series of 
    # f(x)=cos(x)+2cos on(x) [-pi, pi]; the coeffs are computed with Rombergs. 
    # -----------------------------------------------------------------------------------------
    # """
    # def test_plot_error_fun_06(self, num_points=1000, num_coeffs=20):
    #     f = lambda x: math.cos(x) + 2*math.cos(2*x)        
    #     a, b = -math.pi, math.pi
    #     cos_coeffs = []
    #     sin_coeffs = []
    #     for i in range(num_coeffs):
    #         fcos = lambda x: f(x)*math.cos(i*x)
    #         ai = rmb.R_j_l(fcos, a, b, 7, 7)/math.pi
    #         cos_coeffs.append(ai)
    #         if i > 0:
    #             fsin = lambda x: f(x)*math.sin(i*x)
    #             bi = rmb.R_j_l(fsin, a, b, 7, 7)/math.pi
    #             sin_coeffs.append(bi)
    #     xvals = np.linspace(a, b, num_points)
    #     gt_vals = np.array([f(x) for x in xvals])
    #     approx_vals = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs)
    #                             for x in xvals])
    #     err_vals  = [gtav[0]- gtav[1] for gtav in zip(gt_vals, approx_vals)]
    #     fig1 = plt.figure(1)
    #     fig1.suptitle('True Error for y=x; on [{:.2f}, {:.2f}]; num_coeffs={}'.format(a, b, num_coeffs))
    #     plt.xlabel('x')
    #     plt.ylabel('True Error of y=x')
    #     plt.grid()
    #     plt.plot(xvals, err_vals, label='err', c='b')    
    #     plt.legend(loc='best')
    #     plt.show()

    
    # """
    # ----------------------------------------------------------------------------------------
    # test_nth_partial_sum_fun_07() shows the approximation with the Fourier series of 
    # f(x) = cos(x) + 2cos(2x) + 3cos(3x) + 4cos(4x) + 5cos(5x); on [-pi, pi]; the coeffs are computed with Rombergs. 
    # -----------------------------------------------------------------------------------------
    # """
    # def test_nth_partial_sum_fun_07(self, num_points=1000, num_coeffs=20):
    #     f = lambda x: math.cos(x) + 2*math.cos(2*x) + 3*math.cos(3*x) + 4*math.cos(4*x) + 5*math.cos(5*x)
    #     a, b = -math.pi, math.pi
    #     cos_coeffs, sin_coeffs = [], []
    #     for i in range(num_coeffs):
    #         fcos = lambda x: f(x)*math.cos(i*x)
    #         ai = rmb.R_j_l(fcos, a, b, 7, 7)/math.pi
    #         cos_coeffs.append(ai)
    #         if i > 0:
    #             fsin = lambda x: f(x)*math.sin(i*x)
    #             bi = rmb.R_j_l(fsin, a, b, 7, 7)/math.pi
    #             sin_coeffs.append(bi)
    #     xvals = np.linspace(a, b, num_points)
    #     yvals1 = np.array([f(x) for x in xvals])
    #     yvals2 = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs) for x in xvals])
    #     fig1 = plt.figure(1)
    #     fig1.suptitle('y=x; num_coeff={}'.format(num_coeffs))
    #     plt.xlabel('x')
    #     plt.ylabel('y')
    #     plt.grid()
    #     plt.xlim([a, b])
    #     plt.plot(xvals, yvals1, label='y=x', c='r')
    #     plt.plot(xvals, yvals2, label='y=nth_partial_sum', c='b')        
    #     plt.legend(loc='best')
    #     plt.show()

    # """
    # ----------------------------------------------------------------------------------------
    # test_plot_error_fun_07() shows the true error of the approximation of the Fourier series of 
    # f(x) = cos(x) + 2cos(2x) + 3cos(3x) + 4cos(4x) + 5cos(5x) on [-pi, pi]; the coeffs are computed with Rombergs. 
    # -----------------------------------------------------------------------------------------
    # """
    # def test_plot_error_fun_07(self, num_points=1000, num_coeffs=20):
    #     f = lambda x: math.cos(x) + 2*math.cos(2*x) + 3*math.cos(3*x) + 4*math.cos(4*x) + 5*math.cos(5*x)
    #     a, b = -math.pi, math.pi
    #     cos_coeffs = []
    #     sin_coeffs = []
    #     for i in range(num_coeffs):
    #         fcos = lambda x: f(x)*math.cos(i*x)
    #         ai = rmb.R_j_l(fcos, a, b, 7, 7)/math.pi
    #         cos_coeffs.append(ai)
    #         if i > 0:
    #             fsin = lambda x: f(x)*math.sin(i*x)
    #             bi = rmb.R_j_l(fsin, a, b, 7, 7)/math.pi
    #             sin_coeffs.append(bi)
    #     xvals = np.linspace(a, b, num_points)
    #     gt_vals = np.array([f(x) for x in xvals])
    #     approx_vals = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs)
    #                             for x in xvals])
    #     err_vals  = [gtav[0]- gtav[1] for gtav in zip(gt_vals, approx_vals)]
    #     fig1 = plt.figure(1)
    #     fig1.suptitle('True Error for y=x; on [{:.2f}, {:.2f}]; num_coeffs={}'.format(a, b, num_coeffs))
    #     plt.xlabel('x')
    #     plt.ylabel('True Error of y=x')
    #     plt.grid()
    #     plt.plot(xvals, err_vals, label='err', c='b')    
    #     plt.legend(loc='best')
    #     plt.show()

    # """
    # ----------------------------------------------------------------------------------------
    # test_nth_partial_sum_fun_08() shows the approximation with the Fourier series of 
    # f7(x) = |x| on [-pi, pi]; the coeffs are computed with Rombergs. 
    # -----------------------------------------------------------------------------------------
    # """
    # def test_nth_partial_sum_fun_08(self, num_points=1000, num_coeffs=20):
    #     f = lambda x: abs(x)
    #     a, b = -math.pi, math.pi
    #     cos_coeffs, sin_coeffs = [], []
    #     for i in range(num_coeffs):
    #         fcos = lambda x: f(x)*math.cos(i*x)
    #         ai = rmb.R_j_l(fcos, a, b, 7, 7)/math.pi
    #         cos_coeffs.append(ai)
    #         if i > 0:
    #             fsin = lambda x: f(x)*math.sin(i*x)
    #             bi = rmb.R_j_l(fsin, a, b, 7, 7)/math.pi
    #             sin_coeffs.append(bi)
    #     xvals = np.linspace(a, b, num_points)
    #     yvals1 = np.array([f(x) for x in xvals])
    #     yvals2 = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs) for x in xvals])
    #     fig1 = plt.figure(1)
    #     fig1.suptitle('y=x; num_coeff={}'.format(num_coeffs))
    #     plt.xlabel('x')
    #     plt.ylabel('y')
    #     plt.grid()
    #     plt.xlim([a, b])
    #     plt.plot(xvals, yvals1, label='y=x', c='r')
    #     plt.plot(xvals, yvals2, label='y=nth_partial_sum', c='b')        
    #     plt.legend(loc='best')
    #     plt.show()

    # """
    # ----------------------------------------------------------------------------------------
    # test_plot_error_fun_08() shows the true error of the approximation of the Fourier series of 
    # f(x) = |x| on [-pi, pi]; the coeffs are computed with Rombergs. 
    # -----------------------------------------------------------------------------------------
    # """
    # def test_plot_error_fun_08(self, num_points=1000, num_coeffs=20):
    #     f = lambda x: abs(x)
    #     a, b = -math.pi, math.pi
    #     cos_coeffs = []
    #     sin_coeffs = []
    #     for i in range(num_coeffs):
    #         fcos = lambda x: f(x)*math.cos(i*x)
    #         ai = rmb.R_j_l(fcos, a, b, 7, 7)/math.pi
    #         cos_coeffs.append(ai)
    #         if i > 0:
    #             fsin = lambda x: f(x)*math.sin(i*x)
    #             bi = rmb.R_j_l(fsin, a, b, 7, 7)/math.pi
    #             sin_coeffs.append(bi)
    #     xvals = np.linspace(a, b, num_points)
    #     gt_vals = np.array([f(x) for x in xvals])
    #     approx_vals = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs)
    #                             for x in xvals])
    #     err_vals  = [gtav[0]- gtav[1] for gtav in zip(gt_vals, approx_vals)]
    #     fig1 = plt.figure(1)
    #     fig1.suptitle('True Error for y=x; on [{:.2f}, {:.2f}]; num_coeffs={}'.format(a, b, num_coeffs))
    #     plt.xlabel('x')
    #     plt.ylabel('True Error of y=x')
    #     plt.grid()
    #     plt.plot(xvals, err_vals, label='err', c='b')    
    #     plt.legend(loc='best')
    #     plt.show()

    # """
    # ----------------------------------------------------------------------------------------
    # test_nth_partial_sum_fun_09() shows the approximation with the Fourier series of 
    # f(x)=|x^5+3x+2| on [-pi, pi]; the coeffs are computed with Rombergs. 
    # -----------------------------------------------------------------------------------------
    # """
    # def test_nth_partial_sum_fun_09(self, num_points=1000, num_coeffs=20):
    #     f = lambda x: abs(x**5+3*x+2)
    #     a, b = -math.pi, math.pi
    #     cos_coeffs, sin_coeffs = [], []
    #     for i in range(num_coeffs):
    #         fcos = lambda x: f(x)*math.cos(i*x)
    #         ai = rmb.R_j_l(fcos, a, b, 7, 7)/math.pi
    #         cos_coeffs.append(ai)
    #         if i > 0:
    #             fsin = lambda x: f(x)*math.sin(i*x)
    #             bi = rmb.R_j_l(fsin, a, b, 7, 7)/math.pi
    #             sin_coeffs.append(bi)
    #     xvals = np.linspace(a, b, num_points)
    #     yvals1 = np.array([f(x) for x in xvals])
    #     yvals2 = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs) for x in xvals])
    #     fig1 = plt.figure(1)
    #     fig1.suptitle('y=x; num_coeff={}'.format(num_coeffs))
    #     plt.xlabel('x')
    #     plt.ylabel('y')
    #     plt.grid()
    #     plt.xlim([a, b])
    #     plt.plot(xvals, yvals1, label='y=x', c='r')
    #     plt.plot(xvals, yvals2, label='y=nth_partial_sum', c='b')        
    #     plt.legend(loc='best')
    #     plt.show()

    # """
    # ----------------------------------------------------------------------------------------
    # test_plot_error_fun_09() shows the true error of the approximation of the Fourier series of 
    # f(x)=|x^5+3x+2| on [-pi, pi]; the coeffs are computed with Rombergs. 
    # -----------------------------------------------------------------------------------------
    # """
    # def test_plot_error_fun_09(self, num_points=1000, num_coeffs=20):
    #     f = lambda x: abs(x**5+3*x+2)        
    #     a, b = -math.pi, math.pi
    #     cos_coeffs = []
    #     sin_coeffs = []
    #     for i in range(num_coeffs):
    #         fcos = lambda x: f(x)*math.cos(i*x)
    #         ai = rmb.R_j_l(fcos, a, b, 7, 7)/math.pi
    #         cos_coeffs.append(ai)
    #         if i > 0:
    #             fsin = lambda x: f(x)*math.sin(i*x)
    #             bi = rmb.R_j_l(fsin, a, b, 7, 7)/math.pi
    #             sin_coeffs.append(bi)
    #     xvals = np.linspace(a, b, num_points)
    #     gt_vals = np.array([f(x) for x in xvals])
    #     approx_vals = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs)
    #                             for x in xvals])
    #     err_vals  = [gtav[0]- gtav[1] for gtav in zip(gt_vals, approx_vals)]
    #     fig1 = plt.figure(1)
    #     fig1.suptitle('True Error for y=x; on [{:.2f}, {:.2f}]; num_coeffs={}'.format(a, b, num_coeffs))
    #     plt.xlabel('x')
    #     plt.ylabel('True Error of y=x')
    #     plt.grid()
    #     plt.plot(xvals, err_vals, label='err', c='b')    
    #     plt.legend(loc='best')
    #     plt.show()

    # """
    # ----------------------------------------------------------------------------------------
    # test_nth_partial_sum_fun_10() shows the approximation with the Fourier series of 
    # f(x)=abs(math.sin(x) + 2*math.sin(2*x) + 3*math.sin(3*x)) on [-pi, pi]; the coeffs are computed with Rombergs. 
    # -----------------------------------------------------------------------------------------
    # """
    # def test_nth_partial_sum_fun_10(self, num_points=1000, num_coeffs=20):
    #     f = lambda x: abs(math.sin(x) + 2*math.sin(2*x) + 3*math.sin(3*x))
    #     a, b = -math.pi, math.pi
    #     cos_coeffs, sin_coeffs = [], []
    #     for i in range(num_coeffs):
    #         fcos = lambda x: f(x)*math.cos(i*x)
    #         ai = rmb.R_j_l(fcos, a, b, 7, 7)/math.pi
    #         cos_coeffs.append(ai)
    #         if i > 0:
    #             fsin = lambda x: f(x)*math.sin(i*x)
    #             bi = rmb.R_j_l(fsin, a, b, 7, 7)/math.pi
    #             sin_coeffs.append(bi)
    #     xvals = np.linspace(a, b, num_points)
    #     yvals1 = np.array([f(x) for x in xvals])
    #     yvals2 = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs) for x in xvals])
    #     fig1 = plt.figure(1)
    #     fig1.suptitle('y=x; num_coeff={}'.format(num_coeffs))
    #     plt.xlabel('x')
    #     plt.ylabel('y')
    #     plt.grid()
    #     plt.xlim([a, b])
    #     plt.plot(xvals, yvals1, label='y=x', c='r')
    #     plt.plot(xvals, yvals2, label='y=nth_partial_sum', c='b')        
    #     plt.legend(loc='best')
    #     plt.show()

    # """
    # ----------------------------------------------------------------------------------------
    # test_plot_error_fun_10() shows the true error of the approximation of the Fourier series of 
    # abs(math.sin(x) + 2*math.sin(2*x) + 3*math.sin(3*x)) on [-pi, pi]; the coeffs are computed with Rombergs. 
    # -----------------------------------------------------------------------------------------
    # """
    # def test_plot_error_fun_10(self, num_points=1000, num_coeffs=20):
    #     f = lambda x: abs(math.sin(x) + 2*math.sin(2*x) + 3*math.sin(3*x))        
    #     a, b = -math.pi, math.pi
    #     cos_coeffs = []
    #     sin_coeffs = []
    #     for i in range(num_coeffs):
    #         fcos = lambda x: f(x)*math.cos(i*x)
    #         ai = rmb.R_j_l(fcos, a, b, 7, 7)/math.pi
    #         cos_coeffs.append(ai)
    #         if i > 0:
    #             fsin = lambda x: f(x)*math.sin(i*x)
    #             bi = rmb.R_j_l(fsin, a, b, 7, 7)/math.pi
    #             sin_coeffs.append(bi)
    #     xvals = np.linspace(a, b, num_points)
    #     gt_vals = np.array([f(x) for x in xvals])
    #     approx_vals = np.array([nth_partial_sum_of_fourier_series(x, cos_coeffs, sin_coeffs)
    #                             for x in xvals])
    #     err_vals  = [gtav[0]- gtav[1] for gtav in zip(gt_vals, approx_vals)]
    #     fig1 = plt.figure(1)
    #     fig1.suptitle('True Error for y=x; on [{:.2f}, {:.2f}]; num_coeffs={}'.format(a, b, num_coeffs))
    #     plt.xlabel('x')
    #     plt.ylabel('True Error of y=x')
    #     plt.grid()
    #     plt.plot(xvals, err_vals, label='err', c='b')    
    #     plt.legend(loc='best')
    #     plt.show()



    # ### ======================== Problem 3 ===================================
    
    # def test_guitar_wavfile(self):
    #     fs, amps = read_wavfile('Guitar/Guitar_A.wav')
    #     print('\nGuitar_A.wav data:')
    #     print('frequency = {}'.format(fs))
    #     print('num amp readings = {}'.format(len(amps)))
    #     print(amps[:5])
    #     print('\nGuitar_D.wav data:')
    #     fs, amps = read_wavfile('Guitar/Guitar_D.wav')
    #     print('frequency = {}'.format(fs))
    #     print('num amp readings = {}'.format(len(amps)))
    #     print(amps[:5])
    #     print('\nGuitar_E.wav data:')
    #     fs, amps = read_wavfile('Guitar/Guitar_E.wav')
    #     print('frequency = {}'.format(fs))
    #     print('num amp readings = {}'.format(len(amps)))
    #     print(amps[:5])
    #     print('\nGuitar_G.wav data:')
    #     fs, amps = read_wavfile('Guitar/Guitar_G.wav')
    #     print('frequency = {}'.format(fs))
    #     print('num amp readings = {}'.format(len(amps)))
    #     print(amps[:5])

    # def test_violin_wavfile(self):
    #     fs, amps = read_wavfile('Violin/Violin_A.wav')
    #     print('\nViolin_A.wav data:')
    #     print('frequency = {}'.format(fs))
    #     print('num amp readings = {}'.format(len(amps)))
    #     print(amps[:5])
    #     print('\nViolinr_D.wav data:')
    #     fs, amps = read_wavfile('Violin/Violin_D.wav')
    #     print('frequency = {}'.format(fs))
    #     print('num amp readings = {}'.format(len(amps)))
    #     print(amps[:5])
    #     print('\nViolin_E.wav data:')
    #     fs, amps = read_wavfile('Violin/Violin_E.wav')
    #     print('frequency = {}'.format(fs))
    #     print('num amp readings = {}'.format(len(amps)))
    #     print(amps[:5])
    #     print('\nViolin_G.wav data:')
    #     fs, amps = read_wavfile('Violin/Violin_G.wav')
    #     print('frequency = {}'.format(fs))
    #     print('num amp readings = {}'.format(len(amps)))
    #     print(amps[:5])
        
    # def test_recover_fourier_coeffs_in_range_01(self):
    #     acoeffs_0_3, bcoeffs_0_3 = recover_fourier_coeffs_in_range('Guitar/Guitar_A.wav', lower_k=0, upper_k=3)
    #     gt_acoeffs_0_3 = [-1.9655337597097, -0.01041777725028438, 0.0007193855463934214, -0.010668891764580152]
    #     gt_bcoeffs_0_3 = [0.0037368997636770688, -0.005942155223967613, -0.007589167312960408]
    #     print(acoeffs_0_3)
    #     print(bcoeffs_0_3)
        
    #     for i in range(len(acoeffs_0_3)):
    #         assert abs(acoeffs_0_3[i] - gt_acoeffs_0_3[i]) < 1e-3

    #     for i in range(len(bcoeffs_0_3)):
    #         assert abs(bcoeffs_0_3[i] - gt_bcoeffs_0_3[i]) < 1e-3

    #     acoeffs_200_210, bcoeffs_200_210 = recover_fourier_coeffs_in_range('Guitar/Guitar_A.wav',
    #                                                                        lower_k=200, upper_k=210)
    #     print(acoeffs_200_210)
    #     print(bcoeffs_200_210)
        
    #     gt_acoeffs_200_210 = [0.13722870475409696, 0.10055640436382708, 0.11002012559696149, -0.12568215270645233,
    #                           -0.092242329291388, 0.03856262166517736, -0.009747777413318646, 0.04298561534440871,
    #                           0.18116733787453954, -0.126500431900981, -0.07207863616862037]
    #     gt_bcoeffs_200_210 = [-0.10627617684276534, -0.01088611185651106, 0.0553202741882532, -0.03366047808261343,
    #                           0.13368286315765812,  0.0951395517007761, -0.028563372760522013, 0.17982965274587778,
    #                           -0.09021503266256628, -0.0919161686765141, 0.14661621829438923]

    #     for i in range(len(acoeffs_200_210)):
    #         assert abs(acoeffs_200_210[i] - gt_acoeffs_200_210[i]) < 1e-3

    #     for i in range(len(bcoeffs_200_210)):
    #         assert abs(bcoeffs_200_210[i] - gt_bcoeffs_200_210[i]) < 1e-3


    # def test_beautiful_gypsy_lick_1_A7(self):
    #     lk, uk = 3518, 3522
    #     acoeffs, bcoeffs = recover_fourier_coeffs_in_range("Guitar/Beautiful_Gypsy_Lick_1.wav",
    #                                                        lower_k=lk, upper_k=uk)
    #     plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_1',
    #                           'A7', lower_k=lk, upper_k=uk)
    #     plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_1',
    #                           'A7', lower_k=lk, upper_k=uk)


    # def test_beautiful_gypsy_lick_1_D7(self):
    #     lk, uk = 2347, 2352
    #     acoeffs, bcoeffs = recover_fourier_coeffs_in_range("Guitar/Beautiful_Gypsy_Lick_1.wav",
    #                                                        lower_k=lk, upper_k=uk)
    #     plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_1',
    #                           'D7', lower_k=lk, upper_k=uk)
    #     plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_1',
    #                           'D7', lower_k=lk, upper_k=uk)

    # def test_beautiful_gypsy_lick_1_E7(self):
    #     lk, uk = 2636, 2639
    #     acoeffs, bcoeffs = recover_fourier_coeffs_in_range("Guitar/Beautiful_Gypsy_Lick_1.wav",
    #                                                        lower_k=lk, upper_k=uk)
    #     plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_1',
    #                           'E7', lower_k=lk, upper_k=uk)
    #     plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_1',
    #                           'E7', lower_k=lk, upper_k=uk)

    # def test_beautiful_gypsy_lick_1_G7(self):
    #     lk, uk = 3134, 3137
    #     acoeffs, bcoeffs = recover_fourier_coeffs_in_range("Guitar/Beautiful_Gypsy_Lick_1.wav",
    #                                                        lower_k=lk, upper_k=uk)
    #     plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_1',
    #                           'G7', lower_k=lk, upper_k=uk)
    #     plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_1',
    #                           'G7', lower_k=lk, upper_k=uk)

    # def test_beautiful_gypsy_lick_2_A7(self):
    #     lk, uk = 3518, 3522
    #     acoeffs, bcoeffs = recover_fourier_coeffs_in_range("Guitar/Beautiful_Gypsy_Lick_2.wav",
    #                                                        lower_k=lk, upper_k=uk)
    #     plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_2',
    #                           'A7', lower_k=lk, upper_k=uk)
    #     plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_2',
    #                           'A7', lower_k=lk, upper_k=uk)

    # def test_beautiful_gypsy_lick_2_D7(self):
    #     lk, uk = 2347, 2352
    #     acoeffs, bcoeffs = recover_fourier_coeffs_in_range("Guitar/Beautiful_Gypsy_Lick_2.wav",
    #                                                        lower_k=lk, upper_k=uk)
    #     plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_2',
    #                           'D7', lower_k=lk, upper_k=uk)
    #     plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_2',
    #                           'D7', lower_k=lk, upper_k=uk)

    # def test_beautiful_gypsy_lick_2_E7(self):
    #     lk, uk = 2636, 2639
    #     acoeffs, bcoeffs = recover_fourier_coeffs_in_range("Guitar/Beautiful_Gypsy_Lick_2.wav",
    #                                                        lower_k=lk, upper_k=uk)
    #     plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_2',
    #                           'E7', lower_k=lk, upper_k=uk)
    #     plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_2',
    #                           'E7', lower_k=lk, upper_k=uk)

    # def test_beautiful_gypsy_lick_2_G7(self):
    #     lk, uk = 3134, 3137
    #     acoeffs, bcoeffs = recover_fourier_coeffs_in_range("Guitar/Beautiful_Gypsy_Lick_2.wav",
    #                                                        lower_k=lk, upper_k=uk)
    #     plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_2',
    #                           'G7', lower_k=lk, upper_k=uk)
    #     plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Beautiful_Gypsy_Lick_2',
    #                           'G7', lower_k=lk, upper_k=uk)


    # def test_violin_A_A7(self):
    #     lk, uk = 3518, 3522
    #     acoeffs, bcoeffs = recover_fourier_coeffs_in_range("Violin/Violin_A.wav",
    #                                                        lower_k=lk, upper_k=uk)
    #     plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_A',
    #                           'A7', lower_k=lk, upper_k=uk)
    #     plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_A',
    #                           'A7', lower_k=lk, upper_k=uk)

    # def test_violin_A_D7(self):
    #     lk, uk = 2347, 2352
    #     acoeffs, bcoeffs = recover_fourier_coeffs_in_range("Violin/Violin_A.wav",
    #                                                        lower_k=lk, upper_k=uk)
    #     plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_A',
    #                           'D7', lower_k=lk, upper_k=uk)
    #     plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_A',
    #                           'D7', lower_k=lk, upper_k=uk)

    # def test_violin_A_E7(self):
    #     lk, uk = 2636, 2639
    #     acoeffs, bcoeffs = recover_fourier_coeffs_in_range("Violin/Violin_A.wav",
    #                                                        lower_k=lk, upper_k=uk)
    #     plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_A',
    #                           'E7', lower_k=lk, upper_k=uk)
    #     plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_A',
    #                           'E7', lower_k=lk, upper_k=uk)

    # def test_violin_A_G7(self):
    #     lk, uk = 3134, 3137
    #     acoeffs, bcoeffs = recover_fourier_coeffs_in_range("Violin/Violin_A.wav",
    #                                                        lower_k=lk, upper_k=uk)
    #     plot_recovered_coeffs(acoeffs, 'ACOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_A',
    #                           'G7', lower_k=lk, upper_k=uk)
    #     plot_recovered_coeffs(bcoeffs, 'BCOEFFS: RCD={}; RCV={} in [{},{}]', 'Violin_A',
    #                           'G7', lower_k=lk, upper_k=uk)
        
    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
