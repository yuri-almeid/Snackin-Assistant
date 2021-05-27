
## Importando Módulos
from ibm_watson import TextToSpeechV1 # Biblioteca IBM Watson para TTS
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator # Biblioteca IBM Watson para autenticação da API
from datetime import datetime # módulo de tempo
from datetime import date # Módulo de tempo (data)
import random
import os


def IBM_auth():
  print(" >>> Iniciando autenticação do IBM Watson...")
  print()

  ## Configurando chave da API IBM Watson
  # Chave da API
  apikey = 'wu9NYkYxx6jzVQrvrdRK3rCQk5et-VDTSpApnG9dDG2e'
  url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/7583b6cf-bd90-4057-ac04-54fc91ed5c0e'
  print(" >>> Chave: " + apikey )
  # Autenticação da chave
  try:
    authenticator = IAMAuthenticator(apikey)
    tts = TextToSpeechV1(authenticator=authenticator)
    tts.set_service_url(url)

    return tts

  except :
      print(">> Ocorreu um erro na autenticação")
      exit()
  
## TTS
# Funçao que reproduz texto falado
def say(text, tts):
    # Sintetiza voz a partir do texto desejado
    with open('speech.mp3', 'wb') as audio_file:
      res = tts.synthesize(text, accept='audio/mp3', voice='pt-BR_IsabelaV3Voice').get_result()
      audio_file.write(res.content)
    
    # toca mp3 pelo sistema linux
    os.system('./say.sh')  
    
    
    
def KIN(user_):
    # Banco de respostas prontas
    c_greeting = ['como vai?', 'como tem passado?', 'que bom te ver aqui!', 'fico feliz em te ver aqui',
                    'desejo boas compras!', 'te desejo uma boa experiência Snackin']
    c_weekend = ['Aproveite o seu final de semana!',
            'desejamos um excelente final de semana!']
    
    tts = IBM_auth()
    # Cria objeto do log
    log = {'nome': '',
            'data': {'data': '',
                            'hora': '',
                            'dia': ''}}
    
    
    # user = request.args.get('name')
    # from kin import *
    # kin(request.args.get('name'))
    user = str(user_)
    user = user.replace("{","")
    user = user.replace("}","")
    user = user.replace("'","")
    
    # Pega o nome e localização do cliente
    name = user_
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
    
    return True
    
    