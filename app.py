from flask import Flask, request, session, jsonify, render_template, redirect, url_for
from datetime import timedelta
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import os
import smtplib
from email.message import EmailMessage
import json
from db import db
from itsdangerous import URLSafeTimedSerializer

app = Flask(__name__)
serializer = URLSafeTimedSerializer("corinthians")

app.secret_key = "corinthians"
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')

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

@app.route("/enviar_email", methods=["POST"])
def enviar_email():
    data = request.get_json()
    email = data.get("email")

    msg = EmailMessage()
    msg['Subject'] = "Email de instruções de inscrição"
    msg['From'] = "grumelo098@gmail.com"
    msg['To'] = email
    msg.add_alternative(f"""
    <!DOCTYPE html>
<html>
  <body>
    <h2>📩 Bem-vindo à inscrição!</h2>
    <p>✅ Seu processo de inscrição está finalizado.</p>
    <p>Você perceberá que na sua inscrição conterá com 4 digitos, esse é o seu código de acesso no dia do evento</p>
    <hr>
    <p>💬 Não responda este email. Em caso de dúvidas, entre em contato.</p>
  </body>
</html>
""", subtype='html')
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login("grumelo098@gmail.com", 'ourf sgnz wkiw sxse')
            smtp.send_message(msg)
            print("Email enviado com sucesso")
            return jsonify({"mensagem": "Email enviado com sucesso!"}), 200
    except Exception as e:
        print(f"Erro ao enviar email: {e}")
        return jsonify({"erro": "Erro ao enviar email"}), 500

@app.route("/esqueci_senha", methods=["GET", "POST"])
def esqueci_senha():
    if request.method == "POST":
        data = request.get_json()

        email = data.get("email")

        if not email:
            return jsonify({"mensagem": "Email é obrigatório"})
        
        user = usuarios.query.filter_by(emailCadastro=email).first()

        if user:
            token = serializer.dumps(email, salt="senha-reset")
            user.token = token
            db.session.commit()

            link = url_for("redefinir_senha", token=token, _external=True)

            msg = EmailMessage()
            msg['Subject'] = "Redefinição de Senha"
            msg['From'] = "grumelo098@gmail.com"
            msg['To'] = email
            msg.set_content(f"Acesse o link para redefinir sua senha {link}")

            try:
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login("grumelo098@gmail.com", 'ourf sgnz wkiw sxse')
                    smtp.send_message(msg)
                return jsonify({"mensagem": "Link de redefinição enviado para o seu email"}), 200
            except Exception as e:
                print("Erro ao enviar email", e)
                return jsonify({"mensagem": "Erro ao enviar email"}), 500
        else:
            return jsonify({"mensagem": "Email não encontrado"}), 404
    return render_template("esqueceuasenha.html")

@app.route("/redefinir_senha/<token>", methods=["GET", "POST"])
def redefinir_senha(token):
    try:
        email = serializer.loads(token, salt="senha-reset", max_age=3600)
    except:
        return jsonify({"mensagem": "Link inválido ou expirado"}), 400
    
    user = usuarios.query.filter_by(emailCadastro=email).first()

    if request.method == "POST":
        data = request.get_json()
        novaSenha = data.get("novaSenha")

        if not novaSenha:
            return jsonify({"mensagem": "Nova Senha Obrigatório"}), 400
        
        hashed = generate_password_hash(novaSenha)
        user.senhaCadastro = hashed
        user.confirmarSenha = hashed
        user.token = None
        db.session.commit()


        return jsonify({"mensagem": "Senha redefinida com sucesso"}), 200
    
    return render_template("redefinir_senha.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)

