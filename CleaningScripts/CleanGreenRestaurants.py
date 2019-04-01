#!/usr/bin/env python
# coding: utf-8

# In[4]:


import csv
import pandas as pd
import numpy as np


# In[5]:


filename = 'DataSources/Current Certified Green Restaurants.csv'
df = pd.read_csv(filename, encoding = "ISO-8859-1", header = -1, na_filter = ' ')
df = df.rename(columns = {0: 'Name', 1: 'Address', 2: 'City', 3: 'State', 4: 'Zip', 5: 'PhoneNum', 6: 'website', 7: 'rating'})


# In[7]:


df.head()
#df.dropna()


# In[8]:


#ny = df['State'] = df['State'].astype(str)
#df.dtypes


# In[9]:


#df = df[~df['State'].contains('NY').contains('NJ').contains('CT')]
ny = df.loc[(df['State'] == 'NY')] 
nj = df.loc[(df['State'] == 'NJ')]
ct = df.loc[(df['State'] == 'CT')]


# In[10]:


full = ny.append(nj, ignore_index = True) 


# In[11]:


full.head()


# In[12]:


full = full.append(ct, ignore_index = True) 


# In[13]:


full.head()


# In[18]:


full = full.drop(columns = ['PhoneNum'])


# In[20]:


full['rating'] = full['rating'].str.extract('(\d+)')


# In[21]:


full.head()


# In[25]:


full.Name = full.Name.str.strip()
full.Address = full.Address.str.strip()
full.City = full.City.str.strip()
full.State = full.State.str.strip()
full.Zip = full.Zip.str.strip()
full.website = full.website.str.strip()
full.rating = full.rating.str.strip()


# In[26]:


full.to_csv('clean_green.csv')


# In[ ]:




