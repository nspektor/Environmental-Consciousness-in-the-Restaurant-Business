
# coding: utf-8

# In[139]:


environmentalTerms = [line.rstrip('\n') for line in open("DataSources/environmentalTerms.txt")]
environmentalTerms = list(dict.fromkeys(environmentalTerms))


# In[146]:


import pandas as pd
businesses_and_reviews = pd.read_csv("DataSources/businesses_and_reviews.csv")


# In[147]:


businesses_and_reviews.shape


# In[148]:


import nltk
from nltk.corpus import stopwords
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize

from nltk.stem import WordNetLemmatizer 
import re
def pre_process(text):

    # lowercase
    text=text.lower()
    
    #remove tags
    text=re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",text)
    
    # remove special characters and digits
    text=re.sub("(\\d|\\W)+"," ",text)
    
    #splittext = text.split(' ')
    #lemmatizer = WordNetLemmatizer() 
    
    #lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in splittext])
    
    return text#lemmatized_output

businesses_and_reviews['text'] = businesses_and_reviews['text'].apply(lambda x:pre_process(x))


# In[150]:


def get_env_terms(text):
    terms = environmentalTerms
#     text = text.split(' ')
#     print(terms)
#     print(text)
    env_terms_in_text =  [term for term in terms if term in text ]
    return ', '.join(env_terms_in_text)

def get_env_term_counts(rest):
    sum = 0
    for term in rest['env_terms'].split(", "):
#         print(term , " count " , rest['text'].count(term))
        if term != '':
            sum += rest['text'].count(term)
    if sum == 0:
        print('wat')
    return sum


# In[151]:


# businesses_and_reviews['env_terms'] = businesses_and_reviews['text'].apply(lambda x:get_env_terms(x))
# businesses_and_reviews.head()


# In[152]:


businesses_and_reviews.shape


# In[153]:


businesses_and_reviews_1000 = businesses_and_reviews.copy(deep = True)
# businesses_and_reviews_1000.to_csv('businesses_and_reviews_1000.csv')
# businesses_and_reviews_1000.head()


# In[154]:


businesses_and_reviews_1000['env_terms'] = businesses_and_reviews_1000['text'].apply(lambda x:get_env_terms(x))
businesses_and_reviews_1000['env_term_counts'] = businesses_and_reviews_1000[['text','env_terms']].apply(lambda x: get_env_term_counts(x), axis=1)
businesses_and_reviews_1000.sort_values(['env_term_counts'], ascending=False, inplace=True)


# In[155]:


businesses_and_reviews_1000['env_terms_percent_of_overall_words'] = (businesses_and_reviews_1000['env_term_counts']/businesses_and_reviews_1000['text'].str.split().apply(len)) * 100
# businesses_and_reviews_1000['env_terms_percent_of_overall_words'].value_counts()

businesses_and_reviews_1000['len'] = businesses_and_reviews_1000['text'].str.split().apply(len)
businesses_and_reviews_1000['env_terms_percent_of_overall_words'] = (businesses_and_reviews_1000['env_term_counts']/businesses_and_reviews_1000['len'])
businesses_and_reviews_1000['env_terms_percent_of_overall_words'] *= 100
# businesses_and_reviews_1000[['name','len', 'env_term_counts','env_terms_percent_of_overall_words']]
# businesses_and_reviews_1000.loc[486]


# In[156]:


businesses_and_reviews_1000[['name','len', 'env_terms','env_term_counts','env_terms_percent_of_overall_words']]


# In[157]:


businesses_and_reviews_1000['env_terms_percent_of_overall_words'].describe()


# In[164]:


bins = [-1,0.01,0.3,1, 100]
labels = [0,1,2,3]
businesses_and_reviews_1000['green_rating'] = pd.cut(businesses_and_reviews_1000['env_terms_percent_of_overall_words'], bins=bins, labels=labels)








# In[166]:


businesses_and_reviews_1000['green_rating'].value_counts()


# In[168]:


greenest = businesses_and_reviews_1000.loc[businesses_and_reviews_1000['green_rating'] == 3]
greenest[['name','text','green_rating']].to_csv('DataSources/greenest.csv')


# In[167]:


businesses_and_reviews_1000[['name','text','green_rating']].to_csv('big_yelp_data/green_rating_from_yelp_text_and_defined_env_terms_all.csv',index=False)


# In[ ]:


businesses_and_reviews_1000[['name','text','green_rating']]


# In[ ]:


businesses_and_reviews_1000.shape

