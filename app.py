from flask import Flask, render_template, abort
import json

app = Flask(__name__)

with open("MSX.json") as fichero:
        doc = json.load(fichero)

@app.route('/')
def pagina_principal():
    return render_template("paginaprincipal.html",documento=doc)

app.run(debug=True)