# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 10:13:29 2020

@author: Owner
"""
#f(x)=cos(pi*(theta)*x)exp(-x)
import matplotlib as plt
import numpy as np
θ_vals = np.linspace(0, 2, 10)
x = np.linspace(0, 5, 200)
fig, ax = plt.subplots()
for θ in θ_vals:
 ax.plot(x, np.cos(np.pi * θ * x) * np.exp(- x))
plt.show()