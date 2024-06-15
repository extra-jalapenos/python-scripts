# -*- coding: utf-8 -*-
"""
Boolean Data Analytics Course

This script creates a DataFrame containing the current_price, the market_cap 
and the total_volume of transactions between bitcoin and each of the 61 
available tickers for the last 28 days.
"""

import pandas as pd
import requests
import seaborn as sns
import datetime
import time

# initalisation of parameters 
end_date = datetime.date.today()   # <-- today's date
days_back = 28   # <-- lookback window

# list of dates from the last 28 days
date_list = pd.date_range(end=end_date, periods=days_back) \
    .strftime("%d-%m-%Y").tolist()   # format dates as required by the API

# initialise an empty DataFrame named "df"
df = pd.DataFrame([])

# loop through the list of dates and, at each cycle: 
# - make an HTTP request to the CoinGecko API 
# - retrieve the information we need in JSON format
# - save the data to a temporary DataFrame named "tmp_df"
# - add the current cycle's date to a new column name "date" in the DataFrame
# - append the temporary DataFrame to the "df" DataFrame
for dt in date_list: 
    url = 'https://api.coingecko.com/api/v3/coins/bitcoin/history?date=' + dt
    r = requests.get(url)
    print(r.status_code)
    
    try:
        tmp_df = pd.DataFrame.from_dict(r.json()['market_data']).reset_index()
        tmp_df['date'] = dt
        df = pd.concat([df, tmp_df])
    except KeyError:
        print("Encountered an error, sleeping for 120 seconds")
        time.sleep(120)
        url = 'https://api.coingecko.com/api/v3/coins/bitcoin/history?date=' + dt
        r = requests.get(url)
        print(r.status_code)
        tmp_df = pd.DataFrame.from_dict(r.json()['market_data']).reset_index()
        tmp_df['date'] = dt
        df = pd.concat([df, tmp_df])

# re-index the DataFrame to avoid having duplicates in the index
df.reset_index(inplace=True)

# convert the date variable to DateTime
df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')

# finally we plot the time series for a specific exchange: BTC vs EUR
sns.set(rc={'figure.figsize':(13, 7)})
sns.lineplot(x='date', y='current_price', data=df[df['index']=='eur'])
