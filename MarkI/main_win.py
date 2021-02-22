# -*- coding: UTF-8 -*-
#
#   Snackin' Assistant Mark I
#   Author: Yuri L. Almeida
#
from datetime import datetime # módulo de tempo
from datetime import date # Módulo de tempo (data)
import requests
import flask
import random
import json



# Awake
# Cria rodina que acorda > (pegar da API)
# Pega o nome do cliente > (pegar da API) 
# Pega a hora exata > (ok)
# Dá boas vindas ao cliente > (ok)
# Criar log > (ok)
# Separar Rotinas (chegada, permanência, saída) > (ok)
# Rotina: Chegada > (ok)
# Rotina: Permanência > ()
# Rotina: Saída > ()
# Pensar no resto > (working on it)

# Variável que define se de fato deve acordar ou não
awake = True



# Se deve realizar seguinte rotina
if awake	== True:

  # Cria objeto do log
  log = {'nome': '',
          'data': {'data': '',
                           'hora': '',
                           'dia': ''}}

  # Pega o nome do cliente
  name = 'Yuri Almeida'
  log['nome'] = name

  spc = ' ' # apenas uma variável facilitatória

  # Pega a hora exata
  now = datetime.now()
  day = datetime.today().strftime('%A')
  # Inicia contagem de tempo de permanência na loja
  timer_start = now.minute
  # Salva data
  log['data']['data'] = str(now.day) + '/' + str(now.month) + '/' + str(now.year)
  # Salva hora
  log['data']['hora'] = str(now.hour) + ':' + str(now.minute)
  # Salva dia da semana
  log['data']['dia'] = day

  c1 = ['como vai?', 'como tem passado?', 'que bom te ver aqui!', 'fico feliz em te ver aqui',
                'desejo boas compras!', 'te desejo uma boa experiência Snackin']
  c_wdn = ['que tal uma bebida gelada para aproveitar o seu final de semana?',
          'desejamos um excelente final de semana!']

  # Escolha a saudação correta para o horário
  if int(now.hour) >= 4 and int(now.hour) < 12:
    greating = 'Bom dia,'
  elif int(now.hour) >= 12 and int(now.hour) < 19:
    greating = 'Boa tarde,'
  else:
    greating = 'Boa noite,'
  
  # Concatena a saudação com o nome do cliente e um complemento inicial
  phrase = greating + spc + name + spc + random.choice(c1)

  # Mensagem extra para final de semana (sextou)
  if day == 'Friday' or day == 'Saturday':
    phrase = phrase + ', ' + random.choice(c_wdn)



  log['Mensagem'] = phrase


  print(log)
  print(phrase)




  












