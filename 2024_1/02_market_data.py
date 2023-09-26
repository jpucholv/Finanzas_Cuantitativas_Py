# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 11:11:37 2023

@author: OY
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
import importlib
import os

# import our own files an reload
import random_variables
importlib.reload(random_variables)
import market_data
importlib.reload(market_data)

# inputs
directory = r'C:\Users\OY\Documents\Python\Finanzas Cuantitativas Py\Finanzas_Cuantitativas_Py\2024_1_data' # hardcoded
ric = 'SPY'

# computations
dist = market_data.distribution(ric)
dist.load_timeseries()
dist.plot_timeseries()
dist.compute_stats()
dist.plot_histogram()


# loop to check normality in real distributions
rics = []
is_normals = []
for file_name in os.listdir(directory):
    print(f'file_name = {file_name}')
    ric = file_name.split('.')[0]
    if ric == 'ReadMe':
        continue
    
    # compute stats
    dist = market_data.distribution(ric)
    dist.load_timeseries()
    dist.compute_stats()
    
    # generate lists
    rics.append(ric)
    is_normals.append(dist.is_normal)
    
df = pd.DataFrame()
df['ric'] = rics
df['is_normal'] = is_normals
df = df.sort_values(by='is_normal', ascending=False)