#filters out business.csv for restaurant keywords

import pandas as pd
import numpy as np
import csv


filename = 'DataSources/business.csv'
df = pd.read_csv(filename, delimiter = ',')

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
 
mydf

#make all strings caps and trim string
mydf['categories'] = mydf['categories'].str.strip().str.upper()
mydf['name'] = mydf['name'].str.strip().str.upper()
mydf['address'] = mydf['address'].str.strip().str.upper()
mydf['state'] = mydf['state'].str.strip().str.upper()
mydf['city'] = mydf['city'].str.strip().str.upper()


#change to ny for big csv
#NONE FOR NJ/CT!! :O
ny = mydf[(mydf['state'] == 'NY')]
nj = mydf[(mydf['state'] == 'NJ')]
ct = mydf[(mydf['state'] == 'CT')]
#mydf = mydf[(mydf['city'] == 'PHOENIX')]
#NYC NEW YORK NEW YORK CITY N.Y.C
#BROOKLYN, NEW YORK 
#full = ny.append(nj, ignore_index = True) 
#full = full.append(ct, ignore_index = True) 
ny.head()


#mydf = mydf[(mydf['state'] == 'NY')]
mydf


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

restaurant_words = restaurant_words = ['RESTAURANTS','BARS','FOOD',
                                       'BREAKFAST & BRUNCH','DESSERTS',
                                       'BAKERIES, DELIS, SANDWICHES', 
                                       'COFFEE & TEA', 'DINERS', 'CAFES']
pattern = '|'.join(restaurant_words)
mydf['restaurant'] = mydf.categories.str.contains(pattern)


mydf.info()
mydf
mydf.isnull().sum()
mydf = mydf.dropna(subset=['categories', 'restaurant'])
mydf


restaurants = mydf[mydf.restaurant]
restaurants
restaurants = restaurants.drop(['restaurant'], axis = 1)
restaurants.to_csv('all_clean_restaurants.csv')




