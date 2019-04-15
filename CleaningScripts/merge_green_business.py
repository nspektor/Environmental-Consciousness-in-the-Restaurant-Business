#!/usr/bin/env python
# coding: utf-8

# NOTES - 
# I used pandas and did exact matching

# In[1]:


import csv
import pandas as pd
import numpy as np


# # SPARK DataFrame

# Fuzzymatch on restaurant name

import pyspark
sc = pyspark.SparkContext(appName="myAppName")
from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)
from pyspark.sql.session import SparkSession
spark = SparkSession(sc)
from pyspark.sql import functions as F
from pyspark.sql.functions import upper, col, regexp_extract, regexp_replace
from pyspark.sql.functions import levenshtein 

biz = sqlContext.read.format("com.databricks.spark.csv").option("header", "true").option("inferSchema", "true").load('DataSources/all_clean_restaurants.csv')
mybiz = biz

green = sqlContext.read.format("com.databricks.spark.csv").option("header", "true").option("inferSchema", "true").load('DataSources/clean_green.csv')
mygreen = green

mybiz.show()

mygreen = mygreen.withColumnRenamed('Name', 'green_name')
mygreen = mygreen.drop('Address', 'City', 'State', 'Zip')

mygreen.show()

joinedDF = mybiz.join(mygreen, levenshtein(mybiz["name"], mygreen["green_name"]) < 3) 
joinedDF = joinedDF.drop('_c0')
joinedDF.head()

joinedDF.write.csv("business_and_green.csv")


#____________________________________________________________________________________
#PANDAS
# exact match on name

biz = pd.read_csv('DataSources/all_clean_restaurants.csv', header=0, delimiter=',')
green = pd.read_csv('DataSources/clean_green.csv', header=0, delimiter=',')

biz = biz.sort_values(['name'])
green = green.sort_values(['Name'])

biz.head()
green.head()
green.isnull().sum()

testmerge = biz.merge(green, left_on='name', right_on='Name', how='inner', suffixes=['_b', '_g'])
testmerge

##26007
biz.duplicated(subset='name').sum()

testmerge = testmerge.drop(['Unnamed: 0_g','Unnamed: 0_b'], axis=1)
testmerge.head()

testmerge.to_csv('business_green.csv')


