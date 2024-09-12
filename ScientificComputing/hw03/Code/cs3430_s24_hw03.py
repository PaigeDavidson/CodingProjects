###############################################
# module: cs3430_s24_hw03.py
# description: CS3430: S24: HW03
# YOUR NAME: Paige Davidson
# YOUR A-NUMBER: A02339425
###############################################

import numpy as np
import numpy.linalg
import matplotlib.pyplot as plt
import math

### ============= Problem 1 =======================

def line_ip(line1, line2):
    '''
    line_ip(line1, line2) where line1 and line2 are
    3-tuples of floats (A, B, C), e.g., (4.0, 3.0, 380.0).

    finds corner points
    '''
    A = np.array([[line1[0], line1[1]],
                  [line2[0], line2[1]]],
                  dtype=float)
    b = np.array([[line1[2]],
                  [line2[2]]], 
                  dtype=float)
    try: 
        x = np.linalg.solve(A, b)
        return x
    except:
        return None

### This is the same as the static method
### cs3430_s24_hw03_uts.check_line_ip().
def check_line_ip(line1, line2, ip, err=0.0001):
    assert ip is not None
    A1, B1, C1 = line1
    A2, B2, C2 = line2
    x, y = ip[0, 0], ip[1, 0]
    assert np.allclose(abs((A1*x + B1*y) - C1), err)
    assert np.allclose(abs((A2*x + B2*y) - C2), err)
    return True

## Be careful not to compute the same intersection twice.
## In other words, if l1 and l2 are two lines, the
## intersection point b/w l1 and l2 is the same as the
## intersection point b/w l2 and l1. Computing duplicate
## intersections will not render the required computation
## incorrect, but it will make it more efficient.
def find_line_ips(lines):
    cps = []
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            cps.append(line_ip(lines[i], lines[j]))
    return cps

def max_obj_fun(f, cps):
    """
    maximize obj fun f on corner points cps
    """
    MaxVal = 0
    maximized = ()
    for i in cps:
        # compute function with points, return the biggest one
        value = f(i[0], i[1])
        if value > MaxVal:
            MaxVal = value
            point = i
    maximized = (point, MaxVal)
    return maximized

def min_obj_fun(f, cps):
    """
    minimize obj fun f on corner points cps
    """
    minVal = math.inf
    minimized = ()
    for i in cps:
        # compute function with points, return the smallest one
        value = f(i[0], i[1])
        if value < minVal:
            minVal = value
            point = i
    minimized = (point, minVal)
    return minimized

### ================ Coding Lab ======================
### Graphing constraints to the Ted's Toys problem we worked
### out in CS3430: S24: Lecture 05.
def plot_teds_constraints():
    ### plastic constraint: 4x + 3y <= 480
    def plastic_constraint(x): return -(4/3.0)*x + 160.0
    ### steel constraints: 3x + 6y <= 720
    def steel_constraint(x): return -0.5*x + 120.0
    xvals  = np.linspace(0, 160, 10000)
    yvals1 = np.array([plastic_constraint(x) for x in xvals])
    yvals2 = np.array([steel_constraint(x) for x in xvals])
    fig1   = plt.figure(1)
    fig1.suptitle('Ted\'s Toys Problem')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([-5, 160])
    plt.xlim([-5, 160])
    ## x = 0
    x1, y1 = [0, 0], [0, 160]
    ## y = 0
    x2, y2 = [0, 160], [0, 0]
    plt.grid()
    plt.plot(xvals, yvals1, label='4x+3y=480', c='red')
    plt.plot(xvals, yvals2, label='3x+6y=720', c='blue')
    plt.plot(x1, y1, label='x=0', c='green')
    plt.plot(x2, y2, label='y=0', c='yellow')
    plt.legend(loc='best')
    plt.show()

def teds_problem():
    red_line    = (4, 3, 480)
    blue_line   = (3, 6, 720)
    green_line  = (1, 0, 0)
    yellow_line = (0, 1, 0)

    cp1 = line_ip(green_line, yellow_line)
    cp2 = line_ip(green_line, blue_line)
    cp3 = line_ip(blue_line, red_line)
    cp4 = line_ip(red_line, yellow_line)

    obj_fun = lambda x, y: 5.0*x + 4.0*y

    rslt = max_obj_fun(obj_fun, [cp1, cp2, cp3, cp4])

    x = rslt[0][0][0]
    y = rslt[0][1][0]
    p = rslt[1]

    print('num cars   = {}'.format(x))
    print('num trucks = {}'.format(y))
    print('profit     = {}'.format(p))

    return x, y, p

### =============== Problem 2 ========================
    
def problem_2():
    red_line    = (1.0, 1.0, 3.0)
    blue_line   = (3.0, -1.0, -1.0)
    purple_line = (1, 0, 2)

    cp1 = line_ip(red_line, blue_line)
    cp2 = line_ip(blue_line, purple_line)
    cp3 = line_ip(red_line, purple_line)

    obj_fun = lambda x, y: 3.0*x + y


    rslt = max_obj_fun(obj_fun, [cp1, cp2, cp3])

    x = rslt[0][0][0]
    y = rslt[0][1][0]
    p = rslt[1]

    print('Constraint 1   = {}'.format(x))
    print('Constraint 2 = {}'.format(y))
    print('profit     = {}'.format(p))

    return x, y, p

