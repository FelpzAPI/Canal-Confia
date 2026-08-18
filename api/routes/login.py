from flask import Blueprint, request, jsonify, render_template

from api.model import Usuario

from werkzeug.security import check_password_hash


login = Blueprint(
    "login",
    __name__
)


# ==============================
# TELA DE LOGIN
# ==============================

@login.route("/login", methods=["GET"])
def pagina_login():

    return render_template(
        "login.html"
    )



# ==============================
# PROCESSAR LOGIN
# ==============================

@login.route("/login", methods=["POST"])
def fazer_login():

    dados = request.get_json()


    if not dados:

        return jsonify({

            "erro": "JSON inválido."

        }),400



    email = dados.get("email")

    senha = dados.get("senha")



    usuario = Usuario.query.filter_by(
        email=email
    ).first()



    if not usuario:

        return jsonify({

            "sucesso":False,

            "mensagem":"Usuário não encontrado."

        }),404



    if not check_password_hash(
        usuario.senha,
        senha
    ):

        return jsonify({

            "sucesso":False,

            "mensagem":"Senha incorreta."

        }),401



    return jsonify({

        "sucesso":True,

        "id":usuario.id,

        "usuario":usuario.nome,

        "email":usuario.email,

        "tipo":usuario.tipo

    })