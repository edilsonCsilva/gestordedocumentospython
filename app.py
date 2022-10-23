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






@app.route("/cadastro")
def cadastro():
     data=contentValues.getAll() 
     return render_template('views/register.html',**locals())



@app.route("/painel")
def painel():
     data=contentValues.getAll() 

     return render_template('views/painel.html',**locals())




@app.route("/viewdoc")
def viewdoc():
     data=contentValues.getAll() 

     return render_template('views/viewdocs.html',**locals())



@app.route("/add")
def add():
     data=contentValues.getAll() 

     return render_template('views/add.html',**locals())






if __name__ == '__main__':
     app.run(debug=True) 
