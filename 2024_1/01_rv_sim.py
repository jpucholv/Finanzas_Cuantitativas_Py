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
coeff = 5 # df in student, scale in exponential
random_variable_type = 'normal' # options: normal student uniform exponential chi-squared
size = 10**6
decimals = 5

sim = random_variables.simulator(coeff, random_variable_type, size, decimals)
sim.generate_vector()
sim.compute_stats()
sim.plot()