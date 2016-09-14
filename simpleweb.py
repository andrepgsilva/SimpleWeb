from flask_app import app

campos = []
form = False

def web_input(nome_campo):
    campos.append(nome_campo)
    form = True if len(campos) > 1 else False
    return form


def web_env():
    return {"campos":campos, "form":form}

def web_run(application = app):
    application.run()