def plot_problem_2_constraints():
    # constraint one: x + y >= 3
    def constraintOne(x): return -(1)*x + 3
    # constraint two: 3x - y >= -1
    def constraintTwo(x): return (3)*x + 1

    xvals  = np.linspace(0, 4, 10000)
    yvals1 = np.array([constraintOne(x) for x in xvals])
    yvals2 = np.array([constraintTwo(x) for x in xvals])

    fig1 = plt.figure(1)
    fig1.suptitle('CS3430: S24: Problem 2 Constraints')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.ylim([-1, 10])
    plt.xlim([-1, 10])
    ## x <=2 0
    x1, y1 = [2, 2], [0, 10]
    
    plt.grid()
    plt.plot(xvals, yvals1, label='x+y= 3', c='red')
    plt.plot(xvals, yvals2, label='3x-y=-1', c='blue')
    plt.plot(x1, y1, label='x=2', c='purple')

    plt.legend(loc='best')
    plt.show()

## =============== Problem 3 ==================
 
def plot_problem_3_constraints():
    ### constraintOne: x+2y≥6
    def constraintOne(x): return -(1/2.0)*x + 3
    ### constraintTwo: x−y≥−4
    def constraintTwo(x): return x + 4
    # constraintThree: 2x+y≤8.
    def constraintThree(x): return -(2)*x + 8


    xvals  = np.linspace(0, 10, 10000)
    yvals1 = np.array([constraintOne(x) for x in xvals])
    yvals2 = np.array([constraintTwo(x) for x in xvals])
    yvals3 = np.array([constraintThree(x) for x in xvals])

    fig1 = plt.figure(1)
    fig1.suptitle('CS3430: S24: Problem 3 Constraints')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([-1, 10])
    plt.xlim([-1, 10])
    ## x = 0
    x1, y1 = [0, 0], [0, 10]
    ## y = 0
    x2, y2 = [0, 10], [0, 0]
    plt.grid()
    plt.plot(xvals, yvals1, label='x+2y=6', c='magenta')
    plt.plot(xvals, yvals2, label='x-y=-4', c='blue')
    plt.plot(xvals, yvals3, label='2x+y=8', c='purple')
    plt.plot(x1, y1, label='x=0', c='green')
    plt.plot(x2, y2, label='y=0', c='yellow')
    plt.legend(loc='best')
    plt.show()

       
def problem_3():
    red_line    = (1, 2, 6)
    blue_line   = (1, -1, -4)
    purple_line = (2, 1, 8)
    yellow_line = (0, 1, 0)

    cp1 = line_ip(purple_line, yellow_line)
    cp2 = line_ip(purple_line, blue_line)
    cp3 = line_ip(blue_line, red_line)
    cp4 = line_ip(red_line, yellow_line)


    obj_fun = lambda x, y: x + y

    rslt = max_obj_fun(obj_fun, [cp1, cp2, cp3, cp4])

    x = rslt[0][0][0]
    y = rslt[0][1][0]
    p = rslt[1]

    print('x-value  = {}'.format(x))
    print('y-value = {}'.format(y))
    print('profit     = {}'.format(p))

    return x, y, p



### ================= Problem 4 =================

def plot_problem_4_constraints():
    ### constraintOne: 0.8x+0.2y≥90
    def carb_constraint(x): return -(0.8/0.2)*x + (90/0.2)
    ### constraintTwo: 3x+6y≥600
    def cal_constraint(x): return -(3.0/6.0)*x + 100

    xvals  = np.linspace(0, 400, 10000)
    yvals1 = np.array([carb_constraint(x) for x in xvals])
    yvals2 = np.array([cal_constraint(x) for x in xvals])

    fig1 = plt.figure(1)
    fig1.suptitle('CS3430: S24: Problem 4 Constraints')
    plt.xlabel('x')
    plt.ylabel('y')
    
    plt.ylim([-10, 500])
    plt.xlim([-10, 500])
    ## x = 0
    x1, y1 = [0, 0], [0, 500]
    ## y = 0
    x2, y2 = [0, 500], [0, 0]
    plt.grid()
    plt.plot(xvals, yvals1, label='0.8x+0.2y≥90', c='cyan')
    plt.plot(xvals, yvals2, label='3x+6y≥600', c='blue')
    plt.plot(x1, y1, label='x=0', c='orange')
    plt.plot(x2, y2, label='y=0', c='yellow')
    plt.legend(loc='best')
    plt.show()

def problem_4():
    red_line    = (0.8, 0.2, 90)
    blue_line   = (3, 6, 600)
    green_line  = (1, 0, 0)
    yellow_line = (0, 1, 0)

    cp1 = line_ip(green_line, yellow_line)
    cp2 = line_ip(green_line, blue_line)
    cp3 = line_ip(blue_line, red_line)
    cp4 = line_ip(red_line, yellow_line)

    # cost function to minimize
    obj_fun = lambda x, y: 4.0*x + 5.0*y

    rslt = max_obj_fun(obj_fun, [cp1, cp2, cp3, cp4])

    x = rslt[0][0][0]
    y = rslt[0][1][0]
    p = rslt[1]

    print('x-value  = {}'.format(x))
    print('y-value = {}'.format(y))
    print('profit     = {}'.format(p))

    return x, y, p