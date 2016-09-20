from flaskapp import app
from collections import OrderedDict

fields_and_values = OrderedDict()


def web_input(name_field, fields_values=fields_and_values):
    fields_values[name_field] = None
    return True if len(fields_and_values) > 0 else False


def web_env(fields=fields_and_values):
    result_ready = False if None in fields.values() else True
    return {"fields":fields, "result_ready":result_ready}
    # return {"fields":fields, "form":form, "result_ready":result_ready, "web_print":web_print()}


# def web_print(fields_values=fields_and_values):
#     return sum(fields_and_values.values())


def web_run(application = app):
    application.run(debug=True)
