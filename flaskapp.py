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
        for value in request.form:
            values.append(request.form[value])
        sw.result_ready = sw.botao(*values)
    return redirect(url_for("index"))
