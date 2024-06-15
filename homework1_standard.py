#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Boolean Data Analytics Course

Homework 1 Solution - Standard Exercise
"""

import numpy as np
import pandas as pd
import requests
import os


# this is the API endpoint
url = 'https://makeup-api.herokuapp.com/api/v1/products.json'

# the list of brands available via the API
mkp_brands = ['colourpop', 'boosh', 'deciem', 'zorah biocosmetiques',
              'w3llpeople', "sally b's skin yummies", 'rejuva minerals',
              'penny lane organics', 'nudus', 'marienatie',
              "maia's mineral galaxy", 'lotus cosmetics usa', 'green people',
              'coastal classic creation', "c'est moi", 'alva', 'glossier', 
              'nyx', 'fenty', 'clinique', 'dior', 'iman', 'benefit', 
              'smashbox', 'marcelle', 'stila', 'mineral fusion', 'annabelle',
              'dr. hauschka', 'physicians formula', 'cargo cosmetics',
              'covergirl', 'e.l.f.', 'maybelline', 'almay', 'milani',
              'pure anada', "l'oreal", 'sante', 'revlon', 'anna sui',
              'wet n wild', 'pacifica', 'mistura', 'zorah', 'suncoat', 'moov',
              'misa', 'salon perfect', 'orly', 'china glaze', 'essie',
              'butter london', 'sinful colours', 'piggy paint', 'dalish', 
              "burt's bees"]

# randomply select 10 elements from the list
# note: the random component is a bonus, you could have chosen the 
#       items manually
mkp_brands = np.random.choice(mkp_brands, size=10, replace=False)

# create an empty folder named 'mkp' under the 'data' directory
os.mkdir('data/mkp')

# loop through all 10 selected brands and execute algorithm
for brand in mkp_brands: 
    mkp = requests.get(url+'?brand='+brand)
    print('...loading '+str(brand)+' brand | status code = '+str(mkp.status_code))
    mkp_tmp = pd.DataFrame.from_dict(mkp.json())
    mkp_tmp.to_csv('data/mkp/'+brand+'.csv')

os.listdir('data/mkp')

