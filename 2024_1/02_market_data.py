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

# import our own files an reload
import random_variables
importlib.reload(random_variables)

# inputs
ric = 'XLK'

directory = r'C:\Users\OY\Documents\Python\Finanzas Cuantitativas Py\Finanzas_Cuantitativas_Py\2024_1_data'
path = directory + '\\' + ric + '.csv'
raw_data = pd.read_csv(path)

t = pd.DataFrame()
t['date'] = pd.to_datetime(raw_data['Date'])
t['close'] = raw_data['Close']
t.sort_values(by='date', ascending=True)
t['return_close'] = t['close']/t['close'].shift(1) - 1
t = t.dropna()
t = t.reset_index(drop=True)

# inputs
inputs = random_variables.simulation_inputs()
inputs.rv_type = ric + ' | real time'
inputs.size = 10**6
inputs.decimals = 5

# computations
sim = random_variables.simulator(inputs)
sim.vector = t['return_close'].values
sim.inputs.size = len(sim.vector)
sim.str_title = sim.inputs.rv_type
sim.compute_stats()
sim.plot()
