# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 16:46:58 2023

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

class capm:
    
    def __init__(self, benchmark, security, decimals=6):
        self.benchmark = benchmark
        self.security = security
        self.decimals = decimals
        self.timeseries = None
        self.x = None
        self.y = None
        self.alpha = None
        self.beta = None
        self.p_value = None
        self.null_hypothesis = None
        self.correlation = None
        self.r_squared = None
        self.predictor_linreg = None
        
    def syncronize_timeseries(self):
        self.timeseries = market_data.syncronize_timeseries(self.benchmark, self.security)
        
    def plot_timeseries(self):
        plt.figure(figsize=(12,5))
        plt.title('Time series of close prices')
        plt.xlabel('Time')
        plt.ylabel('Prices')
        ax = plt.gca()
        ax1 = self.timeseries.plot(kind='line', x='date', y='close_x', ax=ax, grid=True,\
                              color='blue', label=self.benchmark)
        ax2 = self.timeseries.plot(kind='line', x='date', y='close_y', ax=ax, grid=False,\
                              color='red', secondary_y=True, label=self.security)
        ax1.legend(loc=2)
        ax2.legend(loc=1)
        plt.show()
        
    def compute_linear_regression(self):
        self.x = self.timeseries['return_x'].values
        self.y = self.timeseries['return_y'].values
        slope, intercept, r_value, p_value, std_err = st.linregress(self.x, self.y)
        self.alpha = np.round(intercept, self.decimals)
        self.beta = np.round(slope, self.decimals)
        self.p_value = np.round(p_value, self.decimals)
        self.null_hypothesis = p_value > 0.05 # p_value < 0.05 --> reject null hypothesis
        self.correlation = np.round(r_value, self.decimals) # correlation coefficent
        self.r_squared = np.round(r_value**2, self.decimals) # pct of variance of y explained by x
        self.predictor_linreg = intercept + slope*self.x

    def plot_linear_regression(self):
        str_self = 'Linear regression | security ' + self.security\
            + ' |  benchmark ' + self.benchmark + '\n'\
                + 'alpha (intercept) ' + str(self.alpha)\
                + ' | beta (slope) ' + str(self.beta) + '\n'\
                + 'p_value ' + str(self.p_value)\
                + ' |  null hypothesis ' + str(self.null_hypothesis) + '\n'\
                + 'correl (r_value) ' + str(self.correlation)\
                + ' | r_squared ' + str(self.r_squared)
        str_title = 'Scatterplot of returns' + '\n' + str_self
        plt.figure()
        plt.title(str_title)
        plt.scatter(self.x, self.y)
        plt.plot(self.x, self.predictor_linreg, color='green')
        plt.ylabel(self.security)
        plt.xlabel(self.benchmark)
        plt.grid()
        plt.show()