#!/usr/bin/python

############################################
# module: color_feasible_set.py
# description: graphing and coloring
# feasible sets.
# bugs to vladimir kulyukin via canvas.
############################################

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

"""
These are the  corner points for the SMP01 in
Lecture 07.

P1 = [32.0, 36.0]
P2 = [40.0, 20.0]
P3 = [0.0, 60.0]
P4 = [40.0, 0.0]]
P5 = [0.0, 0.0]
"""

def color_feasible_set_lec07_smp_01():
    ### 3x + 4y = 240
    def red_line(x): return -(3.0/4.0)*x + 60.0
    ### 2x +  y = 100
    def blue_line(x): return -2.0*x + 100.0
    xvals = np.linspace(0, 100, 10000)
    yvals1 = np.array([red_line(x) for x in xvals])
    yvals2 = np.array([blue_line(x) for x in xvals])
    
    fig1 = plt.figure(1)
    fig1.suptitle('Feasible Set for SMP 01 in CS3430: S24: Lecture 07')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([-10, 120])
    plt.xlim([-10, 120])
    ## green line
    x1, y1 = [40, 40], [0, 120]
    ## yellow line y = 0
    x2, y2 = [0, 120], [0, 0]
    ## black line x = 0
    x3, y3 = [0, 0], [0, 120]
    plt.grid()
    plt.plot(xvals, yvals1, label='3x+4y=240', c='red')
    plt.plot(xvals, yvals2, label='2x+y=100', c='blue')
    plt.plot(x1, y1, label='x=40', c='green')
    plt.plot(x2, y2, label='y=0', c='yellow')
    plt.plot(x3, y3, label='x=0', c='black')

    ### These are the corner points.
    poly_verts = np.array([[0.0, 0.0],
                           [0.0, 60.0],                           
                           [32.0, 36.0],
                           [40.0, 20.0],
                           [40.0, 0.0]],
                          dtype=float)
    poly = Polygon(poly_verts, closed=True, color='blue')
    ax = fig1.axes
    collection = PatchCollection([poly])
    ax[0].add_collection(collection)
    
    plt.legend(loc='best')
    plt.show()

if __name__ == '__main__':
    color_feasible_set_lec07_smp_01()    
    pass


