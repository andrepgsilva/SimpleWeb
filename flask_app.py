from flask import Flask, render_template
import simpleweb as sw

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", web=sw.web_env())

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
