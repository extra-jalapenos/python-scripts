#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Boolean Data Analytics Course

Homework 2 Solution - Advanced Exercise
"""

import pandas as pd
import seaborn as sns
import os


# set the directory to the folder containing this script
os.chdir('/Users/franz/Documents/Boolean/Data Analytics/git/3.13.32 APIs, Scripts and OS')

# create a list object containing all the .csv files we need
files = os.listdir('data/homework/1_unprocessed')

# --> IF DIRECTORY DOES NOT EXIST, THEN:
# create a new folder named '2_processed' under 'homework'
if os.path.exists('data/homework/2_processed')==False: 
    os.mkdir('data/homework/2_processed')

# --> IF DIRECTORY IS EMPTY, THEN:
if len(os.listdir('data/homework/2_processed'))==0: 
    # cycle through all the elements in the directory and, at each cycle, load 
    # them to a temporary DataFrame 'tmp_df' and append them to an empty 
    # DataFrame 'df'; after that, move the used .csv file to the '2_processed' directory

    df = pd.DataFrame([])
    for file in files: 
        tmp_df = pd.read_csv('data/homework/1_unprocessed/' + file)
        df = df.append(tmp_df)
        os.rename('data/homework/1_unprocessed/'+file, 'data/homework/2_processed/'+file)

    # re-index the DataFrame to avoid having duplicates in the index
    df.index = pd.RangeIndex(len(df.index))
    
    # convert the date variable to DateTime
    df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')
    
    # finally we plot the time series for a specific exchange: BTC vs EUR
    sns.set(rc={'figure.figsize':(13, 7)})
    plot = sns.lineplot(x='date', y='current_price', data=df[df['index']=='eur'])
    plot.get_figure().autofmt_xdate() 
    plot.set(title='Bitcoin Price Chart (BTC/EUR)', 
             xlabel='', 
             ylabel='Price in Euro')
    # ...and save it locally to a .png file
    plot.get_figure().savefig("data/homework/btceur_line_plot.png") 
