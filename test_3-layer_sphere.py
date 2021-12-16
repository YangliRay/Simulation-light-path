# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 17:21:22 2021

@author: 1229290416
"""

import lightpath as lp
import numpy as np
import matplotlib.pyplot as plt

plt.ylim(-0.5, 3)
#Refrective index between multiple medium
q = 1.2
p = 1.1
index = [q, 1/q, p, 1/p, 0]
index2 = [p, 1/p, 0]

#Range of observation
minimum = 1.8
maximum = 10.2

#Shape of lens
def h(x):
    if x >= 2 and x <= 2.5:
        return (np.sqrt(16 - (x - 6)**2))
    
    elif x > 2.5 and x <= 3:
        return (np.sqrt(16 - (x + 1)**2))
    
    elif x >= 4.367 and x <= 5:
        return (np.sqrt(36 - (x + 1)**2))
    
    elif x >= 4 and x < 4.367:
        return (np.sqrt(100 - (x - 14)**2))

    else: #Out side the domain
        return -99999



#Draw lens
def f2(x):
    return (np.sqrt(16 - (x - 6)**2))

x=np.linspace(2, 2.5, 1000)
ff=f2(x)
plt.plot(x, ff, color = 'black')


def f3(x):
    return (np.sqrt(16 - (x + 1)**2))

x=np.linspace(2.5, 3, 1000)
ff=f3(x)
plt.plot(x, ff, color = 'black')

def f4(x):
    return (np.sqrt(36 - (x + 1)**2))

x=np.linspace(4.367, 5, 1000)
ff=f4(x)
plt.plot(x, ff, color = 'black')


def f5(x):
    return (np.sqrt(100 - (x - 14)**2))

x=np.linspace(4, 4.367, 1000)
ff=f5(x)
plt.plot(x, ff, color = 'black')

#light path
for i in range(10, 260, 10):
    if i/100 < 2.0: 
        lp.shot(i/100, 0, minimum, maximum, index, h)
    else:
        lp.shot(i/100, 0, minimum, maximum, index2, h)
        

plt.show()




