from datetime import datetime

from api.database import db
from api.utils.data import formatar_data



# ============================
# USUÁRIOS (ADMINISTRADORES RH)
# ============================

class Usuario(db.Model):

    __tablename__ = "usuarios"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    nome = db.Column(
        db.String(100),
        nullable=False
    )


    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )


    senha = db.Column(
        db.String(255),
        nullable=False
    )


    ativo = db.Column(
        db.Boolean,
        default=True
    )


    data_criacao = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    tipo = db.Column(
        db.String(20),
        default="admin"
    )



    def to_dict(self):

        return {

            "id": self.id,

            "nome": self.nome,

            "email": self.email,

            "ativo": self.ativo,

            "tipo": self.tipo,

            "data_criacao":
                formatar_data(self.data_criacao)

        }





# ============================
# OCORRÊNCIAS
# ============================

class Denuncia(db.Model):

    __tablename__ = "denuncias"



    id = db.Column(
        db.Integer,
        primary_key=True
    )



    protocolo = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )



    categoria = db.Column(
        db.String(100),
        nullable=False
    )



    setor = db.Column(
        db.String(100)
    )



    local = db.Column(
        db.String(100)
    )



    data_ocorrido = db.Column(
        db.String(20)
    )



    descricao = db.Column(
        db.Text,
        nullable=False
    )



    anexo = db.Column(
        db.String(255)
    )



    status = db.Column(
        db.String(30),
        default="Recebida"
    )



    prioridade = db.Column(
        db.String(30),
        default="Média"
    )



    # ============================
    # PRAZO DE RESPOSTA
    # ============================

    prazo_resposta = db.Column(
        db.String(50),
        default="Não definido"
    )



    observacao_rh = db.Column(
        db.Text,
        default=""
    )



    data_criacao = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )





    def to_dict(self):

        return {

            "id": self.id,

            "protocolo": self.protocolo,

            "categoria": self.categoria,

            "setor": self.setor,

            "local": self.local,

            "data_ocorrido": self.data_ocorrido,

            "descricao": self.descricao,

            "anexo": self.anexo,

            "status": self.status,

            "prioridade": self.prioridade,

            "prazo_resposta": self.prazo_resposta,

            "observacao_rh": self.observacao_rh,

            "data_criacao":
                formatar_data(self.data_criacao)

        }