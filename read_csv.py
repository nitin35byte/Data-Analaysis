# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vZX0KvNU5YXWlXE1uKmUvx5093FXruob
"""

## Opening a csv file from an URL

import pandas as pd
import requests
from io import StringIO
url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0"}
req = requests.get(url, headers=headers)
data = StringIO(req.text)

pd.read_csv(data)

## Sep Parameter

pd.read_csv("https://raw.githubusercontent.com/campusx-official/100-days-of-machine-learning/main/day15%20-%20working%20with%20csv%20files/movie_titles_metadata.tsv", sep="\t" , names=['sno','name','release_year','rating','votes','genres'])

##. Index_col parameter

pd.read_csv("https://raw.githubusercontent.com/campusx-official/100-days-of-machine-learning/main/day15%20-%20working%20with%20csv%20files/aug_train.csv",index_col='enrollee_id')

## Header parameter

pd.read_csv("https://raw.githubusercontent.com/campusx-official/100-days-of-machine-learning/main/day15%20-%20working%20with%20csv%20files/test.csv",header=1)

##use_cols parameter

pd.read_csv("https://raw.githubusercontent.com/campusx-official/100-days-of-machine-learning/main/day15%20-%20working%20with%20csv%20files/aug_train.csv" ,usecols=['enrollee_id','gender','education_level'])

##Squeeze parameters

pd.read_csv('https://raw.githubusercontent.com/campusx-official/100-days-of-machine-learning/main/day15%20-%20working%20with%20csv%20files/aug_train.csv',usecols=['gender'],squeeze=True)

##Loading a huge dataset in chunks

dfs = pd.read_csv('https://raw.githubusercontent.com/campusx-official/100-days-of-machine-learning/main/day15%20-%20working%20with%20csv%20files/aug_train.csv',chunksize=5000)

for chunks in dfs:
  print(chunks.shape)

##Handling Dates

pd.read_csv("https://raw.githubusercontent.com/campusx-official/100-days-of-machine-learning/main/day15%20-%20working%20with%20csv%20files/IPL%20Matches%202008-2020.csv" , parse_dates=['date']).info()

##dtypes parameter

pd.read_csv('aug_train.csv',dtype={'target':int}).info()

##. Skip bad lines

pd.read_csv('BX-Books.csv', sep=';', encoding="latin-1",error_bad_lines=False)

##Convertors

pd.read_csv('IPL Matches 2008-2020.csv',converters={'team1':rename})

##na_values parameter

pd.read_csv('aug_train.csv',na_values=['Male',])

##Encoding parameter

pd.read_csv('zomato.csv',encoding='latin-1')

##Skiprows/nrows Parameter

pd.read_csv('aug_train.csv',nrows=100)

