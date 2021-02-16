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
# say('Iniciando programa, por favor aguarde!', tts)

# Bibliotecas para processamento de linguagem natural
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

say()