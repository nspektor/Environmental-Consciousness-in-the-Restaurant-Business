#Cleans Current Certified Green Restaurants.csv, drops name duplicated and converts rating to integer

import csv
import pandas as pd
import numpy as np

filename = 'DataSources/Current Certified Green Restaurants.csv'
df = pd.read_csv(filename, encoding = "ISO-8859-1", header = -1, na_filter = ' ')
df = df.rename(columns = {0: 'Name', 1: 'Address', 2: 'City', 3: 'State', 4: 'Zip', 5: 'PhoneNum', 6: 'website', 7: 'rating'})

df.head()
#df.dropna()
#df.dtypes


#ny = df.loc[(df['State'] == 'NY')] 
#nj = df.loc[(df['State'] == 'NJ')]
#ct = df.loc[(df['State'] == 'CT')]
#full = ny.append(nj, ignore_index = True) 

full = df
full.head()

#full = full.append(ct, ignore_index = True) 
#full.head()

full = full.drop(columns = ['PhoneNum'])
full = full.drop(columns = ['website'])
full['rating'] = full['rating'].str.extract('(\d+)')
full


full.Name = full.Name.str.strip().str.upper()
full.Address = full.Address.str.strip().str.upper()
full.City = full.City.str.strip().str.upper()
full.State = full.State.str.strip().str.upper()
full.Zip = full.Zip.str.strip()
full.rating = full.rating.str.strip()


full = full.drop_duplicates(subset=['Name'], keep='first', inplace=False)
#from 582 to 573 rows
#full = full.drop_duplicates(subset=['Name', 'City', 'State'], keep='first', inplace=False)
#from ~608 to 582 rows
full

full.to_csv('clean_green.csv')
full.isna().sum()


