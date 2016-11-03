from flaskapp import app

fields_and_values = []
botao = None
result_ready = None

def web_input(name_field):
    fields_and_values.append(name_field)
    return True if len(fields_and_values) > 0 else False


def web_env():
    return {"fields":fields_and_values, "result_ready":result_ready}#A lógica do result_ready precisa mudar


def web_button(fn):
    global botao
    botao = fn


def web_run(application = app):
    application.run(debug=True)
