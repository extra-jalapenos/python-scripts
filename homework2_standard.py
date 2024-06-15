#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Boolean Data Analytics Course

Homework 2 Solution - Standard Exercise
"""

import pandas as pd
import seaborn as sns
import os

# initialise an empty DataFrame
df = pd.DataFrame([])

# save list of all files in the mkp directory
files = os.listdir('data/mkp')

# loop through all the files contained in the 'mkp' folder and 
# execute the algorithm
for file in files:
    mkp_tmp = pd.read_csv('data/mkp/'+file)
    df = df.append(mkp_tmp)

# re-index the DataFrame to avoid having duplicates in the index
df.index = pd.RangeIndex(len(df.index))

# create a bar-plot showing the number of products available for each brand
sns.set(rc={'figure.figsize':(13, 9)})
plot = sns.countplot(y='brand', data=df, color='c', order=df['brand'].value_counts().index)
plot.set(title='Number of products available per brand', 
         xlabel='Number of products', 
         ylabel='')
# ...and save it locally to a .png file
plot.get_figure().savefig("products_per_brand.png") 


# remove all csv files from the 'mkp' directory
for file in os.listdir('data/mkp'): 
    os.remove('data/mkp/' + file)

# remove the (now empty) directory
os.rmdir('data/mkp')
