# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 12:28:08 2023

@author: pmong
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.sin(np.arange(20) / 2)
plt.plot(x)
plt.show()

x = np.linspace(-5,5,100)
y = np.cos(x)
plt.plot(x,y)
plt.title("TITLEEE")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()

plt.plot(np.sin(x))
plt.plot(np.cos(x))
plt.show()

x0 = np.random.randn(100)
x1 = np.random.randn(100)
plt.scatter(x0,x1)
plt.show()

y = np.arange(100) % 2
plt.scatter(x0, x1, c=y)
plt.show()



