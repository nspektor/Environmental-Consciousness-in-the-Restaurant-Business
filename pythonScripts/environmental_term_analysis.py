import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from nltk.stem import WordNetLemmatizer
import re

environmentalTerms = [line.rstrip('\n') for line in open("../data/helper_files/environmentalTerms.txt")]
environmentalTerms = list(dict.fromkeys(environmentalTerms))
restaurants_and_reviews = pd.read_csv("../data/small_name_review_green.csv")
restaurants_and_reviews = restaurants_and_reviews.head(500)


def pre_process(text):
    # lowercase
    text = text.lower()

    # remove tags
    text = re.sub("&lt;/?.*?&gt;", " &lt;&gt; ", text)

    # remove special characters and digits
    text = re.sub("(\\d|\\W)+", " ", text)

    # splittext = text.split(' ')
    # lemmatizer = WordNetLemmatizer()

    # lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in splittext])

    return text  # lemmatized_output


restaurants_and_reviews['text'] = restaurants_and_reviews['text'].apply(lambda x: pre_process(x))


# def get_env_terms(text):
#     terms = environmentalTerms
#     #     text = text.split(' ')
#     env_terms_in_text = [term for term in terms if term in text]
#     return ', '.join(env_terms_in_text)


def get_env_term_counts(restaurant):
    terms = environmentalTerms
    env_terms_in_text = [term for term in terms if term in restaurant['text']]
    # sum = 0
    # for term in restaurant['env_terms'].split(", "):
    #     #         print(term , " count " , rest['text'].count(term))
    #     if term != '':
    #         sum += restaurant['text'].count(term)
    return len(env_terms_in_text)


restaurants_and_reviews['env_term_counts'] = restaurants_and_reviews.apply(
    lambda x: get_env_term_counts(x), axis=1)
restaurants_and_reviews.sort_values(['env_term_counts'], ascending=False, inplace=True)

restaurants_and_reviews['len'] = restaurants_and_reviews['text'].str.split().apply(len)

restaurants_and_reviews['env_terms_percent_of_overall_words'] = (
        restaurants_and_reviews['env_term_counts'] / restaurants_and_reviews['len'])
restaurants_and_reviews['env_terms_percent_of_overall_words'] *= 100

bins = [-1, 0.01, 0.3, 1, 100]
labels = [0, 1, 2, 3]
restaurants_and_reviews['term_based_green_rating'] = pd.cut(restaurants_and_reviews['env_terms_percent_of_overall_words'],
                                                 bins=bins, labels=labels)

# greenest = businesses_and_reviews.loc[businesses_and_reviews['green_rating'] == 3]
# greenest[['name', 'text', 'green_rating']].to_csv('../data/greenest.csv')

restaurants_and_reviews[['name', 'text', 'term_based_green_rating']].to_csv(
    '../data/small_term_based_green_rating_results.csv', index=False)

restaurants_and_reviews.to_csv('small_comprehensive_results.csv', index=False)