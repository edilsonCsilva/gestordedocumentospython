from unicodedata import name
from flask import Flask,render_template
from core.Base.ContentValues import ContentValues


app = Flask(__name__)




contentValues =ContentValues()
contentValues.put("title","Meu Gestor de Documentos Simples")
contentValues.put("N","GEstor de Documentos Simples")
contentValues.put("F","GEstor de Documentos Simples")





@app.route("/")
def home():
     data=contentValues.getAll()
    
     contentValues.put("dia","Domingo dia 23/10/2022 -SP")

     return  render_template('views/index.html',**locals())





@app.route("/teste")
def meuteste():
    return "<h1>Isso  é um Teste:)</h1>"


if __name__ == '__main__':
     app.run(debug=True) 
