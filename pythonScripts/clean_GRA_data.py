# Cleans GRA.csv, drops name duplicated and converts rating to integer
import pandas as pd

filename = '../data/original_sources/GRA.csv'
df = pd.read_csv(filename, encoding="ISO-8859-1", header=-1, na_filter=' ')
df = df.rename(columns=
               {0: 'Name', 1: 'Address', 2: 'City', 3: 'State', 4: 'Zip', 5: 'PhoneNum', 6: 'website', 7: 'rating'})

full = df
full = full.drop(columns=['PhoneNum'])
full = full.drop(columns=['website'])
full['rating'] = full['rating'].str.extract('(\d+)')
full.Name = full.Name.str.strip().str.upper()
full.Address = full.Address.str.strip().str.upper()
full.City = full.City.str.strip().str.upper()
full.State = full.State.str.strip().str.upper()
full.Zip = full.Zip.str.strip()
full.rating = full.rating.str.strip()


full = full.drop_duplicates(subset=['Name'], keep='first', inplace=False)

full.to_csv('../data/clean_green.csv')
print(full.Name.count(), "Restaurants in GRA Data")


