from flaskapp import app

fields_and_types = []
result_ready = None

def int_input(name_field):
    fields_and_types.append([name_field, int])


def float_input(name_field):
    fields_and_types.append([name_field, float])


def str_input(name_field):
    fields_and_types.append([name_field, str])


def web_env():
    fields_names = []
    for i in range(len(fields_and_types)):
        if i == len(fields_and_types)-1:
            break
        fields_names.append(fields_and_types[i][0])
    return {"fields":fields_names, "result_ready":result_ready}


def web_button(fn):
    fields_and_types.append(fn)


def web_run(application = app):
    application.run(debug=True)
