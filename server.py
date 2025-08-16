from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="static")

@app.route("/")
def home():
    return send_from_directory("static", "membresia_app.html")

@app.route("/<path:path>")
def static_proxy(path):
    return send_from_directory("static", path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
