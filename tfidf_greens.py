#!/usr/bin/env python
# coding: utf-8

# In[61]:


import numpy as np
import pandas as pd
import csv

import nltk
from nltk.corpus import stopwords
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

# read csv into a dataframe
df_idf = pd.read_csv("DataSources/small_name_review_green.csv")
 
# print schema
print(df_idf.dtypes)
print(df_idf.shape)


# In[62]:


df_idf.head()


# In[63]:


mydfidf = df_idf.copy()
mydfidf = mydfidf.drop('rating', axis=1)


# In[64]:


mydfidf.info()


# In[65]:


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
    #lemmatizer = nltk.stem.WordNetLemmatizer()
    #lemmatizer = WordNetLemmatizer() 
    #lemmatized_output = ([lemmatizer.lemmatize(w) for w in nltk.word_tokenize(text)])# if w not in string.punctuation]))
    #lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in splittext])
    
    return text


# In[66]:


mydfidf['text'] = mydfidf['text'].apply(lambda x:pre_process(x))


# In[67]:


mydfidf.head()


# In[82]:


mydfidf['text'][2]


# In[69]:


def remove_stopwords(mytext):
    #set(stopwords.words('english'))
    stop_words = set(stopwords.words('english')) 
    word_tokens = word_tokenize(mytext) 

    filtered_sentence = [w for w in word_tokens if not w in stop_words] 

    filtered_sentence = [] 

    for w in word_tokens: 
        if w not in stop_words: 
            filtered_sentence.append(w) 
    
    return filtered_sentence


# In[71]:


#def lemma(mytext):
#    lemmatizer = WordNetLemmatizer() 
#    lemmatized_output = [lemmatizer.lemmatize(w) for w in mytext]#splittext]
#    return lemmatized_output


# In[95]:


import nltk

w_tokenizer = nltk.tokenize.WhitespaceTokenizer()
lemmatizer = nltk.stem.WordNetLemmatizer()

def lemmatize_text(text):
    return [' '.join(lemmatizer.lemmatize(w,'v') for w in w_tokenizer.tokenize(text))]


# In[96]:


#clean will have no stopwords, mydfidf will
clean = mydfidf.copy()


# In[97]:


clean['text'] = clean['text'].apply(lambda x:remove_stopwords(x))


# In[98]:


clean['text'] = clean['text'].str.join(' ')


# In[99]:


clean['text_lemmatized'] = clean.text.apply(lemmatize_text)


# In[100]:


clean.head()


# In[101]:


clean['text_lemmatized'][2]


# In[102]:


from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(max_features=300, smooth_idf=True, )#tokenizer=tokens ,use_idf=True, smooth_idf=True, sublinear_tf=False)


# In[103]:


X = vectorizer.fit_transform(clean['text'])


# In[104]:


print(vectorizer.get_feature_names())


# In[105]:


print(X.shape)


# In[ ]:




