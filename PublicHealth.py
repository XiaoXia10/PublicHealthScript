#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 22:14:07 2020

@author: maryliang
"""

# the oxford stringency categories have been updated but not the canadian data
# best thing to do is to reconstruct the canadian data instead of shovelling 
# it around to match the oxford data

import pandas as pd
import numpy as np
#import re 

# your path here
dat = pd.read_csv(r'YOUR PATH HERE', index_col = 0)
dat = dat.sort_values(by=['region', 'start_date'])

uniq_can_cate = dat['intervention_category'].unique()

#-------------------------------------------
#new category that was added by oxford. This is the only one that I can map
temp = dat['intervention_category']
gathering = temp.str.contains('Public event size restriction', na=False)

# the index of all bool true
#list_true = [i for i in gathering.index if gathering[i]]
list_true = gathering[gathering].index

for ind in list_true:
    dat['oxford_government_response_category'][ind] = 'C4_Restrictions on gatherings'

#-----------------------------------------
   
#New Oxford categories 
new_ox_cate = ['C1_School closing', 'C1_Flag', 'C2_Workplace closing', 'C2_Flag', 'C3_Cancel public events', \
           'C3_Flag', 'C4_Restrictions on gathering','C4_Flag', 'C5_Closed public transport', \
           'C5_Flag', 'C6_Stay at home requirements', 'C6_Flag', 'C7_Restrictions on internal movement', \
           'C7_Flag', 'C8_International travel controls', 'E1_Income Support', 'E1_Flag', \
           'E2_Debt/contract relief', 'E3_Fiscal measures', 'E4_International support', \
           'H1_Public information campaigns', 'H1_Flag', 'H2_Testing policy', 'H3_Contact tracing', \
           'H4_Emergency investment in healthcare', 'H5_Investment in vaccines', 'M1_Wildcard', 'ConfirmedCases', \
           'ConfirmedDeaths', 'StringencyIndex', 'StringencyIndexForDisplay', 'LegacyStringencyIndex', \
           'LegacyStringencyIndexForDisplay'] 

# Old Oxford categories that Canadian public health used 
old_ox_cate = ['S1 School Closing', 'S1_flag', 'S2 Workplace closing', 'S2_flag', 'S3 Cancel public events', 'S3_flag', 'C4_Restrictions on gathering', 'C4_flag', 'S4 Close public transport', 'S4_flag', \
               'C6_Stay at home requirements', 'C6_flag', 'S6 Restrictions on internal movements', 'S6_flag', 'S7 International travel controls', 'E1_Income support', 'E1_flag', 'E2_Debt/contract relief', 'S8 Fiscal Measures', \
               'E4_International support', 'S5 Public info campaigns', 'S5_flag', 'S12 Testing policy', 'S13 Contact tracing', 'S10 Emergency investment in health care', 'S11 Investment in vaccines', 'M1_WildCard', 'ConfirmedCases', \
               'ConfirmedDeaths', 'StringencyIndex', 'StringencyIndexForDisplay', 'LegacyStringencyIndex', \
               'LegacyStringencyIndexForDisplay']

# Replace old Oxford categories with new Oxford categories
n = 0
for old in old_ox_cate:
 
    change_cate = dat['oxford_government_response_category'].str.contains(old, na=False)
    li = change_cate[change_cate].index 
    
    for ind in li:
        dat['oxford_government_response_category'][ind] = new_ox_cate[n]
    
    n += 1
    
can_data = pd.concat([dat['start_date'], dat['country'], dat['region'], dat['subregion'], dat['oxford_government_response_category']], axis = 1)

# need data propagation - I dont not understand the Canadian data and need someone to clarify before continuing
for col in new_ox_cate:
    can_data[col] = np.nan

# your path here 
export_data= can_data.to_csv(r'YOUR PATH HERE')



    
