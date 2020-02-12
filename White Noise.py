# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 08:26:34 2020

@author: Owner
"""

#standar white noise process. each epsilon independent and normally dist'd
import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(100)
plt.plot(x)
plt.show()

#using loops
ts_length = 100
ϵ_values = []   # Empty list

for i in range(ts_length):
    e = np.random.randn()
    ϵ_values.append(e)

plt.plot(ϵ_values)
plt.show()

#factorial exercise
def factorial(n):
    factorial=1
if n<0:
    print("NA")
elif n ==0:
    print("factorial is 1")
else:
    for i in range(1, num+1):
        factorial=factorial*i
        print("factorial" "is")





    
