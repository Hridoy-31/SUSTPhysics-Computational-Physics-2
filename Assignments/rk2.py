#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 22:53:24 2021
@author: S.M. Raihanul Bashir Hridoy
Reg No. 2017132031
"""

'''
    Given a second order differential equation d2x/dt2 = -(k/m)x
    where,
    k/m = 1
    x(0) = x0 = 1
    v(0) = x'(0) = 0
    h = 0.1

    Converting this second order differential equation into a
    system of first order differential equations, we get,

    dx/dt = v .......................(i)
    dv/dt = -(k/m)x ..................(ii)
'''

import numpy as np
import matplotlib.pyplot as plt

def harmonic_eq(x,t,k):
    # considering k/m as a k for variable simplicity
    return x[1], - k*x[0]

def rk2(x, func,t, k, dt) :
    '''
    2nd order Runge-Kutta method for solving Ordinary
    differential equations
    
    y(n+1) = y(n) + (1/2)*(k1+k2)

    where, 
        k1 = hf(xn,yn)
        k2 = hf(xn+h, yn+k1)
    '''
    # for storing the values of k1 & k2
    temp1 = np.zeros(2) 
    temp2 = np.zeros(2)
    temp1 = func(x,t,k) # k1 = hf(x0,y0)
    temp2 = func([x[0]+temp1[0]*dt, x[1]+temp1[1]*dt], t, k) # k2 = hf(x0+h, y0+k1)
    val1 = x[0] + dt/2.0 * (temp1[0] + temp2[0])
    val2 = x[1] + dt/2.0 * (temp1[1] + temp2[1])
    return val1, val2

def plotting(method, equation, k, dt, n_steps):
    t = np.arange(0, n_steps*dt, dt)
    x = np.zeros((n_steps,2))
    # Given initial position
    x[0][0] = 1.0
    for i in range(n_steps-1): 
        x[i+1] = method(x[i],harmonic_eq, t[i], k, dt)
    
    plt.plot(t, x[:,0], 'r', label="$x(t)$")
    plt.plot(t, x[:,1], 'b', label="$v(t)$")
    plt.xlabel("$t$")
    
    
    plt.legend(loc='upper right')
    plt.show()

if __name__ == "__main__" :
    # step size
    dt = 0.1
    # number of steps
    n_step = 100
    # initial value of (k/m)
    k = 1
    plotting(rk2, harmonic_eq, k, dt, n_step)