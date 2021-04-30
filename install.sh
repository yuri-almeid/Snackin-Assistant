echo baixando git -------------------------------------
git clone https://github.com/yuri-almeid/Snackin-Assistant.git

echo instalando player  -------------------------------------
sudo apt install mpg123

echo Subistuindo arquivo default  -------------------------------------
sudo mv /var/codigo/app/controllers/default.py /var/codigo/app/controllers/default_old.py 
sudo cp Snackin-Assistant/default.py /var/codigo/app/controllers/
sudo chmod 777 /var/codigo/app/controllers/default.py

echo Copiando os arquivos .sh -------------------------------------
sudo cp Snackin-Assistant/say.sh /var/codigo/
sudo cp Snackin-Assistant/say_test.sh /var/codigo/
sudo chmod 777 /var/codigo/say_test.sh
sudo chmod 777 /var/codigo/say.sh

echo Copiando audio teste -------------------------------------
sudo cp Snackin-Assistant/say.sh /var/codigo/

echo Instalando Dependencias -------------------------------------
pip3 install ibm_watson
sudo pip3 install ibm_watson