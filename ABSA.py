
import pandas as pd
import numpy as np
import csv
#/Library/Frameworks/Python.framework/Versions/3.8
import nltk
from nltk import pos_tag
from sklearn.feature_extraction.text import CountVectorizer
import spacy
import re

from gensim.models import Word2Vec

df = pd.DataFrame(pd.read_csv(r'/Users/martintin/downloads/instacart_ratings.csv'))


df.drop(df.columns[0],inplace=True, axis=1)

#data cleaning

df = df.rename(columns={'comments':'Comments'})
#renames column "comments" to "Comments"
df['Comments'] = df['Comments'].str.lower()
#makes all reviews lower case
df['Comments'] = df['Comments'].str.replace(r'[^\x00-\x7F]+', '')
#removes emojis
df['Comments'] = df['Comments'].str.replace(r' +', ' ')
#remove double spaces
df['Comments'] = df['Comments'].str.replace(r'\d+', '')
#removes number
df = df.dropna()

df['Comments'] = df['Comments'].str.cat()
df['Comments'] = df['Comments'][0]
#makes it into one string
sentences = nltk.sent_tokenize(df['Comments'][0]) #tokenize sentences
nouns = [] #empty to array to hold all nouns

for sentence in sentences:
     for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
         if (pos == 'NN'):
             nouns.append(word)
 

print(nouns)
def pos_tagging(df):
	pass	
