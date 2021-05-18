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
        if request.method=="GET":
                juego=request.form.get("juego")
                return render_template("juegos.html", juego=juego)
        else:
                return render_template("listajuegos.html")

@app.route('/listajuegos')
def pagina_lista_juegos():
        return render_template("listajuegos.html")

app.run(debug=True)