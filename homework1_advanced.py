#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Boolean Data Analytics Course

Homework 1 Solution - Advanced Exercise
"""

import pandas as pd
import requests
import os

# set the directory to our class
os.chdir('/Users/franz/Documents/Boolean/Data Analytics/git/3.13.32 APIs, Scripts and OS')

# define parameters start_date and end_date
start_date = '2022-05-01'
end_date = '2022-05-31'

# list of dates between start and end dates
date_list = pd.date_range(start=start_date, end=end_date) \
    .strftime("%d-%m-%Y").tolist()   # format dates as required by the API

# --> IF DIRECTORY DOES NOT EXIST, THEN:
# create a directory where to store all the files that we're going to generate
if os.path.exists('data/homework/1_unprocessed')==False: 
    os.mkdir('data/homework/1_unprocessed')

# --> IF DIRECTORY IS EMPTY, THEN:
if len(os.listdir('data/homework/1_unprocessed'))==0: 
    # loop through the list of dates and, at each cycle: 
    # - make an HTTP request to the CoinGecko API 
    # - retrieve the information we need in JSON format
    # - save the data to a temporary DataFrame named "tmp_df"
    # - add the current cycle's date to a new column name "date" in the DataFrame
    # - save the temporary DataFrame to a .csv file in your local folder
    for dt in date_list: 
        url = 'https://api.coingecko.com/api/v3/coins/bitcoin/history?date=' + dt
        r = requests.get(url)
        print('...loading '+str(dt)+' data | status code: '+str(r.status_code))
        tmp_df = pd.DataFrame.from_dict(r.json()['market_data']).reset_index()
        tmp_df['date'] = dt
        tmp_df.to_csv('data/homework/1_unprocessed/btc_'+str(dt)+'.csv')
    
    os.listdir('data/homework/1_unprocessed')
