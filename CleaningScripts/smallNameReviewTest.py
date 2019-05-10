import pandas as pd

smallNameReviewGreen = pd.read_csv('../DataSources/small_name_review_green.csv', header=0)
smallNameReviewGreen = smallNameReviewGreen[['name', 'rating', 'text']]
print(smallNameReviewGreen.info())

# get rid of punctuation and weirdness
