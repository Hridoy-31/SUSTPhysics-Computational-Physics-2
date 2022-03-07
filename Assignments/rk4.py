#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 11:46:24 2021
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

def rk4(x, func,t, k, dt) :
    '''
    4th order Runge-Kutta method for solving Ordinary
    differential equations
    
    y(n+1) = y(n) + (1/6)*(k1+2k2+2k3+k4)

    where, 
        k1 = hf(xn,yn)
        k2 = hf(xn+h/2, yn+k1/2)
        k3 = hf(xn+h/2, yn+k2/2)
        k4 = hf(xn+h, yn+k3)
    '''
    # for storing the values of k1,k2,k3 and k4
    temp1 = np.zeros(2)
    temp2 = np.zeros(2)
    temp3 = np.zeros(2)
    temp4 = np.zeros(2)
    temp1 = func(x,t,k) # k1 = hf(xn,yn)
    temp2 = func([x[0]+temp1[0]*dt/2, x[1]+temp1[1]*dt/2], t, k) # k2 = hf(xn+h/2, yn+k1/2)
    temp3 = func([x[0]+temp1[0]*dt/2, x[1]+temp2[1]*dt/2], t, k) # k3 = hf(xn+h/2, yn+k2/2)
    temp4 = func([x[0]+temp1[0]*dt, x[1]+temp3[1]*dt], t, k) # k4 = hf(xn+h, yn+k3)
    val1 = x[0] + dt/6.0 * (temp1[0] + 2*temp2[0] + 2*temp3[0] + temp4[0])
    val2 = x[1] + dt/6.0 * (temp1[1] + 2*temp2[1] + 2*temp3[1] + temp4[1])
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
    k= 1
    plotting(rk4, harmonic_eq, k, dt, n_step)
