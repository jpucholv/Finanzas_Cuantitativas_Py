# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 21:54:51 2023

@author: OY
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy

degrees_freedom = 8
size = 10**6
random_variable_type = 'exponential' # normal student uniform exponential

if random_variable_type == 'normal':
    x = np.random.standard_t(df=degrees_freedom, size=size)
elif random_variable_type == 'student':
    x = np.random.standard_normal(size=size)
elif random_variable_type == 'uniform':
    x = np.random.uniform(size=size)
elif random_variable_type == 'exponential':
    x = np.random.exponential(size=size)

plt.figure()
plt.hist(x, bins=100)
plt.title(random_variable_type)
plt.show()