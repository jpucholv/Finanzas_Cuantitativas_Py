# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 21:55:22 2023

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
position_security = 'GOOG'
position_delta_usd = 10 # mn USD
benchmark = '^SPX'
hedge_securities = ['AAPL', 'MSFT']

hedger = capm.hedger(position_security, position_delta_usd, benchmark, hedge_securities)
hedger.compute_betas()
hedger.compute_hedge_weights()