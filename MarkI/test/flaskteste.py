from flask import Flask
from flask import request, jsonify
from time import sleep


app = Flask(__name__)

@app.route('/api/echo-json', methods=['GET', 'POST', 'DELETE', 'PUT'])                                                                                                    
def add():                                                                                                                              
    data = request.get_json()
    # ... do your business logic, and return some response
    # e.g. below we're just echo-ing back the received JSON data
    print(data)
    print(data['nome'])
    
    return jsonify(data)
  
app.run(host='0.0.0.0', port= 8090)