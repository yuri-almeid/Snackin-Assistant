#!/usr/bin/python
# -*- coding: UTF-8 -*-

#
#   Snackin' Assistant Mark I
#   Author: Yuri L. Almeida
#

'''----------------------------------------------------------------------------'''
## Importando Módulos
from ibm_watson import TextToSpeechV1 # Biblioteca IBM Watson para TTS
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator # Biblioteca IBM Watson para autenticação da API
from playsound import playsound # Biblioteca para reprodução de arquivos MP3
from tinytag import TinyTag # Biblioteca para análise de .mp3
import time # Biblioteca de delay



'''----------------------------------------------------------------------------'''
## Configurando chave da API IBM Watson
# Chave da API
apikey = 'wu9NYkYxx6jzVQrvrdRK3rCQk5et-VDTSpApnG9dDG2e'
url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/7583b6cf-bd90-4057-ac04-54fc91ed5c0e'
# Autenticação da chave
authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)


'''----------------------------------------------------------------------------'''
## TTS
# Funçao que reproduz texto falado
def synt(text, name):
    # Sintetiza voz a partir do texto desejado
    path = './mp3_db/' + name
    with open(path, 'wb') as audio_file:
      res = tts.synthesize(text, accept='audio/mp3', voice='pt-BR_IsabelaV3Voice').get_result()
      audio_file.write(res.content)
    # analiza o arquivo mp3 gerado
    tag = TinyTag.get(path)
    # Reproduz a voz sintetizada
    playsound(path)    
    # Aguarda fim da fala
    time.sleep(tag.duration)
    


'''----------------------------------------------------------------------------'''
## Main

synt('Snéquim', 'snackin')