import os
from urllib.parse import quote_plus

from dotenv import load_dotenv

load_dotenv()


class Config:

    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")
    MYSQL_DATABASE = os.getenv(
        "MYSQL_DATABASE",
        "canal_anonimo_sos"
    )

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://"
        f"{MYSQL_USER}:"
        f"{quote_plus(MYSQL_PASSWORD)}@"
        f"{MYSQL_HOST}:"
        f"{MYSQL_PORT}/"
        f"{MYSQL_DATABASE}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False