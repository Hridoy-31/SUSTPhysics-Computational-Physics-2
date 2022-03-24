#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 22:33:24 2022
@author: S.M. Raihanul Bashir Hridoy
Reg No. 2017132031
"""
'''
    Solving the boundary value problem
        Ut = Uxx
    subjected U(0,t) = U(1,t) = 0
    U(x,0) = sin(pi*x)
    0 <= x <= 1
    using Bender-Schmidt method 
    taking h = 0.2 and k = 0.02
'''
# importing the necessary libraries
from cProfile import label
import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return math.sin(math.pi*x)

# taking x interval h = 0.2 (given)
x = np.arange(0, 1.1, 0.2)

# taking y interval k = 0.02 (given)
t = np.arange(0, 0.11, 0.02)

print("When t = 0 :")
u1=0;u2=f(0.2);u3=f(0.4);u4=f(0.6);u5=f(0.8);u6=0
l0 = []
l0.append(u1);l0.append(u2);l0.append(u3);l0.append(u4);l0.append(u5);l0.append(u6);
print(l0)
print()

# using Bender-Schmidt iteration method
u12 = (u1+u3)/2
u13 = (u2+u4)/2
u14 = (u3+u5)/2
u15 = (u4+u6)/2

print("When t = 0.02 :")
l1 = []
l1.append(u1);l1.append(u12);l1.append(u13);l1.append(u14);l1.append(u15);l1.append(u6);
print(l1)
print()

print("When t = 0.04 :")
u22 = (u1+u13)/2
u23 = (u12+u14)/2
u24 = (u13+u15)/2
u25 = (u14+u6)/2
l2 = []
l2.append(u1);l2.append(u22);l2.append(u23);l2.append(u24);l2.append(u25);l2.append(u6);
print(l2)
print()

print("When t = 0.06 :")
u32 = (u1+u23)/2
u33 = (u22+u24)/2
u34 = (u23+u25)/2
u35 = (u24+u6)/2
l3 = []
l3.append(u1);l3.append(u32);l3.append(u33);l3.append(u34);l3.append(u35);l3.append(u6);
print(l3)
print()

print("When t = 0.08 :")
u42 = (u1+u33)/2
u43 = (u32+u34)/2
u44 = (u33+u35)/2
u45 = (u34+u6)/2
l4 = []
l4.append(u1);l4.append(u42);l4.append(u43);l4.append(u44);l4.append(u45);l4.append(u6);
print(l4)
print()

print("When t = 0.1 :")
u52 = (u1+u43)/2
u53 = (u42+u44)/2
u54 = (u43+u45)/2
u55 = (u44+u6)/2
l5 = []
l5.append(u1);l5.append(u52);l5.append(u53);l5.append(u54);l5.append(u55);l5.append(u6);
print(l5)
print()

# U vs x plotting
plt.plot(x,l0, '.-', label="t = 0")
plt.plot(x,l1, '.-', label="t = 0.02")
plt.plot(x,l2, '.-', label="t = 0.04")
plt.plot(x,l3, '.-', label="t = 0.06")
plt.plot(x,l4, '.-', label="t = 0.08")
plt.plot(x,l5, '.-', label="t = 0.1")
plt.xlabel("Value of X")
plt.ylabel("Value of U")
plt.legend()
plt.title("U vs X in every timestamp")
plt.show()

lt0 = np.zeros(6); lt5 = np.zeros(6)
lt1 = []; lt2 = []; lt3 = []; lt4 = []; 
lt1.append(u2);lt1.append(u12);lt1.append(u22);lt1.append(u32);lt1.append(u42);lt1.append(u52);
lt2.append(u3);lt2.append(u13);lt2.append(u23);lt2.append(u33);lt2.append(u43);lt2.append(u53);
lt3.append(u4);lt3.append(u14);lt3.append(u24);lt3.append(u34);lt3.append(u44);lt3.append(u54);
lt4.append(u5);lt4.append(u15);lt4.append(u25);lt4.append(u35);lt4.append(u45);lt4.append(u55);

print("When x = 0 :")
print(lt0)
print()

print("When x = 0.2 :")
print(lt1)
print()

print("When x = 0.4 :")
print(lt2)
print()

print("When x = 0.6 :")
print(lt3)
print()

print("When x = 0.8 :")
print(lt4)
print()

print("When x = 1 :")
print(lt5)

# U vs t plotting
# here ---- graph denote the graph overlapping
plt.plot(t,lt0, '--', label="x = 0")
plt.plot(t,lt1, '--', label="x = 0.2")
plt.plot(t,lt2, '--', label="x = 0.4")
plt.plot(t,lt3, '.-', label="x = 0.6")
plt.plot(t,lt4, '.-', label="x = 0.8")
plt.plot(t,lt5, '.-', label="x = 1")
plt.xlabel("Value of T")
plt.ylabel("Value of U")
plt.legend()
plt.title("U vs T in every timestamp")
plt.show()
