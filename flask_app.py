from flask import Flask, render_template, redirect, url_for
import simpleweb as sw

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", web=sw.webstart())

def rodar(app):
    app.run(debug=True, use_reloader=True)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
