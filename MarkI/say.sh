echo Reproduzindo Voz
pulseaudio --start --log-target=syslog
mpg123 speech.mp3
echo Voz Reproduzida com sucesso
