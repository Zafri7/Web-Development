
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'  

@app.route('/<name>')
def hello_name(name):
    return f'Yo, {name}!'

if __name__ == '__main__':
    app.run(port=5000, debug=True)









