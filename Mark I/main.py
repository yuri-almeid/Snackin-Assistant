#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
#   Snackin' Assistant Mark I
#   Author: Yuri L. Almeida
#


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

