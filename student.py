# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 18:17:15 2018

@author: prash
"""

import pandas as pd
import numpy as np 
from pandas import ExcelWriter
import csv
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

#path = is the path of the csv file or the dataset
path = 'C:\\Users\prash\\Downloads\\GitHub\\blackfriday-analysis\\BlackFriday.csv'
bf = pd.read_csv(path)

#sorting by marital status as married
n = bf.where(bf['Marital_Status']==1)
#dropping nans
n = n.dropna(axis=0,how='any')

mf_count = n['Gender'].value_counts()

female = mf_count.F
male = mf_count.M


#age 18-25

n1 = n.where(n['Age'] == '18-25') 
n1 = n1.dropna(axis=0,how='any')

n1 = n1.where(n1['Gender'] == 'M')
n1 = n1.dropna(axis=0, how='all')

des = n1.describe()

#saving the file to a csv
"""n1.to_csv("C:\\Users\\prash\\Downloads\\bf1825.csv",index=False,header = True, sep=",")"""


#plotting
sns.set(color_codes=True)

x = n1['Purchase']

#sns.distplot(x)

mean = np.mean(x)
median = np.median(x)

#plotting the histogram of the purchase 
sns.distplot(x, bins = 10, kde=False, rug=True)

"""We can find that the distribution is a left skewed distribution where 
mean (11908.914) and median(11886.5) are close to each other"""


