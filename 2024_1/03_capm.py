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
import market_data
importlib.reload(market_data)

# inputs
benchmark = 'XLV' # x
security = 'PG' # y

# initialize class capm
capm = market_data.capm(benchmark, security)
capm.syncronize_timeseries()
capm.plot_timeseries()
capm.compute_linear_regression()
capm.plot_linear_regression()