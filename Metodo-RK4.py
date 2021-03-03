#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 15:17:04 2021

@author: dylan
"""
def trunc(f, n): 
    '''Truncates/pads a float f to n decimal places without rounding''' 
    return ('%.*f' % (n + 1, f))[:-1]



f = lambda x,y: (2.0*x + 4.0*y)
g = lambda x,y: (-1.0*x + 6.0*y)

# TODO HARCODEADO PARA TESTEAR, FUNCIONA OK

t = 0.0
x = -1.0
y = 6.0
h = 0.2
i = 0

while(i < 3):
    m1 = f(x,y)
    k1 = g(x,y)

    m2 = f(x + m1*h/2, y + k1*h/2)
    k2 = g(x + m1*h/2, y + k1*h/2)

    m3 = f(x + m2*h/2, y + k2*h/2)
    k3 = g(x + m2*h/2, y + k2*h/2)

    m4 = f(x + m3*h, y + k3*h)
    k4 = g(x + m3*h, y + k3*h)

    print("mi ----- ki")
    print("{} - {} ".format(trunc(m1,3),trunc(k1,3)))
    print("{} - {} ".format(trunc(m2,3),trunc(k2,3)))
    print("{} - {} ".format(trunc(m3,3),trunc(k3,3)))
    print("{} - {} ".format(trunc(m4,3),trunc(k4,3)))

    print("---------------")

    x = x + (h/6)*(m1 + 2*m2 + 2*m3 + m4)
    y = y + (h/6)*(k1 + 2*k2 + 2*k3 + k4)

    print("{} - {}".format(x,y))
    i+=1