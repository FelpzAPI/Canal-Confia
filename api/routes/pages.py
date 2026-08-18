from flask import Blueprint, render_template

pages = Blueprint(
    "pages",
    __name__
)


@pages.route("/")
def index():
    return render_template("index.html")


@pages.route("/login")
def login():
    return render_template("login.html")


@pages.route("/nova-denuncia")
def nova_denuncia():
    return render_template("nova_denuncia.html")


@pages.route("/acompanhar")
def acompanhar():
    return render_template("acompanhar.html")


@pages.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@pages.route("/admin")
def admin():
    return render_template("admin.html")


@pages.route("/protocolo")
def protocolo():
    return render_template("protocolo.html")


@pages.route("/detalhes_denuncia")
@pages.route("/detalhes-denuncia")
def detalhes_denuncia():
    return render_template("detalhes_denuncia.html")