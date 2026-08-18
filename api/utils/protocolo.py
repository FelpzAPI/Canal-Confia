from datetime import datetime
import random
import string

from api.model import Denuncia


def gerar_protocolo():

    ano = datetime.now().year

    while True:

        codigo = "".join(

            random.choices(

                string.ascii_uppercase + string.digits,

                k=6

            )

        )

        protocolo = f"SOS-{ano}-{codigo}"

        existe = Denuncia.query.filter_by(
            protocolo=protocolo
        ).first()

        if not existe:

            return protocolo