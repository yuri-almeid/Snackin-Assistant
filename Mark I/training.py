#!/usr/bin/python
# -*- coding: UTF-8 -*-

#encoding: utf-8


# Para baixar os pacotes necessários para lingua portuguesa do nltk
# import nltk
# nltk.download()

# Recomendo que você faça o download dos seguintes pacotes:
# - averaged_perceptron_tagger
# - floresta
# - mac_morpho
# - machado
# - punkt
# - stopwords
# - wordnet
# - words


# Bibliotecas para processamento de linguagem natural
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

# Bibliotecas do tensorflow
import tensorflow as tf
import numpy as np
import tflearn
import random
import json

print("\n\n")
# Pega todos os intents cadastrados
with open('intents.json') as json_data:
    intents = json.load(json_data)

# Lista com intents
print("Lista com intents:")
print(intents)
print("\n\n")

words = []
classes = []
documents = []
ignore = ['?']

# Loop pelo patterns do json intents
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # Toqueniza cada palavra da sentença
        w = nltk.word_tokenize(pattern, language='portuguese')
        # Adiciona a palavra a lista de palavras
        words.extend(w)
        # Adiciona words ao documento
        documents.append((w, intent['tag']))
        # Adiciona a tag à lista de classes
        if intent['tag'] not in classes:
            classes.append(intent['tag'])


# Pega origem das palavras da forma minúscula
words = [stemmer.stem(w.lower()) for w in words if w not in ignore]
words = sorted(list(set(words)))

# remove classe duplicadas
classes = sorted(list(set(classes)))

print (len(documents), "documents")
print (len(classes), "classes", classes)
print (len(words), "unique stemmed words", words)


# teste