# This was done on local machine using pandas


import csv
import pandas as pd
import numpy as np

rdf = pd.read_csv('DataSources/mini_review.csv', header = 0)
bdf = pd.read_csv('DataSources/all_clean_restaurants.csv', header = 0)

myrdf = rdf[['business_id','text']]
mybdf = bdf.drop_duplicates(['business_id'], axis=1)
test = myrdf.groupby('business_id')['text'].apply(list).to_frame().reset_index()

mergedf = mybdf.merge(test, left_on='business_id', right_on='business_id', how='inner', suffixes=['_biz', '_rev'])
mergedf['categories'] = mergedf['categories'].str.replace(',', ' ')
mergedf['text'] = mergedf['text'].str.replace(',', ' ')

mergedf.to_csv('full_yelp.csv')

