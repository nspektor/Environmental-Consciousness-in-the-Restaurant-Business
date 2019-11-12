# Combine reviews with businesses and add a green rating
import pandas as pd

yelp_reviews = pd.read_csv('../data/original_sources/YelpReview.csv', header=0)
yelp_businesses = pd.read_csv('../data/clean_yelp_restaurants.csv', header=0)

# Yelp Business and Review Data
yelp_businesses = yelp_businesses.drop_duplicates(subset=['business_id'])
yelp_businesses['categories'] = yelp_businesses['categories'].str.replace(',', ' ')

yelp_reviews = yelp_reviews[['business_id', 'text']]
yelp_reviews['text'] = yelp_reviews['text'].str.replace(',', ' ')

yelp_reviews = yelp_reviews.groupby('business_id')['text'].apply(list).to_frame().reset_index()

# merge restaurants with their reviews
restaurants_and_reviews = yelp_businesses.merge(yelp_reviews, left_on='business_id', right_on='business_id',
                                                how='inner', suffixes=['_biz', '_test'])
restaurants_and_reviews = restaurants_and_reviews.groupby('name')['text'].apply(list).to_frame().reset_index()
restaurants_and_reviews = restaurants_and_reviews.sort_values(['name'])
restaurants_and_reviews.to_csv('../data/restaurants_and_reviews.csv', index=False)
small_businesses_and_reviews = restaurants_and_reviews.head(5000)
small_businesses_and_reviews.to_csv('../data/small_restaurants_and_reviews.csv', index=False)

# Add in the GRA data
green = pd.read_csv('../data/clean_green.csv', header=0, delimiter=',')
green = green.sort_values(['Name'])
green = green[['Name', 'rating']]
green.rename(str.lower, axis='columns', inplace=True)

# Add in the Seafood Watch Data
seafood = pd.read_csv('../data/original_sources/SeafoodWatch.csv')
seafood_restaurants = seafood.loc[seafood['PartnerTypes'] == 'Restaurant Partner']


def clean_str(r):
    idx = r.find('(')
    if idx != -1:
        return r[0:idx]
    else:
        return r


seafood = pd.DataFrame(seafood_restaurants['Title'].apply(lambda r: clean_str(r)).unique())
seafood.rename(index=str, columns={0: 'name'}, inplace=True)
seafood['rating'] = 1
seafood = seafood[['name', 'rating']]
seafood['name'] = seafood['name'].str.upper()
green = green.append(seafood, sort=True)
# NO! we should add points for being in both not drop duplicates
green.drop_duplicates(subset="name", inplace=True)

# All together now
name_review_green = restaurants_and_reviews.merge(green, left_on='name', right_on='name', how='left', suffixes=['_b', '_g'])
name_review_green = name_review_green[['name', 'text', 'rating']]
name_review_green = name_review_green.sort_values(['rating'])
print(name_review_green['rating'].value_counts())
small_name_review_green = name_review_green[:56]
name_review_green.to_csv('../data/big_name_review_green.csv')
small_name_review_green.to_csv('../data/small_name_review_green.csv', index=False)
