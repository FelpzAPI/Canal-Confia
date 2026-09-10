import os

from flask import Flask
from flask_cors import CORS

from api.database import db
from api.config import Config


def criar_app():

    BASE_DIR = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )

    app = Flask(

        __name__,

        template_folder=os.path.join(
            BASE_DIR,
            "templates"
        ),

        static_folder=os.path.join(
            BASE_DIR,
            "static"
        )

    )

    # =====================================
    # CONFIGURAÇÕES
    # =====================================

    app.config.from_object(Config)

    CORS(app)

    # =====================================
    # BANCO DE DADOS
    # =====================================

    db.init_app(app)

    from api.model import Usuario, Denuncia

    # =====================================
    # CRIA TABELAS
    # =====================================

    with app.app_context():

        db.create_all()
    # =====================================
    # IMPORTS DAS ROTAS
    # =====================================

    from api.routes.admin import admin
    from api.routes.denuncias import denuncias
    from api.routes.dashboard import dashboard
    from api.routes.login import login
    from api.routes.pages import pages

    # =====================================
    # REGISTRO DOS BLUEPRINTS
    # =====================================

    app.register_blueprint(admin)
    app.register_blueprint(denuncias)
    app.register_blueprint(dashboard)
    app.register_blueprint(login)
    app.register_blueprint(pages)

    return app