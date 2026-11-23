from flask import Flask, render_template, request

# Module de connexion à la base de données (sqlite locale pour le projet)
import sqlite3

app = Flask(__name__)

# chemin de la base de données
DATABASE = './static/movies.sqlite'

# Page d'accueil
@app.route('/')
def index():
  return render_template('index.html')



@app.route('/movies')
def movies():
  return '<h1> Bravo ! la réponse est 42 ! </h1>'

if __name__ == "__main()__":
    app.run()