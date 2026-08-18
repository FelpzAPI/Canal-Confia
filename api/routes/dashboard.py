from flask import Blueprint, jsonify

from api.model import Denuncia


dashboard = Blueprint(
    "dashboard",
    __name__
)


# =====================================
# DASHBOARD
# =====================================

@dashboard.route(
    "/api/dashboard",
    methods=["GET"]
)
def mostrar_dashboard():

    return jsonify({

        "total": Denuncia.query.count(),


        "recebidas": Denuncia.query.filter_by(
            status="Recebida"
        ).count(),


        "analise": Denuncia.query.filter_by(
            status="Em análise"
        ).count(),


        "concluidas": Denuncia.query.filter_by(
            status="Concluída"
        ).count()

    })