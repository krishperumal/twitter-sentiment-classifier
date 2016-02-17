import sys
import numpy

def read_paragraph_vectors(path):
  f = open(path,'r')
  paragraph_vectors_dict = dict()
  for line in f:
    index = line.find(' ')
    postId = int(line[2:index])
    vector_values = line[index+1:]
    vector = []
    for vector_value in vector_values.split(' '):
      if len(vector_value) > 1:
        vector.append(numpy.double(vector_value))
    paragraph_vectors_dict[postId] = vector
  return paragraph_vectors_dict
