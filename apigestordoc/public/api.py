from unicodedata import name
from flask import Flask
from flask_cors import CORS
from  recursoA.OlaClient import OlaClient 

 


app = Flask(__name__)
CORS(app)


@app.route("/")
def init():
    return "<h3>Api OK </h3>"  


@app.route("/recurso-a")
def recursoA():
    olaClient=OlaClient()
    return  olaClient.ola()







if __name__ == '__main__':
     app.run(debug=True,port=5080) 
