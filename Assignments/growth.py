#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 8 11:43:24 2021
@author: S.M. Raihanul Bashir Hridoy
Reg No. 2017132031
"""

'''
    Given an ordinary differential equation dx/dt = ax
    where,
    a = 1
    x(0) = x0 = 1
    h = 0.1
'''


import numpy as np
import matplotlib.pyplot as plt
import math

def Euler(f,y0,t):
    '''
    f : function
        Right-hand side of the differential equation y'=f(t,y), y(t_0)=y_0
    y0 : number
        Initial value y(t0)=y0 where t0 is the entry at index 0 in the array t
    t : array
        1D NumPy array of t values where we approximate y values. Time step
        at each iteration is given by t[n+1] - t[n].
    y : 1D NumPy array
        Approximation y[n] of the solution y(t_n) computed by Euler's method.
    '''
    y = np.zeros(len(t))
    y[0] = y0
    for n in range(0,len(t)-1):
        y[n+1] = y[n] + f(y[n],t[n])*(t[n+1] - t[n])
    return y

def Taylor(t,y0):
    '''
    Taylor expansion calculation upto 8th term
    '''
    z = []
    for n in range(0, len(t)):
        total = 0
        for i in range(8):
            sub_term = ((y0* t[n]**i)/math.factorial(i))
            total += sub_term
        z.append(total)
    return z

# Taking h = 0.1 from 0 to 5 along the x-axis
t = np.linspace(0,5,num=50)
# Inital value
y0 = 1
# The given differential equation
f = lambda y,t: y
# Euler Method
y = Euler(f,y0,t)
# Taylor Method
z = Taylor(t,y0)
# Actual solution to check deviation from the exact
y_true = y0*np.exp(t)
plt.autoscale(enable=True, axis='both', tight=None)
plt.plot(t,z,'g.-',t,y,'b.-',t,y_true,'r-')
plt.legend(['Taylor','Euler','True'])
plt.xlabel("Time")
plt.ylabel("Number of nuclei")
plt.axis([0,6,0,140])
plt.title("Growth curve, x(0)=$1$")
plt.show()