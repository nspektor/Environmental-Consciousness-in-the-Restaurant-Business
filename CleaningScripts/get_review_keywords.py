import pandas as pd
import nltk
nltk.download('stopwords')

pd.set_option('display.max_columns', 500)


rdf = pd.read_csv('DataSources/mini_review.csv', header=0)
bdf = pd.read_csv('DataSources/all_clean_restaurants.csv', header=0)

myrdf = rdf[['business_id','text']]
mybdf = bdf.drop_duplicates(subset=['business_id'])
test = myrdf.groupby('business_id')['text'].apply(list).to_frame().reset_index()

mergedf = mybdf.merge(test, left_on='business_id', right_on='business_id', how='inner', suffixes=['_biz', '_rev'])
mergedf['categories'] = mergedf['categories'].str.replace(',', ' ')
mergedf['text'] = mergedf['text'].str.replace(',', ' ')


# mergedf.to_csv('DataSources/cleaned_reviews.csv')

#nltk stuff
stop = nltk.corpus.stopwords.words('english')

myrdf['stopless'] = myrdf['text'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop]))



print(myrdf.head(5));
