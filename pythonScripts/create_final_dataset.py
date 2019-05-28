
# coding: utf-8

# In[151]:


import pandas as pd
yelp_text_env_term_rating = pd.read_csv("big_yelp_data/green_rating_from_yelp_text_and_defined_env_terms_all.csv")
small_name_review_green = pd.read_csv("DataSources/small_name_review_green.csv")


# In[276]:


all_df = yelp_text_env_term_rating.merge(small_name_review_green, left_on='name',right_on='name', how='left', suffixes=['_b', '_g'])


# In[277]:


all_df.drop(['text_g'],axis=1,inplace=True)


# In[278]:


all_df['rating'] += 1
all_df.fillna(0, inplace=True)


# In[279]:


all_df['overall_green_rating'] = all_df['green_rating'] + all_df['rating']
all_df.rename(index=str, columns={'rating':'GRA_rating', 'text_b':'review_text', 'green_rating':'green_words_rating'}, inplace=True)


# In[280]:


all_df.overall_green_rating.value_counts()


# In[281]:


green_alt_data = pd.read_csv("DataSources/green_alt_data.csv")
green_alt_data['Rating (.5 or 1)'][0] = 1
green_alt_data['name'] = green_alt_data['Restaurant Name'].str.upper()
green_alt_data['alt_rating'] = green_alt_data['Rating (.5 or 1)']
green_alt_data.head()


# In[282]:


all_df = all_df.merge(green_alt_data[['name', 'alt_rating']], left_on='name',right_on='name', how='left', suffixes=['_b', '_g'])
all_df.head()


# In[283]:


all_df.fillna(0, inplace=True)
all_df['overall_green_rating'] = all_df['alt_rating'] + all_df['overall_green_rating']


# In[284]:


all_df.overall_green_rating.value_counts().sort_index()


# In[285]:


all_df['green_words_rating'] = all_df['green_words_rating'].replace(1,0)
all_df['overall_green_rating'] = all_df['green_words_rating'] + all_df['GRA_rating'] + all_df['alt_rating']
all_df.overall_green_rating.value_counts().sort_index()


# In[286]:


all_df['green_boolean'] = all_df['overall_green_rating']
all_df['green_boolean'] = all_df['green_boolean'].replace(to_replace=[2,3,4,5,6],value='green')
all_df['green_boolean'] = all_df['green_boolean'].replace(to_replace=[0,1],value='not_green')
# all_df['overall_green_rating'] = all_df['overall_green_rating'].replace(to_replace=2,value=1)

all_df.green_boolean.value_counts()


# In[287]:


# all_df[['name','review_text','green_boolean']].to_csv('DataSources/green_not_green_all.csv')


# In[288]:


# small_df = all_df[['name','review_text','green_boolean']].sort_values('green_boolean')
small_df = all_df[['name','review_text','green_boolean']].sort_values('green_boolean')[:1000]
small_df = small_df.append(all_df[['name','review_text','green_boolean']].sort_values('green_boolean', ascending=False)[:1000])
small_df.green_boolean.value_counts()


# In[289]:


small_df.to_csv('DataSources/green_not_green_2000.csv')


# In[290]:


greenest_words = pd.read_csv('DataSources/greenest.csv')
greenest_words.head()


# In[291]:


all_df = all_df.merge(greenest_words[['name', 'green_rating']], left_on='name',right_on='name', how='left', suffixes=['_old', '_new'])
all_df.head()


# In[292]:


all_df.fillna(0, inplace=True)
all_df['green_rating'].replace(3,1,inplace=True)
all_df['overall_green_rating'] = all_df['overall_green_rating'] + all_df['green_rating']
all_df.head()


# In[293]:


all_df['green_boolean'] = all_df['overall_green_rating']
all_df['green_boolean'] = all_df['green_boolean'].replace(to_replace=[3,4,5,6,7],value='green')
all_df['green_boolean'] = all_df['green_boolean'].replace(to_replace=[0,1,2],value='not_green')
# all_df['overall_green_rating'] = all_df['overall_green_rating'].replace(to_replace=2,value=1)

all_df.green_boolean.value_counts()


# In[294]:


small_df = all_df[['name','review_text','green_boolean']].sort_values('green_boolean')[:2598]
small_df = small_df.append(all_df[['name','review_text','green_boolean']].sort_values('green_boolean', ascending=False)[:2598])
small_df.green_boolean.value_counts()


# In[295]:


small_df.to_csv('DataSources/for_sure_green_not_green_5000.csv')


# In[296]:


all_df = all_df.rename({"green_words_rating":"less_stingent_gwr"})
all_df = all_df.rename({"green_rating":"green_words_rating"})


# In[297]:


all_df[['name', 'review_text', 'green_boolean','overall_green_rating', 'GRA_rating', 'green_words_rating','alt_rating']][::20]


# In[298]:


yelp_businesses = pd.read_csv('DataSources/all_clean_restaurants.csv', header=0)
yelp_businesses = yelp_businesses[['name', 'stars']]
yelp_businesses.head()


# In[299]:


yelp_businesses = yelp_businesses.groupby(['name']).mean()
yelp_businesses.head()


# In[300]:


all_df = all_df.merge(yelp_businesses, left_on='name',right_on='name', how='left', suffixes=['_old', '_new'])


# In[305]:


all_df[['name', 'review_text', 'green_boolean','overall_green_rating', 'GRA_rating', 'green_words_rating','alt_rating', 'stars']][:10]


# In[322]:


small_df = all_df[['name','review_text','green_boolean', 'stars']].sort_values('green_boolean')[:2598]
small_df = small_df.append(all_df[['name','review_text','green_boolean','stars']].sort_values('green_boolean', ascending=False)[:2598])
small_df = small_df.round(2)

small_df.head()




# In[326]:


small_df.head()


# In[324]:


small_df['stars'] = pd.cut(small_df['stars'], bins=[0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5], labels = [0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5])

# In[327]:


small_df.to_csv('DataSources/green_not_green_with_stars_5000.csv')


# In[347]:


green_stars = pd.DataFrame(small_df.loc[small_df['green_boolean'] == 'green']['stars'].value_counts().sort_index(ascending=False))
green_stars


# In[348]:


small_df.loc[small_df['green_boolean'] == 'green']['stars'].value_counts().sort_index(ascending=False)


# In[356]:


small_df.loc[small_df['green_boolean'] == 'not_green']['stars'].value_counts().sort_index(ascending=False)


# In[357]:


green_stars.rename(columns ={'stars':'Green Restaurants'}, inplace=True)


# In[358]:


green_stars['Non-Green Restaurants'] = small_df.loc[small_df['green_boolean'] == 'not_green']['stars'].value_counts().sort_index(ascending=False)
green_stars


# In[359]:


green_stars.to_csv('green_non_green_stars.csv')

