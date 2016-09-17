from flaskapp import app

fields = []
form = False

def web_input(name_field):
    fields.append(name_field)
    form = True if len(fields) > 1 else False
    return form


def web_env():
    return {"fields":fields, "form":form}


def web_run(application = app):
    application.run()
