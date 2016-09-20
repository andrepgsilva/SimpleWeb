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
            sw.fields_and_values[value] = int(request.form[value])
    return redirect(url_for("index"))
