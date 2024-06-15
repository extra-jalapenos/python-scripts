#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Boolean Data Analytics Course

This script loops through each of the files in the 'btc' folder and appends
them to an initially empty DataFrame. 
"""

import pandas as pd
import seaborn as sns
import os


# set the directory to the folder containing this script
os.chdir('/Users/franz/Documents/Boolean/Data Analytics/git/3.13.32 APIs, Scripts and OS')

# list all the contents of the 'btc' folder
os.listdir('data/btc')

# create a list object containing all the csv files we need
files = os.listdir('data/btc')

# cycle through all the elements in the directory and, at each cycle, load 
# them to a temporary DataFrame 'tmp_df' and append them to an empty 
# DataFrame 'df' 
df = pd.DataFrame([])
for file in files: 
    if file != '.ipynb_checkpoints':        
        tmp_df = pd.read_csv('data/btc/' + file)
        df = df.append(tmp_df)

# re-index the DataFrame to avoid having duplicates in the index
df.index = pd.RangeIndex(len(df.index))

# convert the date variable to DateTime
df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')

# finally we plot the time series for a specific exchange: BTC vs EUR
sns.set(rc={'figure.figsize':(13, 7)})
plot = sns.lineplot(x='date', y='current_price', data=df[df['index']=='eur'])
plot.set(title='Bitcoin Price Chart (BTC/EUR)', 
         xlabel='', 
         ylabel='Price in Euro')
# ...and save it locally to a .png file
plot.get_figure().savefig("btceur_line_plot.png") 


# remove all csv files from the 'btc' directory
for file in os.listdir('data/btc'): 
    os.remove('data/btc/' + file)

# remove the (now empty) directory
os.rmdir('data/btc')
