#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 20:43:29 2023

@author: ashercohen
"""
import numpy as np
from matplotlib import pyplot as plt

def f(x, y):
    return 3 * np.power(x, 2)

def find_k1(f, x0, y0, h = .1):
    return f(x0, y0)

def find_k2(f, k1, x0, y0, h = .1):
    return f(x0 + (h/2), y0 + ((h/2) * k1))

def find_k3(f, k2, x0, y0, h = .1):
    return f(x0 + (h/2), y0 + ((h/2) * k2))

def find_k4(f,k3, x0, y0, h = .1):
    return f(x0 + h, y0 + (h * k3))

def yNext(y0, x0, k1, k2, k3, k4, h = .1):
    return y0 + ((h/6) * (k1 + (2 * k2) + (2 * k3) + k4))

def doIt(f, y0, x0, yNext, number = 10, h = .1):
    xVal = [x0]
    yVal = [y0]
    xVal = list(xVal)
    yVal = list(yVal)
    for i in range(number):
        k1 = find_k1(f, xVal[i], yVal[i], h)
        k2 = find_k2(f, k1, xVal[i], yVal[i], h)
        k3 = find_k3(f, k2, xVal[i], yVal[i], h)
        k4 = find_k4(f, k3, xVal[i], yVal[i], h)
        
        yUsing = yNext(yVal[i], xVal[i], k1, k2, k3, k4, h)
        xUsing = xVal[i] + h
        
        xVal.append(xUsing)
        yVal.append(yUsing)
    
    return xVal, yVal

x, y = doIt(f, 0, -1, yNext, 200, .01)

plt.plot(x, y)

plt.show()
    
    
    
    
    