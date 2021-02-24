
#-------------------------------------------------------------------------------
### IBM
# from ibm_watson import SpeechToTextV1
# from ibm_watson.websocket import RecognizeCallback, AudioSource 
# from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# apikey = 'Mwa1XzlAioFlzJqSBQKESOxvPqyKhcKg2sdIk46qM_nh'
# url = 'https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/885c5b99-82b6-4c58-bd8b-6a7c125db35f'

# # Setup Service
# authenticator = IAMAuthenticator(apikey)
# stt = SpeechToTextV1(authenticator=authenticator)
# stt.set_service_url(url)

# # Perform conversion
# with open('Untitled.mp3', 'rb') as f:
#     res = stt.recognize(audio=f, content_type='audio/mp3', model='pt-BR_BroadbandModel', continuous=True).get_result()


# with open('log.txt', 'w') as out:
#     out.writelines(res)


import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")