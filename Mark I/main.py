#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
#   Snackin' Assistant Mark I
#   Author: Yuri L. Almeida
#

### Módulos e Bibliotecas ######################################################
# Módulos de sitentização de voz
from IBM_interface import * 
tts = IBM_auth()

# Aviso inicial
say('Iniciando programa, por favor aguarde!', tts)

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

import pickle

### Define a rede neural e carrega treinamento #################################
# Transforma o conjunto de bytes em uma hierarquia de objetos
data = pickle.load( open( "./brain/training_data", "rb" ) )
words = data['words']
classes = data['classes']
train_x = data['train_x']
train_y = data['train_y']

with open('./brain/intents.json') as json_data:
    intents = json.load(json_data)


# Recria a rede
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 10)
net = tflearn.fully_connected(net, 10)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)

# Redefine o modelo
model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')

# Carrega o modelo salvo
model.load('./brain/model.tflearn')


### Thinking processing ########################################################

def clean_up_sentence(sentence):
    # Tokeniza as sentenças
    sentence_words = nltk.word_tokenize(sentence, language='portuguese')
    # Simplifica palavras
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# returning bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=False):
    # Tokeniza as sentenças
    sentence_words = clean_up_sentence(sentence)
    # Cria conjunto de palavras
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)

    return(np.array(bag))

context = {}
ERROR_THRESHOLD = 0.25
def classify(sentence):
    # Gera as probalidades para o modelo
    results = model.predict([bow(sentence, words)])[0]
    # Filtra a saida
    results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD]
    # Organiza pela força da probabilidade da resposta correta
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
    # Retorna a tupla com o intent e a probabilidade 
    return return_list

def response(sentence, userID='123', show_details=False):
    results = classify(sentence)
    # if we have a classification then find the matching intent tag
    if results:
        # loop as long as there are matches to process
        while results:
            for i in intents['intents']:
                # find a tag matching the first result
                if i['tag'] == results[0][0]:
                    # set context for this intent if necessary
                    if 'context_set' in i:
                        if show_details: print ('context:', i['context_set'])
                        context[userID] = i['context_set']

                    # check if this intent is contextual and applies to this user's conversation
                    if not 'context_filter' in i or \
                        (userID in context and 'context_filter' in i and i['context_filter'] == context[userID]):
                        if show_details: print ('tag:', i['tag'])
                        # a random response from the intent
                        return print(random.choice(i['responses']))

            results.pop(0)


while True:
  question = input("Você: ")
  answer = response(question, show_details=True)
  #print("Super Smart AI from Snackin': " + answer)
  say(answer)