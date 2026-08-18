import os

from flask import (
    Blueprint,
    request,
    jsonify,
    send_from_directory
)

from werkzeug.utils import secure_filename

from api.database import db
from datetime import datetime
from api.model import Denuncia

from api.utils.protocolo import gerar_protocolo



denuncias = Blueprint(
    "denuncias",
    __name__
)



UPLOAD_FOLDER = "uploads"


os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)



# =====================================
# DEFINIR PRAZO DE RESPOSTA
# =====================================

def definir_prazo(prioridade):

    if prioridade == "Alta":
        return "24 horas"

    elif prioridade == "Média":
        return "3 dias úteis"

    elif prioridade == "Baixa":
        return "7 dias úteis"

    return "Não definido"





# =====================================
# CADASTRAR OCORRÊNCIA
# =====================================

@denuncias.route(
    "/denuncias",
    methods=["POST"]
)
def criar_denuncia():


    categoria = request.form.get("categoria")

    descricao = request.form.get("descricao")

    data_ocorrido = request.form.get("data_ocorrido")



    if not categoria:

        return jsonify({

            "erro": "Categoria é obrigatória."

        }), 400



    if not descricao:

        return jsonify({

            "erro": "Descrição é obrigatória."

        }), 400




    # ===============================
    # VALIDA DATA FUTURA
    # ===============================

    if data_ocorrido:

        try:

            data_informada = datetime.strptime(
                data_ocorrido,
                "%Y-%m-%d"
            )


            if data_informada > datetime.now():

                return jsonify({

                    "erro":
                    "A data do ocorrido não pode ser futura."

                }),400


        except ValueError:

            return jsonify({

                "erro":
                "Data inválida."

            }),400





    nome_arquivo = None



    arquivo = request.files.get("anexo")



    if arquivo and arquivo.filename != "":


        nome_arquivo = secure_filename(
            arquivo.filename
        )


        caminho = os.path.join(

            UPLOAD_FOLDER,

            nome_arquivo

        )


        arquivo.save(caminho)





    prioridade = request.form.get("prioridade")

    if prioridade not in ["Alta", "Média", "Baixa"]:

        prioridade = "Média"



    denuncia = Denuncia(

        protocolo=gerar_protocolo(),

        categoria=categoria,

        setor=request.form.get("setor"),

        local=request.form.get("local"),

        data_ocorrido=data_ocorrido,

        descricao=descricao,

        anexo=nome_arquivo,

        status="Recebida",

        prioridade=prioridade,

        prazo_resposta=definir_prazo(prioridade)

    )



    db.session.add(denuncia)

    db.session.commit()



    return jsonify({

        "mensagem":
        "Ocorrência registrada com sucesso.",

        "id":
        denuncia.id,

        "protocolo":
        denuncia.protocolo

    }),201





# =====================================
# LISTAR OCORRÊNCIAS
# =====================================

@denuncias.route(
    "/denuncias",
    methods=["GET"]
)
def listar_denuncias():


    lista = Denuncia.query.order_by(

        Denuncia.id.desc()

    ).all()



    return jsonify([

        denuncia.to_dict()

        for denuncia in lista

    ])






# =====================================
# BUSCAR POR ID
# =====================================

@denuncias.route(
    "/denuncias/<int:id>",
    methods=["GET"]
)
def buscar_denuncia(id):


    denuncia = Denuncia.query.get_or_404(id)


    return jsonify(

        denuncia.to_dict()

    )







# =====================================
# CONSULTAR PELO PROTOCOLO
# =====================================

@denuncias.route(
    "/protocolo/<codigo>",
    methods=["GET"]
)
def consultar_protocolo(codigo):


    denuncia = Denuncia.query.filter_by(

        protocolo=codigo

    ).first()



    if not denuncia:

        return jsonify({

            "erro":
            "Protocolo não encontrado."

        }),404




    return jsonify({

        "protocolo":
        denuncia.protocolo,


        "categoria":
        denuncia.categoria,


        "status":
        denuncia.status,


        "prioridade":
        denuncia.prioridade,


        "prazo_resposta":
        denuncia.prazo_resposta,


        "observacao_rh":
        denuncia.observacao_rh,



        "ultima_atualizacao":

            denuncia.data_criacao.strftime(
                "%d/%m/%Y %H:%M"
            )

    })







# =====================================
# ATUALIZAR OCORRÊNCIA
# =====================================

@denuncias.route(
    "/denuncias/<int:id>",
    methods=["PUT"]
)
def atualizar_denuncia(id):


    denuncia = Denuncia.query.get_or_404(id)



    dados = request.get_json()



    if not dados:

        return jsonify({

            "erro":
            "JSON inválido."

        }),400





    if "status" in dados:


        denuncia.status = dados["status"]



        if denuncia.status == "Concluída":

            denuncia.observacao_rh = (

                denuncia.observacao_rh +

                "\n\nOcorrência concluída. "
                "O prazo inicial de resposta era "
                + denuncia.prazo_resposta

            )







    if "prioridade" in dados:


        denuncia.prioridade = dados["prioridade"]


        denuncia.prazo_resposta = definir_prazo(

            dados["prioridade"]

        )







    if "observacao_rh" in dados:


        denuncia.observacao_rh = dados["observacao_rh"]






    db.session.commit()



    return jsonify({

        "mensagem":
        "Ocorrência atualizada com sucesso.",


        "denuncia":
        denuncia.to_dict()

    })








# =====================================
# VISUALIZAR ANEXO
# =====================================

@denuncias.route(
    "/uploads/<filename>",
    methods=["GET"]
)
def visualizar_anexo(filename):


    return send_from_directory(

        UPLOAD_FOLDER,

        filename

    )