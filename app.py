from flask import Flask, request, session, jsonify, render_template, redirect, url_for
from datetime import timedelta
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import os
import json
from db import db

app = Flask(__name__)

app.secret_key = "corinthians"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=30)

db.init_app(app)
CORS(app)

from models import usuarios

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "GET":
        return render_template("cadastro.html")
    
    try:
        if request.method == "POST":
            data = request.get_json()

            if not data:
                return jsonify({"mensagem": "Erro ao carregar dados"})
            
            nomeCadastro = data.get("nomeCadastro")
            emailCadastro = data.get("emailCadastro")
            senhaCadastro = data.get("senhaCadastro")
            confirmarSenha = data.get("confirmarSenha")

            if not nomeCadastro or not emailCadastro or not senhaCadastro or not confirmarSenha:
                return jsonify({"mensagem": "Por favor, preencha todos os campos"}), 400
            
            if confirmarSenha != senhaCadastro:
                return jsonify({"mensagem": "As senhas não combinam"})
            
            user_exists = usuarios.query.filter_by(emailCadastro=emailCadastro).first()

            hashed_senha = generate_password_hash(senhaCadastro)
            
            if user_exists:
                return jsonify({"mensagem": "Usuário já existe"})
            
            new_user = usuarios(nomeCadastro=nomeCadastro, emailCadastro=emailCadastro, senhaCadastro=hashed_senha, confirmarSenha=hashed_senha)
            db.session.add(new_user)
            db.session.commit()

            return jsonify({"mensagem": "Usuário cadastro com sucesso"}), 200
    except Exception as e:
        print("Erro no backend", e)
        return jsonify({"mensagem": "Erro ao se conectar com o backend"}), 400
    
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.get_json()

        emailLogin = data.get("emailLogin")
        senhaLogin = data.get("senhaLogin")

        if not emailLogin or not senhaLogin:
            return jsonify({"mensagem": "Preencha todos os campos por favor"})
        
        user = usuarios.query.filter_by(emailCadastro=emailLogin).first()

        if user and check_password_hash(user.senhaCadastro, senhaLogin):
            session['emailLogin'] = emailLogin
            return jsonify({"sucesso": True, "mensagem": "Login feito com sucesso"}), 200
        else:
            return jsonify({"sucesso": False, "mensagem": "Email ou senha inválidos"}), 400
    return render_template("login.html")

@app.route("/index2", methods=["GET", "POST"])
def index2():
    return render_template("index2.html")

@app.route("/eventos", methods=["GET", "POST"])
def eventos():
    return render_template("eventos.html")

@app.route("/perfil", methods=["GET", "POST"])
def perfil():
    return render_template("perfil.html")

@app.route("/inscricao", methods=["GET", "POST"])
def inscricao():
    if request.method == "GET":
        return render_template("inscricao.html")
    
    try:
        if request.method == "POST":
            data = request.get_json()

            if not data:
                return jsonify({"mensagem": "Erro: erro ao carregar dados"})
            
            name = data.get("name")
            email = data.get("email")
            telefone = data.get("telefone")
            pcd = data.get("pcd")
            nopcd = data.get("nopcd")
            semgluten = data.get("semgluten")
            vegano = data.get("vegano")
            vegetariano = data.get("vegetariano")
            semlactose = data.get("semlactose")
            diabetico = data.get("diabetico")

            if not name or not email or not telefone:
                return jsonify({"mensagem": "Por favor, preencha todos os campos (nome, email e telefone)"}), 400
            
            else:
                session["name"] = name
                session["email"] = email
                session["telefone"] = telefone
                return jsonify({"mensagem": "Inscricao Feita com sucesso"}), 200
    except Exception as erro:
        print("Erro no servidor", erro)
        return jsonify({"mensagem": "Erro no backend"})   
    return render_template("inscricao.html")
            

@app.route("/minhasinscricoes", methods=["GET", "POST"])
def minhasinscricoes():

    try:
        name = session.get("name")
        email = session.get("email")
        telefone = session.get("telefone")
        return render_template("minhasinscricoes.html", name=name, email=email, telefone=telefone)
    except Exception as erro:
        print("Erro no backend", erro)
        return jsonify({"mensagem": "Erro no backend"})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)

