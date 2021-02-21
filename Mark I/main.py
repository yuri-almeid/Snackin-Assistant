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

from playsound import playsound # Biblioteca para reprodução de arquivos MP3
from tinytag import TinyTag # Biblioteca para análise de .mp3
import time # Biblioteca de delay

from datetime import datetime # módulo de tempo
from datetime import date # Módulo de tempo (data)



# Awake
# Cria rodina que acorda > (pegar da API)
# pega o nome do cliente > (pegar da API) 
# Pega a hora exata > ()
# dá boas vindas ao cliente > 
# Falta pensar no resto > 

awake = True


'''
 elif cmd_type == 'asktime':
        now = datetime.now()
        result = 'It is ' + str(now.hour) + ' hours and ' + str(now.minute) + ' minutes.'
        
    # 2 Comando de data
    elif cmd_type == 'askdate':
        now = date.today()
        result = str(now.strftime("Today is %B, %d, it's a %A")) + '.'
'''

if awake	== True:

  hour = datetime.now()
  day = date.today()
  print(hour.day)

