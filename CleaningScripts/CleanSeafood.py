import pandas as pd
filename = 'DataSources/Current Certified Green Restaurants.csv'
df = pd.read_csv(filename, encoding = "ISO-8859-1", header = -1, na_filter = ' ')