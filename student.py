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

bf2 = bf.dropna(axis=0,how='any')
#sorting by marital status as married
n = bf.where(bf['Marital_Status']==1)
#dropping nans
n = n.dropna(axis=0,how='any')

mf_count = n['Gender'].value_counts()

female = mf_count.F
male = mf_count.M


#age 18-25 - Male

n1 = n.where(n['Age'] == '18-25') 
n1 = n1.dropna(axis=0,how='any')

n1 = n1.where(n1['Gender'] == 'M')
n1 = n1.dropna(axis=0, how='all')

des = n1.describe()


"""#plotting
sns.set(color_codes=True)

x = n1['Purchase']

sns.distplot(x)

mean = np.mean(x)
median = np.median(x)

#plotting the histogram of the purchase 
sns.distplot(x, bins = 15, kde=False, rug=True)"""

"""We can find that the distribution is slightly skewed to the left where
mean (11908.914) and median(11886.5) are close to each other""" 

df = n.copy() 
df = df.dropna(axis=0,how='any')

n2 = df.where(n['Age'] == '18-25') 
n2 = n2.dropna(axis=0,how='any')

n2 = n2.where(n2['Gender'] == 'F')
n2 = n2.dropna(axis=0, how='all')

des2 = n2.describe()

male_mean = np.mean(n1['Purchase'])
female_mean = np.mean(n2['Purchase'])

male_median = np.median(n1['Purchase'])
female_median = np.median(n2['Purchase'])

#Calculation of purchase under each City for married men aged 18-25
cityA_purchaseMmale = np.sum(n1['Purchase'].where(n1['City_Category'] == 'A'))
cityB_purchaseMmale = np.sum(n1['Purchase'].where(n1['City_Category'] == 'B'))
cityC_purchaseMmale = np.sum(n1['Purchase'].where(n1['City_Category'] == 'C'))

#Other stats
#ax = sns.countplot(x="City_Category", hue="Stay_In_Current_City_Years", data=n1)

#ax1 = sns.countplot(x="City_Category", hue="Product_Category_1", data=n1)

#ax2 = sns.countplot(x="Product_Category_1", hue="City_Category", data=n1)

#g = sns.catplot(x="Product_Category_1", hue="Stay_In_Current_City_Years", col="City_Category",data=n1,
             #   kind="count",height=4, aspect=.7)

#statistics for city category B, married men aged 18-25
occ = n1.where(n1['City_Category'] == 'B') 
occ = occ.dropna(axis=0,how='any')

#g1 = sns.catplot(x="Occupation", hue="Product_Category_1", col="Stay_In_Current_City_Years",data=occ,
#                kind="count",height=4, aspect=.7)

#ax3 = sns.countplot(x="Occupation", hue="Stay_In_Current_City_Years", data=occ)


#More General

#Count by gender
#g2 = sns.catplot(x="Occupation", hue="City_Category", col="Gender",data=bf2,
             #   kind="count",height=4, aspect=.7)

#Count by marital status
#g3 = sns.catplot(x="Occupation", hue="City_Category", col="Marital_Status",data=bf2,
              #kind="count",height=4, aspect=.7)

#occupaton count by city category
#ax4 = sns.countplot(x="Occupation", hue="City_Category", data=bf2)

#occupaton count by gender
#ax5 = sns.countplot(x="Occupation", hue="Gender", data=bf2)

#Count by marital status
#g5 = sns.boxplot(x="Occupation",y="Purchase",hue="Marital_Status",data=bf2)

#by order of occupation
sns.catplot(x="Occupation",order=[5,7,4,1,10], hue = 'Gender', col='City_Category',
            data=bf2,kind="count")

