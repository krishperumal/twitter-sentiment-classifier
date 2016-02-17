import re
import vocabulary_generator
import nltk
from nltk import PorterStemmer

positive_words = ["love","like","good","awesome","great"]
negative_words = ["hate","bad","ugly","worst"]

st = PorterStemmer()
positive_words = [st.stem(word) for word in positive_words]
negative_words = [st.stem(word) for word in negative_words]

def extract_all_features(data,vocab,par_vec):
  all_features = []
  counter = 0
  for d in data:
    class_features = []
    for tweet in d:
      tweet_features = []
      tweet_features.append(str(extract_no_of_words(tweet)))
      tweet_features.append(str(extract_no_of_first_person_pronouns(tweet)))
      tweet_features.append(str(extract_first_word_first_person_pronoun(tweet)))
      tweet_features.append(str(extract_no_of_verbs(tweet)))
      tweet_features.append(str(extract_no_of_exclamation_marks(tweet)))      
      tweet_features.append(str(extract_no_of_question_marks(tweet)))
      tweet_features.append(str(extract_no_of_past_tense_verbs(tweet)))
      tweet_features.append(str(extract_vocabulary_vector(tweet,vocab)))
      tweet_features.append(str(extract_no_of_words_in_list(tweet,positive_words)))
      tweet_features.append(str(extract_no_of_words_in_list(tweet,negative_words)))
      tweet_features.append(str(extract_no_of_whWords(tweet)))
      tweet_features.append(str(extract_URL(tweet)))
      tweet_features.append(str(extract_paragraph_vector(counter,par_vec)))
      counter += 1
      class_features.append(tweet_features)
    all_features.append(class_features)
    print all_features
  return all_features

def extract_no_of_words(token_tags):
  return len(token_tags)
  
def extract_no_of_first_person_pronouns(token_tags):
  return len([token_tag for token_tag in token_tags if re.match(r"PRP\$?", token_tag[1]) and token_tag[0] in ["I","i","my"]])

def extract_first_word_first_person_pronoun(token_tags):
  if token_tags[0][0].lower() in ["i","my"]:
    return 1
  return 0

def extract_no_of_verbs(token_tags):
  return len([token_tag for token_tag in token_tags if token_tag[1].startswith('VB')])
  
def extract_no_of_exclamation_marks(token_tags):
  return len([token_tag for token_tag in token_tags if token_tag[0].startswith("!")])

def extract_no_of_question_marks(token_tags):
  return len([token_tag for token_tag in token_tags if token_tag[0].startswith("?")])

def extract_no_of_past_tense_verbs(token_tags):
  return len([token_tag for token_tag in token_tags if token_tag[1]=="VBD"])

def extract_no_of_words_in_list(token_tags,l):
  return len([token_tag for token_tag in token_tags if token_tag[0] in l])

def extract_no_of_whWords(token_tags):
  return len([token_tag for token_tag in token_tags if re.search(r"^W((DT)|(P\$?)|(RB))$", token_tag[1])])

def extract_URL(token_tags):
  for token_tag in token_tags:
    if token_tag in ["www","http",".com"]:
      return 1
  return 0

def extract_vocabulary_vector(token_tags,vocab):
  vec = [0]*len(vocab)
  tokens = [token_tag[0] for token_tag in token_tags]
  for token in tokens:
    if token in vocab:
      vec[vocab.index(token)] +=1
  return ",".join([str(v) for v in vec])

def extract_paragraph_vector(counter,par_vec):
  return ",".join([str(p) for p in par_vec[counter]])