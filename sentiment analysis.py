# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Get the sentiment of text from a website

#pip install newspaper3k

# import the libraries
from textblob import TextBlob
import nltk
from newspaper import Article

# Get the article
#Custom URL
url='' 
article=Article(url)

# Do some NLP
article.download()
article.parse()
nltk.download('punkt')
article.nlp()

# Get the summary of the article
text = article.summary

# print the text 
print(text)

# Creating a TextBlob object
obj = TextBlob(text)

#this returns a value between -1 and 1
sentiment = obj.sentiment.polarity
print(sentiment)

if sentiment == 0:
  print('The text is neutral')
elif sentiment > 0:
  print('The text is positive')
else:
  print('The text is negative')

