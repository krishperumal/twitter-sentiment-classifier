cd ./modules/paragraph2vec/word2vec
cp ../word2vec.c .
gcc word2vec.c -o word2vec -lm -pthread -O3 -march=native -funroll-loops
./word2vec -train ../data-ids.txt -output vectors.txt -cbow 1 -size $1 -window 5 -negative 5 -hs 0 -sample 1e-4 -threads 10 -binary 0 -iter 100 -min-count 1 -sentence-vectors 1
grep '_\*' vectors.txt > paragraph_vectors.txt
