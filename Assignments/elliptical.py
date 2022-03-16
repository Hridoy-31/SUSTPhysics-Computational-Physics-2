#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 22:33:24 2022
@author: S.M. Raihanul Bashir Hridoy
Reg No. 2017132031
"""

'''
    Given the Laplace equation:
        Uxx + Uyy = 0
    and the following grid:

        1000    1000    1000    1000
          |       |       |       |
          |       |       |       |
        2000    u1,2    u2,2    500
          |       |       |       |
          |       |       |       |
        2000    u1,1    u2,1      0
          |       |       |       |
          |       |       |       |
        1000     500      0       0

    We have to find the values of the grid points u(1,1), u(1,2), u(2,1), u(2,2)
    by using the following interation method:
        1) Jacobian Method
        2) Gauss-Seidal Method
'''
# the formulas are represented by the functions
def standard_formula(a1, b1, c1, d1):
    return (a1+b1+c1+d1)/4 

def diagonal_formula(a1, b1, c1, d1):
    return (a1+b1+c1+d1)/4

#   At first, we are considering u(2,1) = 0
u_021 = 0

# using diagonal formula for getting the initial value for u(1,2)
u_012 = diagonal_formula(1000,1000,2000,u_021)

# using standard formula for getting the initial value for u(2,2)
u_022 = standard_formula(u_012,1000,500,u_021)

# using standard formula for getting the initial value for u(1,1)
u_011 = standard_formula(2000,u_012,u_021,500)

# using standard formula for getting the initial value for u(2,1)
u_021 = standard_formula(u_011,u_022,0,0)

u_11 = u_011
u_12 = u_012
u_21 = u_021
u_22 = u_022

print("Initial values of the grid points\n")
print("u(1,1) :", u_11)
print("u(1,2) :", u_12)
print("u(2,1) :", u_21)
print("u(2,2) :", u_22)
print()

# considering 20 iterations
iteration = 20

# Jacobian iterations of the grid points
print("Using Jacobian iteration method :\n")
for i in range(iteration):
    print("Interation:" + str(i+1))
    print()
    u_11 = standard_formula(2000,u_12,u_21,500)
    u_12 = standard_formula(2000,1000,u_22,u_11)
    u_21 = standard_formula(u_11,u_22,0,0)
    u_22 = standard_formula(u_12,1000,500,u_21)
    print("u(1,1) :", u_11)
    print("u(1,2) :", u_12)
    print("u(2,1) :", u_21)
    print("u(2,2) :", u_22)
    print()



# Gauss-Seidal iterations of the grid points
u_11 = u_011
u_12 = u_012
u_21 = u_021
u_22 = u_022
print("Using Gauss-Seidal iteration method: \n")
for i in range(iteration):
    print("Iteration :" + str(i+1))
    print()
    u_12 = standard_formula(2000,1000,u_22,u_11)
    u_11 = standard_formula(2000,u_12,u_21,500)
    u_22 = standard_formula(u_12,1000,500,u_21)
    u_21 = standard_formula(u_11,u_22,0,0)
    print("u(1,1) :", u_11)
    print("u(1,2) :", u_12)
    print("u(2,1) :", u_21)
    print("u(2,2) :", u_22)
    print()
