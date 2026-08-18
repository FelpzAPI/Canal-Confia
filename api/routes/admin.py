import re

from flask import Blueprint, request, jsonify

from werkzeug.security import generate_password_hash

from api.database import db
from api.model import Usuario


admin = Blueprint(
    "admin",
    __name__
)


# =====================================
# CADASTRAR ADMINISTRADOR
# =====================================

@admin.route(
    "/api/admin",
    methods=["POST"]
)
def cadastrar_admin():

    dados = request.get_json()

    if not dados:

        return jsonify({

            "erro": "JSON inválido."

        }), 400


    nome = dados.get("nome")

    email = dados.get("email")

    senha = dados.get("senha")


    if not nome or not email or not senha:

        return jsonify({

            "erro": "Todos os campos são obrigatórios."

        }), 400


    # =====================================
    # VALIDAÇÃO DA SENHA
    # =====================================

    senha_forte = re.compile(
    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$"
)

    if not senha_forte.match(senha):

        return jsonify({

        "erro": (
            "A senha deve possuir no mínimo 8 caracteres, "
            "uma letra maiúscula, uma letra minúscula, "
            "um número e um caractere especial."
        )

    }), 400


    existe = Usuario.query.filter_by(
        email=email
    ).first()


    if existe:

        return jsonify({

            "erro": "Já existe um administrador com esse e-mail."

        }), 409


    usuario = Usuario(

        nome=nome,

        email=email,

        senha=generate_password_hash(senha),

        tipo="admin"

    )


    db.session.add(usuario)

    db.session.commit()


    return jsonify({

        "mensagem": "Administrador cadastrado com sucesso."

    }), 201


# =====================================
# LISTAR ADMINISTRADORES
# =====================================

@admin.route(
    "/api/admin",
    methods=["GET"]
)
def listar_admins():

    usuarios = Usuario.query.all()

    return jsonify([

        usuario.to_dict()

        for usuario in usuarios

    ])


# =====================================
# EXCLUIR ADMINISTRADOR
# =====================================

@admin.route(
    "/api/admin/<int:id>",
    methods=["DELETE"]
)
def excluir_admin(id):

    usuario = Usuario.query.get_or_404(id)

    db.session.delete(usuario)

    db.session.commit()

    return jsonify({

        "mensagem": "Administrador removido."

    })