# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 18:26:02 2020

@author: liu
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# find how many superchargers in each city
#url = 'https://www.tesla.com/findus/list/superchargers/china'

#find how many destination chargers in the city
#url = 'https://www.tesla.com/findus/list/chargers/china'

#find how many stores in the city
url = 'https://www.tesla.com/findus/list/stores/china'

hdr = {'User-Agent': 'firefox'}
result = requests.get(url, headers = hdr)
page = BeautifulSoup(result.content, 'html.parser')
charger_locs = page.find_all('span', {'class': 'locality'})
dic = {}
for loc in charger_locs:
    dic[loc.text] = dic.get(loc.text,0)+1

cities = []
charger_num = []
for key in dic.keys():
    cities.append(key)
    charger_num.append(dic[key])
#    
#df = pd.DataFrame({'city_name':cities, 'charger_num':charger_num})
#df.to_csv('raw/supercharger_num.csv', index=False)
#df.to_csv('raw/Destination charger_num.csv', index=False)

df = pd.DataFrame({'city_name':cities, 'stores_num':charger_num})
df.to_csv('raw/stores_num.csv', index=False)
