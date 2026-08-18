from api import criar_app


app = criar_app()


if __name__ == "__main__":

    app.run(
        debug=True
    )