import subprocess
import paragraph_vectors_reader
import collections
import nltk
from nltk import word_tokenize

def get_paragraph_vectors(data,par_vec_size):
  dataIdsFilePath = "./modules/paragraph2vec/data-ids.txt"
  f = open(dataIdsFilePath,'w')
  counter = 0
  for d in data:
    for tweet in d:
      f.write("_*" + str(counter) + " " + " ".join(word_tokenize(tweet)) + "\n")
      counter += 1
  f.close()
  subprocess.call(["./modules/paragraph2vec/go.sh " + str(par_vec_size)],shell=True)
  paragraph_vectors_dict = paragraph_vectors_reader.read_paragraph_vectors("./modules/paragraph2vec/word2vec/paragraph_vectors.txt")
  sorted_paragraph_vectors = collections.OrderedDict(sorted(paragraph_vectors_dict.items()))
  vectors = [sorted_paragraph_vectors[postId] for postId in sorted_paragraph_vectors]
  return vectors
