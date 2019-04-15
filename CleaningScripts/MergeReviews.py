#to combine review.csv with all_clean_restaurants.csv
#produces all text for each unique business_id

import csv
import pandas as pd
import numpy as np

bdf = pd.read_csv('DataSources/all_clean_restaurants.csv', header = 0)
mybdf = bdf.drop_duplicates(subset = ['business_id'])
mybdf['categories'] = mybdf['categories'].str.replace(',', ' ')

rdf = pd.read_csv('DataSources/review.csv', header = 0)
myrdf = rdf[['business_id','text']]
myrdf['text'] = myrdf['text'].str.replace(',', ' ')

test = myrdf.groupby('business_id')['text'].apply(list).to_frame().reset_index()

mergedf = mybdf.merge(test, left_on='business_id', right_on='business_id', how='inner', suffixes=['_biz', '_test'])
mergedf

mergedf.to_csv('test_full_yelp.csv')

