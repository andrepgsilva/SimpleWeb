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
        for i in range(len(sw.fields_and_types)):
            if i == len(sw.fields_and_types)-1:
                break
            name_field = sw.fields_and_types[i][0]
            type_field = sw.fields_and_types[i][1]
            if type_field == int:
                values.append(int(request.form[name_field]))
            elif type_field == float:
                values.append(float(request.form[name_field]))
            else:
                values.append(request.form[name_field])
        sw.result_ready = sw.fields_and_types[len(sw.fields_and_types)-1](*values)
    return redirect(url_for("index"))
