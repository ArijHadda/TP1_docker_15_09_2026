from flask import Flask
from pymongo import MongoClient #sertà etablir une connexion vers un serveur MongoDB

app = Flask(__name__)
connection = MongoClient("mongodb://mongo:27017/") #C'est Docker Compose qui va faire en sorte que ce nom soit "traduisible" en adresse réseau vers le bon conteneur
try:
    connection.admin.command("ping") #On teste la connexion
    print("Connexion à MongoDB réussie !")
except Exception as e:
    print("Erreur lors de la connexion à MongoDB : ",e)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

