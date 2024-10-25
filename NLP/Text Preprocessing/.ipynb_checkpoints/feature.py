import numpy as np
import pandas as pd

df=pd.DataFrame({'text':['people watch campusx','campusx watch campusx','people write comment','campusx write comment'],'output':[1,1,0,0]})

from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer()
# count vectorizer
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(ngram_range=(2,2))
bow=cv.fit_transform(df['text'])

print(cv.vocabulary_)

print(bow[0].toarray())
print(bow[1].toarray())

cv.transform(["campusx watch and write comment of campusx"]).array()
# tfidf vectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf=TfidfVectorizer()
tfidf_matrix=tfidf.fit_transform(df['text'])
print(tfidf_matrix.toarray())

print(tfidf.idf_)
print(tfidf.get_feature_names_out())