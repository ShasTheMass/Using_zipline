# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 05:50:09 2016

@author: chaz
"""

import talib 
import numpy as np
import matplotlib.pyplot as plt

close = np.random.random(100)
output1 = talib.SMA(close,timeperiod=10)
output2 = talib.BBANDS(close)
#fig = plt.figure()
#close = close.astype(int)
#close.plot()
#plt.show()
plt.plot(close)
plt.plot(output1)
plt.plot(output2)

plt.ylabel('some numbers')
plt.show()