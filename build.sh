#!/bin/bash

buildCorpus() {
  echo "Building corpus from data.JSON"
  python3 buildCorpus.py
}

cutCorpus(){
  #39497 
  tail -n $1 corpus.txt > ./fastText-0.1.0/MTG.valid
  echo "Created validation set size $1"

  head -n $((39497 - $1)) corpus.txt > ./fastText-0.1.0/MTG.train
  echo "Created test set"
}

echo "$1 Got"
buildCorpus
cutCorpus $1

#./fastText-0.1.0/fasttext test model_MTG.bin MTG.valid
#./fastText-0.1.0/fasttext predict model_MTG.bin - 5

