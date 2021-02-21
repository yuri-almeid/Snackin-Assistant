# -*- coding: UTF-8 -*-
#
#   Snackin' Assistant Mark I
#   Author: Yuri L. Almeida
#

### Módulos e Bibliotecas ######################################################
# Módulos de sitentização de voz
from IBM_interface import * 
#tts = IBM_auth() # Faz autenticação com a IBM

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
import random



# Awake
# Cria rodina que acorda > (pegar da API)
# pega o nome do cliente > (pegar da API) 
# Pega a hora exata > (ok)
# dá boas vindas ao cliente > 
# Falta pensar no resto > (working on it)

awake = True

if awake	== True:

  # Pega o nome do cliente
  name = 'Yuri Almeida'

  spc = ' '

  # Pega a hora exata
  now = datetime.now()
  day = datetime.today().strftime('%A')

  # Cria frase
  if int(now.hour) >= 4 and int(now.hour) < 12:
    greating = 'Bom dia'
  elif int(now.hour) >= 12 and int(now.hour) < 19:
    greating = 'Boa tarde'
  else:
    greating = 'Boa noite'
  
  phrase = greating + spc + name

  c1 = ['como vai?', 'como tem passado?', 'que bom te ver aqui!', 'fico feliz em te ver aqui',
                'desejo boas compras!', 'te desejo uma boa experiência Snackin']
  c_wdn = ['que tal uma bebida gelada para aproveitar o seu final de semana?',
          'desejamos um excelente final de semana!']
  c_sdy = ['']

  phrase = phrase + spc + random.choice(c1)

  if day == 'Friday' or day == 'Saturday':
    phrase = phrase + ', ' + random.choice(c_wdn)

  print(phrase)

  

  












