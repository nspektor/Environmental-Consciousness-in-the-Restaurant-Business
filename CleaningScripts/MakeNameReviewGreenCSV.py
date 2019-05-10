# to combine reviews with businesses and add a green rating
import pandas as pd

# rdf = pd.read_csv('DataSources/mini_review.csv', header=0)
yelp_reviews = pd.read_csv('big_yelp_data/review.csv', header=0)
yelp_businesses = pd.read_csv('DataSources/all_clean_restaurants.csv', header=0)
# greendf = pd.read_csv('DataSources/business_green.csv', header=0)

# Yelp Business and Review Data
yelp_businesses = yelp_businesses.drop_duplicates(subset=['business_id'])
yelp_businesses['categories'] = yelp_businesses['categories'].str.replace(',', ' ')

yelp_reviews = yelp_reviews[['business_id', 'text']]
yelp_reviews['text'] = yelp_reviews['text'].str.replace(',', ' ')

print("yelp_businesses:\n", yelp_businesses.head())
yelp_reviews = yelp_reviews.groupby('business_id')['text'].apply(list).to_frame().reset_index()
print("yelp_reviews:\n", yelp_reviews.head())
# merge businesses and reviews
businesses_and_reviews = yelp_businesses.merge(yelp_reviews, left_on='business_id', right_on='business_id', how='inner',
                                               suffixes=['_biz', '_test'])
businesses_and_reviews = businesses_and_reviews.groupby('name')['text'].apply(list).to_frame().reset_index()
businesses_and_reviews = businesses_and_reviews.sort_values(['name'])

# Green Restaurant Association Data
green = pd.read_csv('DataSources/clean_green.csv', header=0, delimiter=',')
green = green.sort_values(['Name'])
green = green[['Name', 'rating']]
green.rename(str.lower, axis='columns', inplace=True)

# Seafood Watch Data
seafood= pd.read_csv('DataSources/original_sources/SeafoodWatch.csv')
seafoodRestaurants = seafood.loc[seafood['PartnerTypes'] == 'Restaurant Partner']

def clean_str(r):
    idx = r.find('(')
    if idx != -1:
        return r[0:idx]
    else:
        return r

restaurantNames = seafoodRestaurants['Title'].apply(lambda r: clean_str(r)).unique()
seafood = pd.DataFrame(restaurantNames)
seafood.rename(index=str, columns={0:'name'},inplace=True)
seafood['rating'] = 1
seafood = seafood[['name', 'rating']]
seafood['name'] = seafood['name'].str.upper()
print('seafood shape: ',seafood.shape)
print('green shape:' ,green.shape)
green = green.append(seafood, sort=True)
green.drop_duplicates(subset ="name", inplace = True)
# print('green:\n',green[::15])
print('post drop shape:', green.shape)



nameRevGreen = businesses_and_reviews.merge(green, left_on='name', right_on='name', how='left', suffixes=['_b', '_g'])
nameRevGreen = nameRevGreen[['name', 'text','rating']]
nameRevGreen = nameRevGreen.sort_values(['rating'])
print("green: ", nameRevGreen['rating'].sum())
print("not green: ", nameRevGreen['rating'].isnull().sum())
# nameRevGreen.to_csv('big_yelp_data/name_review_green.csv')
smallNameReviewGreen = nameRevGreen[:84]
smallNameReviewGreen.to_csv('DataSources/small_name_review_green.csv', index=False)
