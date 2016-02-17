import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk import pos_tag
from nltk import PorterStemmer

st = PorterStemmer()

def preprocess(data):
  preprocessed_data = []
  for d in data:
    tweets = []
    for tweet in d:
      #tweet_sents = sent_tokenize(tweet)
      tweet_words = word_tokenize(tweet)
      tweet_pos = pos_tag([unicode(word,"utf-8") for word in tweet_words])
      tweets.append([(st.stem(word),pos) for (word,pos) in tweet_pos])
    preprocessed_data.append(tweets)
  return preprocessed_data