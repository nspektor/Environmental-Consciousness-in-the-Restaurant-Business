# to combine review.csv with all_clean_restaurants.csv
# produces all text for each unique business_id

import csv
import pandas as pd
import numpy as np

rdf = pd.read_csv('DataSources/mini_review.csv', header=0)
bdf = pd.read_csv('DataSources/all_clean_restaurants.csv', header=0)
greendf = pd.read_csv('DataSources/business_green.csv', header=0)
mybdf = bdf.drop_duplicates(subset=['business_id'])
mybdf['categories'] = mybdf['categories'].str.replace(',', ' ')


myrdf = rdf[['business_id', 'text']]
myrdf['text'] = myrdf['text'].str.replace(',', ' ')
# run nltk preprocessing on text




test = myrdf.groupby('business_id')['text'].apply(list).to_frame().reset_index()

mergedf = mybdf.merge(test, left_on='business_id', right_on='business_id', how='inner', suffixes=['_biz', '_test'])
#merge with green data

grouped = mergedf.groupby('name')['text'].apply(list).to_frame().reset_index()

print(grouped)
grouped.to_csv('mini_yelp_data/grouped_by_name.csv')

test['green'] = np.random.randint(0, 2, test.shape[0])

mergedf.to_csv('mini_yelp_data/mini_merged_yelp.csv')
test.to_csv('mini_yelp_data/mini_merged_reviews.csv')
