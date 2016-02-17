def write_arff(data,vocab,arff_file_name,par_vec_size):
  f = open(arff_file_name,'w')
  f.write("@relation twitter_sentiment_analysis\n\n")
  len_features = len(data[0][0])
  for i in range(len_features-2): # minus the vector and paragraph vector features
    f.write("@attribute f" + str(i+1) + " numeric\n")
  for i in range(len(vocab)):
    f.write("@attribute fv" + str(i+1) + " numeric\n")
  for i in range(par_vec_size):
    f.write("@attribute fpv" + str(i+1) + " numeric\n")
  f.write("@attribute class {pos,neg,ntr}\n\n")
  f.write("@data")
  class_labels = ["pos","neg","ntr"]
  for i in range(len(data)):
    for feature in data[i]:
      f.write("\n" + ",".join([feat for feat in feature]) + "," + class_labels[i])
  f.close()