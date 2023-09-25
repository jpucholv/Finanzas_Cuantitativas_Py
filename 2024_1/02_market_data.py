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

# inputs
ric = 'EWW'

directory = r'C:\Users\OY\Documents\Python\Finanzas Cuantitativas Py\Finanzas_Cuantitativas_Py\2024_1_data'
path = os.path.join(directory, f'{ric}.csv')
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

plt.figure()
t.plot(kind='line', x='date', y='close', grid=True, color='blue', label=ric,\
       title=f'Timeseries of close price for {ric}')
plt.show()

rics = []
is_normals = []
for file_name in os.listdir(directory):
    print(f'file_name = {file_name}')
    ric = file_name.split('.')[0]
    if ric == 'ReadMe':
        continue
    
    # get dataframe
    path = os.path.join(directory, f'{ric}.csv')
    raw_data = pd.read_csv(path)
    t = pd.DataFrame()
    t['date'] = pd.to_datetime(raw_data['Date'])
    t['close'] = raw_data['Close']
    t.sort_values(by='date', ascending=True)
    t['return_close'] = t['close']/t['close'].shift(1) - 1
    t = t.dropna()
    t = t.reset_index(drop=True)
    
    # computations
    sim = random_variables.simulator(inputs)
    sim.vector = t['return_close'].values
    sim.inputs.size = len(sim.vector)
    sim.str_title = sim.inputs.rv_type
    sim.compute_stats()
    
    # generate lists
    rics.append(ric)
    is_normals.append(sim.is_normal)
    
df = pd.DataFrame()
df['ric'] = rics
df['is_normal'] = is_normals