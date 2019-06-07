from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/<path:path>')
def static_proxy(path):
    # Serve everything in the 'static' folder
    return app.send_static_file(path)


if __name__ == "__main__":
    app.run(debug=True)
