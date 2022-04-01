#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 22:33:24 2022
@author: Showrav Acharjee & Tanver Hossain Refat 
Reg No. 2017132066 & 2017132007
"""

# Importing necessary libraries
from matplotlib import pyplot as plt
import numpy as np

# Initial conditions 
xn = 1
yn = 1
zn = 1

# for different conditions, change the a,b,c variables for different systems
a = 10 # denoting system 3
b = 8/3 # denoting system 3
c = 38 # denoting system 3

# Step size
h = 0.01

# Runge-Kutta 4th Order
t_sol = []
x_sol = []
y_sol = []
z_sol = []

for i in np.arange(0, 100, 0.01):
    k1 = a*h*(yn-xn)
    l1 = h*(c*xn-xn*zn-yn)
    m1 = h*(xn*yn-b*zn)

    k2 = a*h*(yn-(xn+k1/2))
    l2 = h*(c*xn-xn*zn-(yn+l1/2))
    m2 = h*(xn*yn-b*(zn+m1/2))

    k3 = a*h*(yn-(xn+k2/2))
    l3 = h*(c*xn-xn*zn-(yn+l2/2))
    m3 = h*(xn*yn-b*(zn+m2/2))

    k4 = a*h*(yn-(xn+k3))
    l4 = h*(c*xn-xn*zn-(yn+l3))
    m4 = h*(xn*yn-b*(zn+m3))

    xn_1 = xn + 1/6 * (k1 + 2*k2 + 2*k3 + k4)
    yn_1 = yn + 1/6 * (l1 + 2*l2 + 2*l3 + l4)
    zn_1 = zn + 1/6 * (m1 + 2*m2 + 2*m3 + m4)

    t_sol.append(i)
    x_sol.append(xn_1)
    y_sol.append(yn_1)
    z_sol.append(zn_1)

    xn = xn_1
    yn = yn_1
    zn = zn_1

# Plotting
plt.style.use('classic') # used for classic plotting
plt.subplot(3, 1, 1)
plt.title('x vs t')
plt.plot(t_sol, x_sol, label='x')
plt.subplot(3, 1, 2)
plt.title('y vs t')
plt.plot(t_sol, y_sol,'g', label='y')
plt.subplot(3, 1, 3)
plt.title('z vs t')
plt.xlabel('time')
plt.plot(t_sol, z_sol,'r', label='z')
plt.show()