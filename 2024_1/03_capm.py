# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 10:36:40 2023

@author: OY
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
import importlib

# import our own files an reload
import capm
importlib.reload(capm)

# inputs
benchmark = '^SPX' # x
security = 'GOOG' # y

# initialize class capm
model = capm.model(benchmark, security)
model.syncronize_timeseries()
model.plot_timeseries()
model.compute_linear_regression()
model.plot_linear_regression()