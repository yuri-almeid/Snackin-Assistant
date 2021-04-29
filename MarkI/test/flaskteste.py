from flask import Flask
from flask import request
from time import sleep


app = Flask(__name__)
  
@app.route('/postjson', methods = ['POST'])
def postJsonHandler():
    
    print('Teste - ')
    sleep(1)
    print('printado:')
    
    print (request.is_json)
    content = request.get_json()
    print (content)
    return 'JSON posted'
  
app.run(host='0.0.0.0', port= 8090)