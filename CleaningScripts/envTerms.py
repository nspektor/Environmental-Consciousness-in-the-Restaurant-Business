import pandas as pd
businesses_and_reviews = pd.read_csv("DataSources/businesses_and_reviews.csv")

environmentalTerms = [line.rstrip('\n') for line in open("DataSources/environmentalTerms.txt")]

def get_env_terms(text):
    env_terms_in_text = [word for word in text if word in environmentalTerms]
    return ', '.join(env_terms_in_text)

businesses_and_reviews['env_terms'] = businesses_and_reviews['text'].apply(lambda x:get_env_terms(x))
businesses_and_reviews.head()