from modules import reader
from modules import preprocessor
from modules import vocabulary_generator
from modules import paragraph_vectors
from modules import feature_extractor
from modules import arff_writer

par_vec_size = 25

def main():
  train_data = reader.read_data(["./datasets/dataset_pos.txt","./datasets/dataset_neg.txt","./datasets/dataset_ntr.txt"])
  par_vec_train = paragraph_vectors.get_paragraph_vectors(train_data,par_vec_size)
  train_data = preprocessor.preprocess(train_data)
  vocab = vocabulary_generator.get_vocabulary(train_data)
  train_features = feature_extractor.extract_all_features(train_data,vocab,par_vec_train)
  arff_writer.write_arff(train_features,vocab,"sentiment_analysis_train.arff",par_vec_size)
  test_data = reader.read_data(["./datasets/dataset_test_pos.txt","./datasets/dataset_test_neg.txt","./datasets/dataset_test_ntr.txt"])
  par_vec_test = paragraph_vectors.get_paragraph_vectors(test_data,par_vec_size)
  test_data = preprocessor.preprocess(test_data)
  test_features = feature_extractor.extract_all_features(test_data,vocab,par_vec_test)
  arff_writer.write_arff(test_features,vocab,"sentiment_analysis_test.arff",par_vec_size)

if __name__=='__main__':
  main()