from db import db

class usuarios(db.Model):

    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nomeCadastro = db.Column(db.String(100), nullable=False, unique=True)
    emailCadastro = db.Column(db.String(100), nullable=False)
    senhaCadastro = db.Column(db.String(100), nullable=False)
    confirmarSenha = db.Column(db.String(100), nullable=False)
    token = db.Column(db.String(200))
    