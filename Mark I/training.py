#!/usr/bin/python
# -*- coding: UTF-8 -*-

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

print("\n >>> Carregando intents.json")
# Pega todos os intents cadastrados
with open('intents.json') as json_data:
    intents = json.load(json_data)

# Lista com intents
print(" >>> Lista com intents:")
print(intents)
print("\n\n")

words = []
classes = []
documents = []
ignore = ['?']


print(" >>> Iniciando tokenização de palavras")
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

# remove classes duplicadas
classes = sorted(list(set(classes)))

print (len(documents), "documents")
print (len(classes), "classes", classes)
print (len(words), "unique stemmed words", words)


# Cria dados de treinamento
training = []
output = []
# Cria array vazio para saida
output_empty = [0] * len(classes)

# Cria o training set, conjunto de palavras para cada sentença
for doc in documents:
    # Inializa conjunto
    bag = []
    # Lista de palavras tokenizadas do pattern
    pattern_words = doc[0]
    # Pega a origem de cada palavra
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
    # Cria o conjunto
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    # saída é 1 para tag atual e 0 para outras tags
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

# Embaralhando características e criando array
random.shuffle(training)
training = np.array(training)

# Listas de treinamento
train_x = list(training[:,0])
train_y = list(training[:,1])

# Resetando graficos (tem b.o. aqui ainda)
#tf.reset_default_graph()

# Criação da rede neural
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 10)
net = tflearn.fully_connected(net, 10)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)

# Definindo modelo da rede e Tensorboard
model = tflearn.DNN(net, tensorboard_dir='./brain/tflearn_logs')

# Inicia o treinamento
model.fit(train_x, train_y, n_epoch=1000, batch_size=8, show_metric=True)
model.save('./brain/model.tflearn')

import pickle
pickle.dump( {'words':words, 'classes':classes, 'train_x':train_x, 'train_y':train_y}, open( "./brain/training_data", "wb" ) )


#