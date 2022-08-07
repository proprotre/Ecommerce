from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cad/usuario/caduser", methods=["POST"])
def caduser():
    return request.form

@app.route("/cad/usuario/")
def usuario():
    return render_template("usuario.html", titulo="Cadastro de Usuário")

@app.route("/cad/anuncio/")
def anuncio():
    return render_template("anuncio.html", titulo="Cadastro de Anúncio")

@app.route("/anunc/pergunta/")
def pergunta():
    return render_template("pergunta.html")

@app.route("/anunc/compra/")
def compra():
    return "<h1 style='text-align: center ;'>Seja Bem Vindo!</h1> <a style='text-align: center ;' href='../../'>Página Inicial</a>"

@app.route("/anunc/favoritos/")
def favoritos():
    return "<h1 style='text-align: center ;'>Seja Bem Vindo!</h1> <a style='text-align: center ;' href='../../'>Página Inicial</a>"

@app.route("/config/categoria/")
def categoria():
    return render_template("categoria.html")

@app.route("/rel/vendas")
def relVendas():
    return render_template("relVendas.html")

@app.route("/rel/compras")
def relCompras():
    return render_template("relCompras.html")


