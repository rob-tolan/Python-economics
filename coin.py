# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 09:19:13 2020

@author: Owner
"""

from numpy.random import randint

x = randint(0,2,10).tolist()
j = 0
for i in range(len(x)-2):
      if x[i] == 1 and x[i+1] == 1 and x[i+2] == 1:
            j = j + 1
if j >= 1:
      print("You pay one dollar.")
else:
      print("You pay nothing.")