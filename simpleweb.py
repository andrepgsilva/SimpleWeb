from flaskapp import app

field_names = []
fn_and_operation = []
result_ready = None

def int_input(name_field):
    field_names.append(name_field)
    if len(fn_and_operation) < 1:
        fn_and_operation.append(int)


def float_input(name_field):
    field_names.append(name_field)
    if len(fn_and_operation) < 1:
        fn_and_operation.append(float)


def str_input(name_field):
    field_names.append(name_field)
    if len(fn_and_operation) < 1:
        fn_and_operation.append(str)


def web_env():
    return {"fields":field_names, "result_ready":result_ready}


def web_button(fn):
    fn_and_operation.insert(0, fn)


def web_run(application = app):
    application.run(debug=True)
