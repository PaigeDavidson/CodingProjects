############################################
# module: cs3430_s24_lecture_06.py
# description: graphing lines in 2D with
# matplotlib for the problems discussed in
# F2F lecture 06 on 01/29/2024.
# Please take a look at graph2D.py in
# the zip of Lecture 05. There is some overlap.
# This file has a few more examples of using
# matplolib to do 2D plotting.
# bugs to vladimir kulyukin in canvas.
############################################

import numpy as np
import matplotlib.pyplot as plt

def lec_06_example_01():
    def y(x): return (-15/8)*x + (60/8)
    xvals = np.linspace(-2, 10, 10000)
    yvals1 = np.array([y(x) for x in xvals])
    yvals = np.linspace(-2, 10, 10000)
    zero_x = np.linspace(0, 0, 10000)
    zero_y = np.linspace(0, 0, 10000)
    fig1 = plt.figure(1)
    fig1.suptitle('CS3430: S24: Lecture 06: Example 01')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([-2, 10])
    plt.xlim([-2, 10])
    plt.grid()
    plt.plot(xvals, zero_y, label='y=0', c='r')
    plt.plot(zero_x, yvals, label='x=0', c='b')
    plt.plot(xvals, yvals1, label='y=(-15/8)x + (60/8)', c='g')
    plt.legend(loc='best')
    plt.show()

def lec_06_example_02():
    def y1(x): return 0.5*x
    def y2(x): return (-3/4.0)*x + 3
    xvals = np.linspace(-2, 10, 10000)
    xvals1 = np.linspace(1, 1, 10000)
    yvals = np.linspace(-2, 10, 10000)
    yvals2 = np.array([y1(x) for x in xvals])
    yvals3 = np.array([y2(x) for x in xvals])
    fig1 = plt.figure(1)
    fig1.suptitle('CS3430: S24: Lecture 06: Example 02')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([-2, 5])
    plt.xlim([-2, 5])
    plt.grid()
    plt.plot(xvals1, yvals, label='x=1', c='r')
    plt.plot(xvals, yvals2, label='y=0.5x', c='b')
    plt.plot(xvals, yvals3, label='y=(-3/4)*x + 3', c='g')
    plt.legend(loc='best')
    plt.show()

### a couple more function plotting examples.
def fun_plot_1():
    def f1(x): return 600.0/80.0 - (150.0/80.0)*x
    xvals = np.linspace(0, 5, 10000)
    yvals1 = np.array([f1(x) for x in xvals])
    fig1 = plt.figure(1)
    fig1.suptitle('150x + 80y = 600')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([0, 10])
    plt.xlim([0, 5])
    plt.grid()
    plt.plot(xvals, yvals1, label='150x + 80y = 600', c='r')
    plt.legend(loc='best')
    plt.show()

def fun_plot_2():
    ### 3x + 4y = 240
    def red_line(x): return -(3.0/4.0)*x + 80.0
    ### 2x +  y = 100
    def blue_line(x): return -2.0*x + 100.0
    xvals = np.linspace(0, 100, 10000)
    yvals1 = np.array([red_line(x) for x in xvals])
    yvals2 = np.array([blue_line(x) for x in xvals])
    fig1 = plt.figure(1)
    fig1.suptitle('Intersection of 3 lines')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([-10, 120])
    plt.xlim([-10, 120])
    x1, y1 = [40, 40], [0, 120]
    plt.grid()
    plt.plot(xvals, yvals1, label='3x+4y=12', c='red')
    plt.plot(xvals, yvals2, label='2x+y=100', c='blue')
    plt.plot(x1, y1, label='x=40', c='green')
    plt.legend(loc='best')
    plt.show()

if __name__ == '__main__':
    lec_06_example_01()
    lec_06_example_02()
    #fun_plot_1()
    #fun_plot_2()
    pass


