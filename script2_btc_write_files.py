#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Boolean Data Analytics Course

This script retrieves data from the CoinGecko API for the last 28 days and, 
for each day retrieved, saves the results to a csv file in the 'btc' folder.
"""

import pandas as pd
import requests
import datetime
import os

# set the directory to our class
os.chdir('/Users/franz/Documents/Boolean/Data Analytics/git/3.13.32 APIs, Scripts and OS')

# initalisation of parameters
end_date = datetime.date.today()   # <-- today's date
days_back = 28   # <-- lookback window

# list of dates from the last 28 days
date_list = pd.date_range(end=end_date, periods=days_back) \
    .strftime("%d-%m-%Y").tolist()   # format dates as required by the API

# create a directory where to store all the files that we're going to generate
os.mkdir('data/btc')

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
    tmp_df.to_csv('data/btc/btc_'+str(dt)+'.csv')

os.listdir('data/btc')
