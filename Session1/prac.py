# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 21:56:46 2019

@author: Shri Hari
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

dataset = pd.read_csv('Data.csv')
X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,3].values