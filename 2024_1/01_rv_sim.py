# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 21:54:51 2023

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
inputs = random_variables.simulation_inputs()
inputs.df = 23 # degrees of freedom or df in student an chi_squared
inputs.scale = 17 # scale in exponential
inputs.mean = 5 # mean in normal
inputs.std = 10 # standard deviation or std in normal
inputs.rv_type = 'chi_squared' # options: standard_normal normal student uniform exponential chi_squared
inputs.size = 10**6
inputs.decimals = 5

# computations
sim = random_variables.simulator(inputs)
sim.generate_vector()
sim.compute_stats()
sim.plot()