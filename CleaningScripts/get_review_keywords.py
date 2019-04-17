# to combine review.csv with all_clean_restaurants.csv
# produces all text for each unique business_id

import pandas as pd

# rdf = pd.read_csv('DataSources/mini_review.csv', header=0)
rdf = pd.read_csv('big_yelp_data/review.csv', header=0)
bdf = pd.read_csv('DataSources/all_clean_restaurants.csv', header=0)
greendf = pd.read_csv('DataSources/business_green.csv', header=0)
bdf = bdf.drop_duplicates(subset=['business_id'])
bdf['categories'] = bdf['categories'].str.replace(',', ' ')

rdf = rdf[['business_id', 'text']]
rdf['text'] = rdf['text'].str.replace(',', ' ')

print("bdf:\n" , bdf.info())
result_df = rdf.groupby('business_id')['text'].apply(list).to_frame().reset_index()
print("result_df:\n" , result_df.get(0))
businesses_and_reviews = bdf.merge(result_df, left_on='business_id', right_on='business_id', how='inner', suffixes=['_biz', '_test'])
businesses_and_reviews = businesses_and_reviews.groupby('name')['text'].apply(list).to_frame().reset_index()

print("businesses_and_reviews:\n" , businesses_and_reviews.head(10))
bdf.to_csv('mini_yelp_data/bdf.csv')

businesses_and_reviews.to_csv('mini_yelp_data/businesses_and_reviews.csv')
result_df.to_csv('mini_yelp_data/result_df.csv')

green = pd.read_csv('DataSources/clean_green.csv', header=0, delimiter=',')

businesses_and_reviews = businesses_and_reviews.sort_values(['name'])
green = green.sort_values(['Name'])

testmerge = businesses_and_reviews.merge(green, left_on='name', right_on='Name', how='left', suffixes=['_b', '_g'])
testmerge = testmerge[['name', 'text', 'rating']]
print("green: ",testmerge['rating'].sum())
print("not green: ",testmerge['rating'].isnull().sum())
testmerge.to_csv('big_yelp_data/name_review_green.csv')




