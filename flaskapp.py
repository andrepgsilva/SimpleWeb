from flask import Flask, render_template, url_for, request, redirect
import simpleweb as sw

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", web=sw.web_env())

@app.route("/", methods=["POST"])
def catch_data():
    if request.method == "POST":
        values = []
        for fields in sw.field_names:
            if sw.fn_and_operation[1] == int:
                values.append(int(request.form[fields]))
            elif sw.fn_and_operation[1] == float:
                values.append(float(request.form[fields]))
            else:
                values.append(request.form[fields])
        sw.result_ready = sw.fn_and_operation[0](*values)
    return redirect(url_for("index"))
