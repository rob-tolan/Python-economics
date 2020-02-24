# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 19:15:13 2019

@author: Owner
"""
import numpy as np
#problem set 1
#utility function
def u(x1,x2,alpha=0.5,beta=1):
    return (alpha*x1**(-beta) + (1-alpha)*x2**(-beta))**(-1/beta)
#optimisation problem for min f((x) = min sin(x)+0.05*x**2
#note how function is open on R so can't be solved ananlytically
def f(x):
    return np.sin(x)+0.05*x**2

N = 100
x_vec = np.linspace(-10,10,N)
f_vec = np.empty(N)

f_best = np.inf # initial maximum
x_best = np.nan # not-a-number

for i,x in enumerate(x_vec):
    f_now = f_vec[i] = f(x)
    if f_now < f_best:
        x_best = x
        f_best = f_now
#can use scipy
#utility maximisation with five goods
def utility_function(x,alpha):
   u = 1
   alpha = np.ones(5)/5
p = np.array([1,2,3,4,5])
I = 10

for x_now,alpha_now in zip(x,alpha):
        u *= np.max(x_now,0)**alpha_now
return u 



