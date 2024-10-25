import numpy as np
import pandas as pd

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df = pd.read_csv(r'C:\Users\User\OneDrive\Desktop\ML_Practice\Practice\NLP\Text Preprocessing\IMDB Dataset.csv')

df.head()
df['review'].str.lower()

# remove html tags

import re   
def clean_text(text):
    text = re.sub(r'<.*?>', '', text)
    return text

text = '<h1> this is a heading </h1>'
clean_text(text)

df['review'] = df['review'].apply(clean_text)

# remove url
def remove_url(text):
    url = re.compile(r'https?://\S+|www\.\S+')
    return url.sub(r'', text)

text1= 'this is a url https://www.google.com'
remove_url(text1)

# remove punctuation
import string,time
string.punctuation

exclude=string.punctuation

def remove_punc(text):
    for char in exclude:
        text=text.replace(char,'')
    return text

text2 = 'string.with.punctuation!'

start = time.time()
print(remove_punc(text2))
print('Time taken:', time.time()-start)

# technique 2(faster)
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

start = time.time()
print(remove_punctuation(text2))
print('Time taken:', time.time()-start)

# spelling correction
from textblob import TextBlob
incorrect_text = 'I havv goood speling'
correct_text = TextBlob(incorrect_text).correct()
print(correct_text)

# remove stopwords
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stop = stopwords.words('english')

def remove_stopwords(text):
    new_text=[]
    for word in text.split():
        if word not in stop:
            new_text.append(word)
        else:
            new_text.append('')
    x=new_text[:]
    new_text.clear()
    return ' '.join(x)

text3 = 'this is a sample text with stopwords'
remove_stopwords(text3)

df['review'] = df['review'].apply(remove_stopwords)

# remove emojis
# 1.remove

import re
def remove_emoji(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

text4 = 'this is a sample text with emojis 😜'
remove_emoji(text4)
# 2. replace
import emoji
def replace_emoji(text):
    return emoji.demojize(text)
text5 = 'this is a sample text with emojis 😜'
replace_emoji(text5)

# tokenization
# 1. word tokenization
sent1 = 'this is a sample sentence'
sent1.split()
# 2. sentence tokenization
sent2= 'this is a sample sentence. this is another sentence'
sent2.split('.')
# problems with split
sent3 = 'this is a sample sentence. this is another sentence!'
sent3.split('.')
# 2.using regex
import re
re.split(r'[.!?]', sent3)
# 3. using nltk
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize
sent_tokenize(sent3)
word_tokenize(sent3)
# 4.spacy
import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp(sent3)
for token in doc:
    print(token.text)

# stemming
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
def stem_text(text):
    return ' '.join([stemmer.stem(word) for word in text.split()])

stem_text('I am running very fastly')
# lemmatization
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

sentence = 'The striped bats are hanging on their feet for best'
punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
sentence = ''.join(ch for ch in sentence if ch not in set(punctuation))
words = sentence.split()
words = [lemmatizer.lemmatize(word) for word in words]
print(' '.join(words))




