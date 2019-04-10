#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
import numpy as np
import csv


# In[35]:


filename = 'DataSources/business.csv'
df = pd.read_csv(filename, delimiter = ',')


# In[36]:


#df.dtypes


# In[62]:


mydf = df[[
'business_id', 
'categories', 
'name',
'review_count',
'stars',    
'address', 
'city',     
'state',
'postal_code',
'latitude',
'longitude']]
 


# In[63]:


mydf


# In[64]:


#make all strings caps and trim string
mydf['categories'] = mydf['categories'].str.strip().str.upper()
mydf['name'] = mydf['name'].str.strip().str.upper()
mydf['address'] = mydf['address'].str.strip().str.upper()
mydf['state'] = mydf['state'].str.strip().str.upper()
mydf['city'] = mydf['city'].str.strip().str.upper()


# In[50]:


#change to ny for big csv
#NONE FOR NJ/CT!! :O
ny = mydf[(mydf['state'] == 'NY')]
nj = mydf[(mydf['state'] == 'NJ')]
ct = mydf[(mydf['state'] == 'CT')]
#mydf = mydf[(mydf['city'] == 'PHOENIX')]
#NYC NEW YORK NEW YORK CITY N.Y.C
#BROOKLYN, NEW YORK 


# In[53]:


#full = ny.append(nj, ignore_index = True) 
#full = full.append(ct, ignore_index = True) 


# In[54]:


mydf = mydf[(mydf['state'] == 'NY')]
mydf


# In[67]:


#restaurants, bars, food, desserts, bakeries, breakfast, brunch, lunch, dinner, sandwiches
#a = 'RESTAURANTS, BARS, FOOD' #***
#b = 'BREAKFAST & BRUNCH'
#c = 'FOOD, DESSERTS, JUICE BARS & SMOOTHIES' 
#d = 'DESSERTS, FOOD, CUPCAKES, BAKERIES'

#other keywords to find restaurants :
#Sandwiches, Desserts, Custom Cakes, Bakeries...
#Fast Food, Food, Restaurants, Ice Cream 
#Bakeries, Food
#Sandwiches, Salad, Restaurants, Burgers, 
#Italian, Restaurants, Pizza, Chicken Wings
#CAFES???

restaurant_words = ['RESTAURANTS','BARS','FOOD','BREAKFAST & BRUNCH','DESSERTS','BAKERIES, DELIS, SANDWICHES', 'COFFEE & TEA', 'DINERS', 'CAFES']
pattern = '|'.join(restaurant_words)
mydf['restaurant'] = mydf.categories.str.contains(pattern)


# In[68]:


mydf


# In[79]:


mydf.isnull().sum()


# In[77]:


mydf = mydf.dropna(subset=['categories', 'restaurant'])


# In[78]:


mydf


# In[80]:


restaurants = mydf[mydf.restaurant]


# In[81]:


restaurants


# In[82]:


restaurants = restaurants.drop(['restaurant'], axis = 1)


# In[83]:


restaurants.to_csv('all_clean_restaurants.csv')


# In[ ]:




