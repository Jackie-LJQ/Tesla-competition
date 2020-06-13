# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 23:09:53 2020

@author: liu
"""
import pandas as pd
# extract feature of a-type site

def find_feature(t = 'a'):
    df = pd.read_csv('data/site.csv')
    dfa1 = df.where(df.site_type == t).dropna()
    dfa = dfa1[['var_name', 'var_value']]
    df1 = dfa.where(dfa.var_name == 'charging_experience_v1').dropna().reset_index()
    feature = pd.DataFrame({'charging_experience_v1':df1.var_value})
    for name in df.var_name.unique()[1:]:
        temp = dfa.where(dfa.var_name == name).dropna().reset_index()
        temp = temp.rename(columns = {'var_value':name})
        feature = pd.concat([feature, temp[name]], axis=1)
    feature.to_csv('data'+t+'_feature.csv', index = False)
# similiarly find feature of b and c site. 
#find_feature('a')
#find_feature('b')
#find_feature('c')

df1 = pd.read_csv('data/a_feature.csv')  
df2 = pd.read_csv('data/b_feature.csv')
df3 = pd.read_csv('data/c_feature.csv')

df_id = pd.DataFrame({'id':['a']*4296})
df1 = pd.concat([df_id, df1], axis = 1)

df_id = pd.DataFrame({'id':['b']*165})
df2 = pd.concat([df_id, df2], axis = 1)
    
df_id = pd.DataFrame({'id':['c']*165})
df3 = pd.concat([df_id, df3], axis = 1)

feature = pd.concat([df1, df2, df3])

feature.to_csv('data/site_feature.csv', index=False)
    