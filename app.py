from flask import Flask, request, session, jsonify, render_template
from datetime import timedelta
from flask_cors import CORS
from werkzeug.security import generate_password_hash
import os
import json
from db import db

app = Flask(__name__)

app.secret_key = "corinthians"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=30)

from models import User

@app.route("/index", methods=["GET", "POST"])
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
            
            user_exists = User.query.filter_by(emailCadastro=emailCadastro).first()

            hashed_senha = generate_password_hash(senhaCadastro, confirmarSenha)
            
            if user_exists:
                return jsonify({"mensagem": "Usuário já existe"})
            
            new_user = User(nomeCadastro=nomeCadastro, emailCadastro=emailCadastro, hashed_senha=senhaCadastro, hashed_senha=confirmarSenha)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({"mensagem": "Usuário cadastro com sucesso"}), 200
    except Exception as e:
        print("Erro no backend", e)
        return jsonify({"mensagem": "Erro ao se conectar com o backend"}), 400
    
