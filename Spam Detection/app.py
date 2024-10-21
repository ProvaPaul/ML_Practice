import nltk
import pandas as pd
pd.set_option('display.max_colwidth',100)
messages= pd.read_csv(r'C:\Users\User\OneDrive\Desktop\ML_Practice\Practice\Spam Detection\spam.csv',encoding="latin-1")

# drop unused columns
columns_to_drop=['Unnamed: 2','Unnamed: 3','Unnamed: 4']
messages=messages.drop(columns=columns_to_drop,axis=1)
messages.columns=['label','text']
messages['label'].value_counts()
print('Number of nulls in label:{}'.format(messages['label'].isnull().sum()))
print('Number of nulls in text:{}'.format(messages['text'].isnull().sum()))
messages.head()

messages['label'].value_counts()

# Data Cleaning and Preprocessing
import re
import string
stopwords=nltk.corpus.stopwords.words('english')
print(stopwords)


def clean_text(text):
    text="".join([word.lower() for word in text if word not in string.punctuation])
    tokens=re.split(r'\W+',text)
    text=[word for word in tokens if word not in stopwords]
    return text 
clean_text('I am learning NLP')

# TF-IDF VECTORISATION
# APPLY TfidfVectorizer

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vect=TfidfVectorizer(analyzer=clean_text)
X_tfidf=tfidf_vect.fit_transform(messages['text'])
print(X_tfidf.shape)
print(tfidf_vect.get_feature_names_out())


# Feature Engineering
X_features=pd.DataFrame(X_tfidf.toarray())
X_features.head()

# random forest classifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score,recall_score
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X_features,messages['label'],test_size=0.2)
rf=RandomForestClassifier()
rf_model=rf.fit(X_train,y_train)

# Predictions
y_pred=rf_model.predict(X_test)
precision=precision_score(y_test,y_pred,pos_label='spam')
recall=recall_score(y_test,y_pred,pos_label='spam')
print('Precision:{} / Recall:{}'.format(round(precision,3),round(recall,3)))
# manual testing

text=["Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005."]
text_tfidf=tfidf_vect.transform(text)
X_features=pd.DataFrame(text_tfidf.toarray())
X_features.head()

y_pred=rf_model.predict(text_tfidf)
y_pred