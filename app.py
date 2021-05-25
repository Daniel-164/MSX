from flask import Flask, render_template, abort, request
import json

app = Flask(__name__)


@app.route('/',methods=["GET"])
def pagina_principal():
    return render_template("paginaprincipal.html")

@app.route('/juegos',methods=["GET","POST"])
def pagina_juegos():
        return render_template("juegos.html")

@app.route('/listajuegos',methods=["POST"])
def pagina_lista_juegos():
        with open("MSX.json") as fichero:
                doc = json.load(fichero)
        caracteres=request.form.get("juego")
        lista=[]
        if len(caracteres)==0:
                lista=doc
        else:
                for juego in doc:
                        if str(juego.get("nombre")).startswith(caracteres):
                                lista.append(juego)
        return render_template("listajuegos.html", juego_a_buscar=caracteres, juegosmsx=lista)

@app.route('/juego/<identificador>')
def pagina_juego(identificador):
        if identificador in identificador:
                return render_template("juego.html")

app.run(debug=True)