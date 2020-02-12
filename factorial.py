# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 09:00:53 2020

@author: Owner
"""

def factorial(n): 
  
    # single line to find factorial 
    return 1 if (n==1 or n==0) else n * factorial(n - 1)  