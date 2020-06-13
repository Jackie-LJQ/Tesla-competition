# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 22:13:11 2020

@author: liu
"""

import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv('data/site.csv')
name = 'charging_experience_v1'
df1 = df.where(df.var_name == name).dropna()
df2 = df1.groupby(['site_type']).var_value.mean().reset_index()
features = pd.DataFrame({'site_type':df2.site_type, name:df2.var_value})
#extract mean feature from site.csv
for name in df.var_name.unique()[1:]:
    temp1 = df.where(df.var_name == name).dropna()
    temp2 = temp1.groupby(['site_type']).var_value.mean().reset_index()
    features[name] = pd.DataFrame({name:temp2.var_value})
features.to_csv('data/means.csv', index = False)

