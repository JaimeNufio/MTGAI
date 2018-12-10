#!/bin/bash

buildCorpus() {
  echo "Building corpus from data.JSON"
  python3 buildCorpus.py
}

cutCorpus(){
  #39497 
  tail -n $1 corpus.txt > ./fastText-0.1.0/MTG.valid
  echo "Created validation set size $1"

  headS=$(expr 18013 - $1)
  echo "Head Size: $headS"
  head -n $headS corpus.txt > ./fastText-0.1.0/MTG.train
  echo "Created test set"
}

echo "$1 Got"
buildCorpus
cutCorpus $1
./fastText-0.1.0/fasttext supervised -input ./fastText-0.1.0/MTG.train -output ./fastText-0.1.0/model_MTG -epoch 75 -lr .55 -wordNgrams 2

