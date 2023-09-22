# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 21:54:51 2023

@author: OY
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st

# inputs
coeff = 5 # df in student, scale in exponential
size = 10**6
random_variable_type = 'student' # options: normal student uniform exponential chi-squared
decimals = 5

# code
str_title = random_variable_type
if random_variable_type == 'normal':
    x = np.random.standard_normal(size=size)

elif random_variable_type == 'student':
    x = np.random.standard_t(df=coeff, size=size)
    str_title += ' df=' + str(coeff)

elif random_variable_type == 'uniform':
    x = np.random.uniform(size=size)

elif random_variable_type == 'exponential':
    x = np.random.exponential(scale=coeff, size=size)
    str_title += ' scale=' + str(coeff)
    
elif random_variable_type == 'chi-squared':
    x = np.random.chisquare(df=coeff, size=size)
    str_title += ' df=' + str(coeff)
    
mu = st.tmean(x) # np.mean st.tmean
sigma = st.tstd(x) # np.std st.tstd
skewness = st.skew(x)
kurtosis = st.kurtosis(x)

# Test of Normality: Jarque-Bera
jb_stat = size/6 * (skewness**2 + 1/4 * kurtosis**2)
p_value = 1 - st.chi2.cdf(jb_stat, df=2)
is_normal = (p_value > 0.05) # equivalently jb < 6

str_title += '\n' + 'mean=' + str(np.round(mu, decimals)) \
    + ' | ' + 'volatility=' + str(np.round(sigma, decimals)) \
    + '\n' + 'skewness=' + str(np.round(skewness, decimals)) \
    + ' | ' + 'kurtosis=' + str(np.round(kurtosis, decimals)) \
    + '\n' + 'JB stat=' + str(np.round(jb_stat, decimals)) \
    + ' | ' + 'p-value' + str(np.round(p_value, decimals)) \
    + ' | ' + 'is_normal=' + str(is_normal)
    
# plot
plt.figure()
plt.hist(x, bins=100)
plt.title(str_title)
plt.show()


####################################
# Loop of Jarque-Bera normality test
####################################

n = 0
is_normal = True
str_title = 'normal'

while is_normal and n < 100:
    x = np.random.standard_normal(size=size)
    
    mu = st.tmean(x) # np.mean st.tmean
    sigma = st.tstd(x) # np.std st.tstd
    skewness = st.skew(x)
    kurtosis = st.kurtosis(x)

    # Test of Normality: Jarque-Bera
    jb_stat = size/6 * (skewness**2 + 1/4 * kurtosis**2)
    p_value = 1 - st.chi2.cdf(jb_stat, df=2)
    is_normal = (p_value > 0.05) # equivalently jb < 6
    
    print(f'n={n} | is_normal={is_normal}')
    n += 1

str_title += '\n' + 'mean=' + str(np.round(mu, decimals)) \
    + ' | ' + 'volatility=' + str(np.round(sigma, decimals)) \
    + '\n' + 'skewness=' + str(np.round(skewness, decimals)) \
    + ' | ' + 'kurtosis=' + str(np.round(kurtosis, decimals)) \
    + '\n' + 'JB stat=' + str(np.round(jb_stat, decimals)) \
    + ' | ' + 'p-value' + str(np.round(p_value, decimals)) \
    + ' | ' + 'is_normal=' + str(is_normal)
    
# plot
plt.figure()
plt.hist(x, bins=100)
plt.title(str_title)
plt.show()