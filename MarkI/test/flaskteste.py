from flask import Flask

app = Flask(__name__)

@app.route('/')
def ola():
    return '<h1>Olá Flask!</h1>'


@app.route('/<name>')
def abrir(name):
    return 'abriu ' + name

app.run()