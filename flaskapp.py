from flask import Flask, render_template, url_for, request, redirect
import simpleweb as sw

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", web=sw.web_env())

@app.route("/", methods=["GET", "POST"])
def catch_data():
    if request.method == "POST":
        for value in request.form:
            sw.fields_values.append(request.form[value])
        if len(sw.fields_values) != 0:
            sw.result_ready = True
    return redirect(url_for("index"))
