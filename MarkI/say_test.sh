echo Reproduzindo Voz Teste
pulseaudio --start --log-target=syslog
mpg123 speech_test.mp3
echo Voz Reproduzida com sucesso
