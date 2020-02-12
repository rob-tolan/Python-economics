# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 09:20:37 2020

@author: Owner
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

def timeseries(α,T):
      x = [0]
      ε = np.random.randn(T)
      for t in range(T):
            x.append(α*x[t-1]+ε[t])
      return x
T = int(input('Please input the T:'))
α = float(input('Please input the α：'))
plt.figure(figsize=(10,5))
plt.plot(timeseries(α,T+1),color = 'Hotpink',label = 'x')
plt.legend()