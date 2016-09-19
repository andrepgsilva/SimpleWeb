from flaskapp import app

fields = []
fields_values = []
form = False
result_ready = False


def web_input(name_field):
    fields.append(name_field)
    form = True if len(fields) > 1 else False
    return form


def web_env(fields=fields, form=form):
    return {"fields":fields, "form":form, "result_ready":result_ready, "web_print":web_print()}


def web_print(fields_values=fields_values):
    result = 0
    for i in fields_values:
        result += int(i)
    return result


def web_run(application = app):
    application.run()
