#!/usr/bin/env python
# coding: utf-8

# In[129]:


import numpy as np
import pandas as pd
import csv

import nltk
from nltk.corpus import stopwords
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

# read csv into a dataframe
df_idf = pd.read_csv("BDSProject/DataSources/small_name_review_green.csv")
 
# print schema
print(df_idf.dtypes)
print(df_idf.shape)


# In[130]:


df_idf.head()


# In[131]:


mydfidf = df_idf.copy()
mydfidf = mydfidf.drop('rating', axis=1)


# In[132]:


mydfidf.info()


# In[133]:


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


# In[134]:


mydfidf['text'] = mydfidf['text'].apply(lambda x:pre_process(x))


# In[135]:


mydfidf.head()


# In[136]:


mydfidf['text'][2]


# In[117]:


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


# In[141]:


def lemma(mytext):
    #splittext = mytext.split(' ')
    lemmatizer = WordNetLemmatizer() 
    
    lemmatized_output = [lemmatizer.lemmatize(w) for w in mytext]#splittext]
    #print(lemmatized_output)
    #text = lemmatizer.lemmatize(text)
    return lemmatized_output


# In[139]:


#clean will have no stopwords, mydfidf will
clean = mydfidf.copy()


# In[140]:


clean['text'] = clean['text'].apply(lambda x:remove_stopwords(x))


# In[144]:


clean['text'] = clean['text'].apply(lambda x:lemma(x))


# In[142]:


clean.head()


# In[148]:


clean['text'] = clean['text'].str.join(' ')


# In[149]:


clean.head()


# In[150]:


clean['text'][2]


# In[146]:


from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(max_features=300, smooth_idf=True, )#tokenizer=tokens ,use_idf=True, smooth_idf=True, sublinear_tf=False)


# In[151]:


X = vectorizer.fit_transform(clean['text'])


# In[152]:


print(vectorizer.get_feature_names())


# In[153]:


print(X.shape)


# In[ ]:


X


# In[ ]:




