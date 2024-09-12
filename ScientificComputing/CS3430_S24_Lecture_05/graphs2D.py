
############################################
# module: graphs2D.py
# description: graphing lines in 2D with
# matplotlib.
# bugs to vladimir kulyukin in canvas
############################################

import numpy as np
import matplotlib.pyplot as plt

def lec_05_01():
    def f1(x): return -1.5*x + 3.0
    xvals = np.linspace(-2, 2, 10000)
    yvals1 = np.array([f1(x) for x in xvals])
    fig1 = plt.figure(1)
    fig1.suptitle('3x + 2y = 6')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([0, 4])
    plt.xlim([0, 2])
    plt.grid()
    plt.plot(xvals, yvals1, label='y=-1.5x + 3', c='r')
    plt.legend(loc='best')
    plt.show()

def lec_05_02():
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

def lec_05_03():
    def f1(x): return 3.0 - (3.0/4.0)*x
    def f2(x): return 0.5*x
    xvals = np.linspace(0, 5, 10000)
    yvals1 = np.array([f1(x) for x in xvals])
    yvals2 = np.array([f2(x) for x in xvals])
    fig1 = plt.figure(1)
    fig1.suptitle('Intersection of 3 lines')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([0, 4])
    plt.xlim([0, 5])
    x1, y1 = [1, 1], [0, 4]
    plt.grid()
    plt.plot(xvals, yvals1, label='3x+4y=12', c='r')
    plt.plot(xvals, yvals2, label='x=2y', c='b')
    plt.plot(x1, y1, label='x=1', c='g')
    plt.legend(loc='best')
    plt.show()

def lec_05_lp_problem_03():
    def y(x): return (-15/8)*x + (60/8)
    xvals = np.linspace(-2, 10, 10000)
    yvals1 = np.array([y(x) for x in xvals])
    yvals = np.linspace(-2, 10, 10000)
    zero_x = np.linspace(0, 0, 10000)
    zero_y = np.linspace(0, 0, 10000)
    fig1 = plt.figure(1)
    fig1.suptitle('CS3430: S24: Lecture 05: LP Problem 3')
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


if __name__ == '__main__':
    lec_05_01()
    lec_05_02()
    lec_05_03()
    lec_05_lp_problem_03()
    pass


