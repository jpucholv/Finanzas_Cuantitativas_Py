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

benchmark = '^SPX' # x
security = '^VIX' # 

# get timeseries of x an y
timeseries_x = market_data.load_timeseries(benchmark)
timeseries_y = market_data.load_timeseries(security)
timestamp_x = list(timeseries_x['date'].values)
timestamp_y = list(timeseries_y['date'].values)
timestamps = list(set(timestamp_x) & set(timestamp_y))
timeseries_x = timeseries_x[timeseries_x['date'].isin(timestamps)]
timeseries_x = timeseries_x.sort_values(by='date', ascending=True)
timeseries_x = timeseries_x.reset_index(drop=True)
timeseries_y = timeseries_y[timeseries_y['date'].isin(timestamps)]
timeseries_y = timeseries_y.sort_values(by='date', ascending=True)
timeseries_y = timeseries_y.reset_index(drop=True)

timeseries = pd.DataFrame()
timeseries['date'] = timeseries_x['date']
timeseries['close_x'] = timeseries_x['close']
timeseries['close_y'] = timeseries_y['close']
timeseries['return_x'] = timeseries_x['return']
timeseries['return_y'] = timeseries_y['return']

# plot timeseries
plt.figure(figsize=(12,5))
plt.title('Time series of close prices')
plt.xlabel('Time')
plt.ylabel('Prices')
ax = plt.gca()
ax1 = timeseries.plot(kind='line', x='date', y='close_x', ax=ax, grid=True,\
                      color='blue', label=benchmark)
ax2 = timeseries.plot(kind='line', x='date', y='close_y', ax=ax, grid=False,\
                      color='red', secondary_y=True, label=security)
ax1.legend(loc=2)
ax2.legend(loc=1)
plt.show()