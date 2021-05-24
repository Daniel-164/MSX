from flask import Flask, render_template, abort, request
import json

app = Flask(__name__)

with open("MSX.json") as fichero:
        doc = json.load(fichero)

@app.route('/',methods=["GET"])
def pagina_principal():
    return render_template("paginaprincipal.html",documento=doc)

@app.route('/juegos',methods=["GET","POST"])
def pagina_juegos():
        juego=request.form.get("juego")
        return render_template("juegos.html", juego=juego)

@app.route('/listajuegos',methods=["POST"])
def pagina_lista_juegos():
        return render_template("listajuegos.html")

@app.route('/juego/<identificador>')
def pagina_juego(identificador):
        if identificador in identificador:
                return render_template("juego.html")
app.run(debug=True)