# Environmental Consciousness in the Restaurant Business 
## Spring 2019 Big Data Science Project
#### Nellie Spektor, Valerie Angulo, Andrea Waxman

- For our project we used Python 3.7.0, NLTK, pandas, NumPy and RapidMiner
- Link to project github: https://github.com/vangul01/BDSProject

## Data Sources
- Yelp dataset: https://www.yelp.com/dataset
- Seafood Watch: https://www.seafoodwatch.org/
- Green Restaurant Association: http://www.dinegreen.com/

## Code
Below are the python scripts we used in order of when they were written. We did not include the source data or files that were generated in this submission, but they can all be found on github or through the yelp dataset website. 

1. json_to_csv.py 
   - Imports: pandas
   - Converted JSON files downloaded from Yelp dataset challenge into csv files.    
2. clean_yelp_businesses.py
    - Imports:  pandas 
    - Explored the Yelp Businesses data
    - Got rid of unwanted columns
    - Removed businesses that were not restaurants (or cafes, bars, etc.)
        - Words we used to fitler restaurants: ['RESTAURANTS','BARS','FOOD','BREAKFAST & BRUNCH','DESSERTS','BAKERIES, DELIS, SANDWICHES', 'COFFEE & TEA', 'DINERS', 'CAFES']
3. clean_GRA_data.py
   - Imports:  pandas
   - Drop unnecessary columns 
   - Capitalize string type columns in order to merge data on restaurant name
4. merge_GRA_with_yelp_restaurants_attempt.py
    - Imports:  pandas, Spark
        ```
        import pyspark
        from pyspark.sql import SQLContext
        from pyspark.sql import functions as F```
    - Combining clean yelp restaurant data with GRA data
    - We did not end up using this script, combine_yelp_and_GRA_restaurant_data.py does this
    - Here we attempted  fuzzy matching using Spark DataFrames and levenshtein distance but results were too varied, even with a distance of 1 so we chose exact matching
5. merge_GRA_with_yelp_restaurants.py
    - Imports:  pandas
    - Merged yelp business and review data into one pandas dataframe by combining the text from each review about a restaurant into one large block of text
        - We merged entries for separate locations of the same franchise into one row in our dataset. 
            - For example, all McDonalds reviews were combined into one row
    - Added a column to the above dataframe to indicate whether the restaurant appeared in the list we got from the Green Restaurant Association.
6. environmental_term_analysis.py
    - Imports:  pandas, NLTK to preprocess review text
    - Create a green rating for each restaurant based on whether it’s reviews contains “environmental” terms. 
        - Examples of environmental terms: compost, recycle, green, local, vegan, vegetarian
        - If 1% or more of the total words in the reviews were environmental words, the restaurant got a score of 3, the rest got scores of 0, 1, or 2 but in our final dataset we only counted those with a score of 3 as “green”
7. create_final_dataset.py
    - Imports:  pandas
    - Combined results from the previous scripts and the Seafood Watch and Blog data to create our final dataset which we uploaded to Rapid Miner
    - The final dataset
        - Columns which indicate “green” score from all of our methods (GRA, Seafood, blogs, green terms)
        - A column that aggregates all of the other green scores into a boolean classification of “green” or “not green”.
        - A column that has the average yelp star-rating of all of the locations of any given restaurant
        - A column with the cleaned review text
    - The actual final dataset had over 51,000 entries, but here we created a smaller version with just over 5000 entries. This is to make the data more manageable and to ensure that we have an equal balance of green and not green restaurants to analyze. 
8. tfidf.py
    - imports:
      ```
      from sklearn.feature_extraction.text import TfidfVectorizer
      from wordcloud import WordCloud, ImageColorGenerator
      import matplotlib
      ```
    - Used the 6000 row final dataset of green/not green data to preprocess transform data into tfidf matrix
    - Preprocessed text reviews for restaurants
    - Explored top words
    - Created word clouds to visualize top words







