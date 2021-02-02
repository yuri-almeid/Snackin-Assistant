#!/usr/bin/python
# -*- coding: UTF-8 -*-

print("\n >>> Software Iniciando...")

# Libraries needed for NLP
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

# Libraries needed for Tensorflow processing
import tensorflow as tf
import numpy as np
import tflearn
import random
import json

print("\n >>> Software Iniciado.")

# import our chat-bot intents file
with open('intents_pt.json') as json_data:
    intents = json.load(json_data)

print(intents)