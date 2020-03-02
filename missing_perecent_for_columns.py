# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 11:41:04 2020

@author: mpenm
"""

import numpy as np
import pandas as pd

coff_data = pd.read_csv('clt_coff_shops.csv')

coff_data1 = coff_data

coff_data1.describe()


for column in coff_data1.columns:
    #print(column)
    print(coff_data1[column].value_counts(dropna=False))
    
    
percent_missing = coff_data1.isnull().sum() * 100 / len(coff_data1)
missing_value_df = pd.DataFrame({'column_name': coff_data1.columns,'percent_missing': percent_missing})


missing_value_df.to_excel('missingdata.xlsx')
