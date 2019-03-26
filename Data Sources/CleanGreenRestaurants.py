#!/usr/bin/env python
# coding: utf-8

# In[40]:


import csv
import pandas as pd
import numpy as np


# In[41]:


filename = 'Current Certified Green Restaurants.csv'
df = pd.read_csv(filename, encoding = "ISO-8859-1", header = -1, na_filter = ' ')
df = df.rename(columns = {0: 'Name', 1: 'Address', 2: 'City', 3: 'State', 4: 'Zip', 5: 'PhoneNum', 6: 'website', 7: 'rating'})


# In[42]:


df
#df.dropna()


# In[43]:


#ny = df['State'] = df['State'].astype(str)
#df.dtypes


# In[48]:


#df = df[~df['State'].contains('NY').contains('NJ').contains('CT')]
ny = df.loc[(df['State'] == 'NY')] 
nj = df.loc[(df['State'] == 'NJ')]
ct = df.loc[(df['State'] == 'CT')]


# In[52]:


full = ny.append(nj, ignore_index = True) 


# In[53]:


full


# In[54]:


full = full.append(ct, ignore_index = True) 


# In[55]:


full


# In[58]:


full.to_csv('clean_green.csv')


# In[ ]:




