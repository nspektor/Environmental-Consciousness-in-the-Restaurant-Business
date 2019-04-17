# to combine reviews with businesses and add a green rating
import pandas as pd

# rdf = pd.read_csv('DataSources/mini_review.csv', header=0)
rdf = pd.read_csv('big_yelp_data/review.csv', header=0)
bdf = pd.read_csv('DataSources/all_clean_restaurants.csv', header=0)
greendf = pd.read_csv('DataSources/business_green.csv', header=0)
bdf = bdf.drop_duplicates(subset=['business_id'])
bdf['categories'] = bdf['categories'].str.replace(',', ' ')

rdf = rdf[['business_id', 'text']]
rdf['text'] = rdf['text'].str.replace(',', ' ')

print("bdf:\n", bdf.info())
result_df = rdf.groupby('business_id')['text'].apply(list).to_frame().reset_index()
print("result_df:\n", result_df.get(0))
businesses_and_reviews = bdf.merge(result_df, left_on='business_id', right_on='business_id', how='inner',
                                   suffixes=['_biz', '_test'])
businesses_and_reviews = businesses_and_reviews.groupby('name')['text'].apply(list).to_frame().reset_index()

green = pd.read_csv('DataSources/clean_green.csv', header=0, delimiter=',')

businesses_and_reviews = businesses_and_reviews.sort_values(['name'])
green = green.sort_values(['Name'])

nameRevGreen = businesses_and_reviews.merge(green, left_on='name', right_on='Name', how='left', suffixes=['_b', '_g'])
nameRevGreen = nameRevGreen[['name', 'text', 'rating']]
print("green: ", nameRevGreen['rating'].sum())
print("not green: ", nameRevGreen['rating'].isnull().sum())
nameRevGreen.to_csv('big_yelp_data/name_review_green.csv')
