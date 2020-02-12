# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 09:25:06 2020

@author: Owner
"""
import numpy as np
import matplotlib.pyplot as plt

x = [np.random.randn() for i in range(100)]
plt.plot(x, label="white noise")
plt.legend()
plt.show()
αs = [0.0, 0.8, 0.98]
ts_length = 200

for α in αs:
    x_values = []
    current_x = 0
    for i in range(ts_length):
        x_values.append(current_x)
        current_x = α * current_x + np.random.randn()
    plt.plot(x_values, label=f'$\\alpha = {α}$')
plt.legend()
plt.show()
