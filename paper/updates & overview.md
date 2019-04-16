# Updates on our project:
*as of 4/09/19*


1. Defining restaurant success (features to look at)

-Does the restaurant offer a unique experience, (ie. unique food, unique presentation of food, unique decorations, unique music, etc)
-Does the restaurant generate traffic during slow times? Perhaps by offering special promotions during off-peak times.
-Does the restaurant receive good ratings & positive reviews? (Yelp 'highly recommended')
-Is the restaurant clean? (inspection grade, rat calls in area, yelp reviews about clean/dirty)
-Does the restaurant offer quality food? (Yelp reviews, check to mention 'quality', 'hair in food', 'plastic', 'fresh', 'organic', 'smell')
-Does the restaurant have multiple locations? Has it expanded? How many customers does it have? (can give us insight to how much money it has to pay its employees)
-Is the restaurant part of GRA (with high grade) or Seafood Watch?

2. Data sources:
-Yelp
-GRA
-Seafood Watch


3. Cleaned data using Pandas Python -

__GRA:__

Green restaurants in NY (tri-state area)/ Total # of restaurants:
119 / 603

__Yelp data:__

number of Businesses in NY / Total # of businesses:
__ /192609

Restaurants in NY / Total Restaurants (USA):
13 / 77332

New York Yelp Reviews / Yelp Reviews Total
Need to filter. Not clean yet

__Seafood Watch__

number of Restaurants in NY / Total Restaurants
Not clean yet. *********

__Overview of plan & next steps:__

- join business reviews
- separate into training (GRA) and test data (not GRA)
- Preprocessing:
- run TFIDF --> K-means

- Deploy, visualize, etc

__Future potential steps:__
Prove/show correlation does Green =?= Success

Meeting 4/16/19

Split data set into labeled and unlabeled.
What constitutes labeled data? Anything with a higher grade than zero.
If it appears in green restaurant data, keep their ratings
Seafood watch appearance weight_?_
Green rating + seafood rating 

