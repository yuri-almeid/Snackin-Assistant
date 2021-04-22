#!/usr/bin/python
#
#
#   Snackin' Assistant Mark I
#   Author: Yuri L. Almeida
#
from datetime import datetime # módulo de tempo
from datetime import date # Módulo de tempo (data)
import requests # Módulo para webrequest
import random # Módulo Random
import json # Modulo para lidar com arquivos JSON

from fastapi import FastAPI # Módulo para o FASTAPI
import uvicorn # Modulo para rodar o fastapi
from pydantic import BaseModel # Criação de base de dados

from IBM_interface import * # Interface da IBM para sintetizar voz
tts = IBM_auth() # Realiza autenticação e cria o objeto TTS

# from playsound import playsound # Biblioteca para reprodução de arquivos MP3
# from tinytag import TinyTag # Biblioteca para análise de .mp3


# Cria aplicação da API
app = FastAPI()

# Classe para modelo de requisição
class User(BaseModel):
  name: str
  location: str

# Banco de respostas prontas
c_greeting = ['como vai?', 'como tem passado?', 'que bom te ver aqui!', 'fico feliz em te ver aqui',
                'desejo boas compras!', 'te desejo uma boa experiência Snackin']
c_weekend = ['Aproveite o seu final de semana!',
          'desejamos um excelente final de semana!']


@app.post("/")
def welcome(user: User):

  # Cria objeto do log
  log = {'nome': '',
          'condominio': '',
          'data': {'data': '',
                           'hora': '',
                           'dia': ''}}
  
  # Pega o nome e localização do cliente
  name = user.name
  log['nome'] = name
  loc = user.location
  log['condominio'] = loc

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


  # Escolha a saudação correta para o horário
  if int(now.hour) >= 4 and int(now.hour) < 12:
    greating = 'Bom dia,'
  elif int(now.hour) >= 12 and int(now.hour) < 19:
    greating = 'Boa tarde,'
  else:
    greating = 'Boa noite,'


  # Concatena a saudação com o nome do cliente e um complemento inicial
  msg = greating + spc + name + ',' + spc + random.choice(c_greeting)

  # Mensagem extra para final de semana (sextou)
  if day == 'Friday' or day == 'Saturday':
    msg = msg + ', ' + random.choice(c_weekend)

  log['Mensagem'] = msg
  # Colocar json response
  print(log)
  
  # sudo apt-get install sox
  # sudo apt-get install sox libsox-fmt-all
  say(msg, tts)
  
  
  
  return log


# Rota Get Id
@app.get("/User/{user_id}")
def get_user_by_id(user_id: int):
  return {"Status": 404, "Message": "User not found"}

# Rota Presentation
@app.get("/presentation")
def presentation():
  
  say('Olá pessoal, eu sou a Kin, sou a nova assistente dos mercados isnéquin!', tts)
  say('É um grande prazer conhece-los!', tts)
  
  
  return True


# RODA COM: uvicorn main:app --reload

