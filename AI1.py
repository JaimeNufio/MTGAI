import nltk
from nltk.stem.lancaster import LancasterStemmer
import os
import json
import datetime
stemmer = LancasterStemmer()


def populate():
    global dataSet;
    f = open("corpus.txt",'r');
    for card in f:
        temp = card.split("|");
        #The idea here would be to add more options
        dataSet.append({"Color":temp[3],"Text":temp[4]});
    #poulate the dataSet by reading corpus
    pass;

dataSet = [];
#dataSet.append({"Color":"ColorIdentity","OracleText":"OracleText"});

populate();
#print(dataSet);
#organize data struct for documents, classes, and words
wordList = []
colors = []
documentList = []
ignore = ["{","}"]

#We have to loop thru sentences of data
for card in dataSet:
    words = nltk.word_tokenize(card['Text'].decode('utf-8'));
    #print (word);
    #Extend instead of append, nice function
    wordList.extend(words);
    
    #document of corpus... not sure why
    documentList.append((words, card['Color']));
    #print(documentList);

    #Currently support only monocolored creatures
    #TODO: Hardcode color identities?
    if card['Color'] not in colors:
        colors.append(card['Color']);

wordList = [stemmer.stem(words.lower()) for words in wordList if words not in ignore];
#Remove dupes, is this necesary?
colors = list(set(colors)); 
print("Created DocumentList")

##### Creating Training Data  ######

trainSet = []
outputSet = []

outputEmpty = [0]*len(colors)
cnt=0
for item in documentList:
    #bag of words approach
    bag = []
    #list of word-tokens from the items(cards);
    patternWords = item[0];

    #stem each word
    patternWords = [stemmer.stem(word.lower()) for word in patternWords];

    #create bag of word array
    for word in wordList:
        bag.append(1) if word in patternWords else bag.append(0);

    trainSet.append(bag);
    
    outRow=list(outputEmpty);
    outRow[colors.index(item[1])] = 1;
    outputSet.append(outRow);
    cnt=cnt+1
    print(cnt);


i = 0
wordCurr = documents[i][0];
print([stemmer.stem(word.lower()) for word in wordCurr]);
print (trainSet[i]);
print (outputSet[i]);


