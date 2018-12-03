# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 18:17:15 2018

@author: prash
"""

import pandas as pd
import numpy as np 
from pandas import ExcelWriter
import csv
bf = pd.read_csv('C:\\Users\prash\\Downloads\\GitHub\\blackfriday-analysis\\BlackFriday.csv')

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

"""n1.to_csv("C:\\Users\\prash\\Downloads\\bf1825.csv",index=False,header = True, sep=",")"""
