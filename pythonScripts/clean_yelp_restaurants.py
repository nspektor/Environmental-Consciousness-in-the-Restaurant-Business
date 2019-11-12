# Filters out YelpBusiness.csv for restaurant keywords

import pandas as pd

filename = '../data/original_sources/YelpBusiness.csv'
df = pd.read_csv(filename, delimiter=',')

my_df = df[[
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

# make all strings caps and trim string
my_df['categories'] = my_df['categories'].str.strip().str.upper()
my_df['name'] = my_df['name'].str.strip().str.upper()
my_df['address'] = my_df['address'].str.strip().str.upper()
my_df['state'] = my_df['state'].str.strip().str.upper()
my_df['city'] = my_df['city'].str.strip().str.upper()

restaurant_words = ['RESTAURANTS', 'BARS', 'FOOD',
                    'BREAKFAST & BRUNCH', 'DESSERTS',
                    'BAKERIES, DELIS, SANDWICHES',
                    'COFFEE & TEA', 'DINERS', 'CAFES']
pattern = '|'.join(restaurant_words)
my_df['restaurant'] = my_df.categories.str.contains(pattern)
my_df = my_df.dropna(subset=['categories', 'restaurant'])

restaurants = my_df[my_df.restaurant]
print(restaurants.head())
restaurants = restaurants.drop(['restaurant'], axis=1)
restaurants.to_csv('../data/clean_yelp_restaurants.csv')
