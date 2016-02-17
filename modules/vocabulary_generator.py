def get_vocabulary(data):
  return list(set([token_tag[0] for d in data for tweet in d for token_tag in tweet]))
