from unicodedata import name
from flask import Flask,render_template

app = Flask(__name__)





@app.route("/")
def home():
     data=[]
  
     return "<h1>Ola Mundo..!</h1>"





@app.route("/teste")
def meuteste():
    return "<h1>Isso  é um Teste:)</h1>"


if __name__ == '__main__':
     app.run(debug=True) 
