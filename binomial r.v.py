# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 09:05:23 2020

@author: Owner
"""
import numpy as np
def factorial(n):
      if n < 2:
            return 1
      else:
            return n*factorial(n-1)
u = np.random.normal(0,1)
N = int(input("Please input the N value："))
u=np.random.normal(0,1)
def binomial_rv(n,p):
    y=p**n*(1-p)**(N-n)*factorial(N)/factorial(n)*factorial(N-n)
    return y
n = int(input("Please input the n value:"))
p = float(input("Please input the p value:"))
print(binomial_rv(n,p))
