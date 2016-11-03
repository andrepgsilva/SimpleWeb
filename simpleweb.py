from flaskapp import app

field_names = []
fn_and_operation = []
result_ready = None

def web_input(name_field):
    field_names.append(name_field)


def web_env():
    return {"fields":field_names, "result_ready":result_ready}


def web_button(fn, operation=str):
    fn_and_operation.append(fn)
    fn_and_operation.append(operation)


def web_run(application = app):
    application.run(debug=True)
