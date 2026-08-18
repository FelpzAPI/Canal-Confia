from datetime import timedelta


def formatar_data(data):

    if not data:
        return None


    data_brasilia = data - timedelta(hours=3)


    return data_brasilia.strftime(
        "%d/%m/%Y %H:%M"
    )