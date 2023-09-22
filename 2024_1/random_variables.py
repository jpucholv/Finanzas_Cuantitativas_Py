# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 23:15:06 2023

@author: OY
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st

class simulator():
    
    # constructor
    def __init__(self, coeff, rv_type, size=10**6, decimals=5):
        self.coeff = coeff
        self.rv_type = rv_type
        self.size = size
        self.decimals = decimals
        self.str_title = None
        self.vector = None
        
    def generate_vector(self):
        self.str_title = self.rv_type
        
        if self.rv_type == 'normal':
            self.vector = np.random.standard_normal(size=self.size)

        elif self.rv_type == 'student':
            self.vector = np.random.standard_t(df=self.coeff, size=self.size)
            self.str_title += ' df=' + str(self.coeff)

        elif self.rv_type == 'uniform':
            self.vector = np.random.uniform(size=self.size)

        elif self.rv_type == 'exponential':
            self.vector = np.random.exponential(scale=self.coeff, size=self.size)
            self.str_title += ' scale=' + str(self.coeff)
            
        elif self.rv_type == 'chi-squared':
            self.vector = np.random.chisquare(df=self.coeff, size=self.size)
            self.str_title += ' df=' + str(self.coeff)