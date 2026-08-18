from werkzeug.security import generate_password_hash

from api.database import db
from api.model import Usuario


# =====================================
# CRIA GERENTE PADRÃO
# =====================================

def criar_gerente_padrao():

    gerente = Usuario.query.filter_by(
        email="gerenterh@lobios.com"
    ).first()

    if not gerente:

        gerente = Usuario(

            nome="Gerente RH",

            email="gerenterh@lobios.com",

            senha=generate_password_hash("123456"),

            tipo="gerente"

        )

        db.session.add(gerente)

        db.session.commit()

        print("Gerente padrão criado com sucesso.")

    else:

        print("Gerente padrão já existe.")