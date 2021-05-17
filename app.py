from flask import Flask, render_template, abort
import json

app = Flask(__name__)

with open("MSX.json") as fichero:
        doc = json.load(fichero)

@app.route('/')
def pagina_principal():
    return render_template("paginaprincipal.html",documento=doc)

@app.route('/juegos')
def pagina_juegos():
        return render_template("juegos.html")

@app.route('/listajuegos')
def pagina_lista_juegos():
        return render_template("listajuegos.html")

app.run(debug=True)