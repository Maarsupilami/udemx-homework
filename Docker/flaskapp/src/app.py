from flask import Flask, render_template, jsonify
from utils.network import fetch_details

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/status")
def status():
    return jsonify(
        status="running"
    )

@app.route("/host")
def host():
    host_name, ip = fetch_details()
    return render_template("host.html", hostname=host_name, ip=ip)

@app.route("/details")
def details():
    host_name, ip = fetch_details()
    return jsonify(
        host_name=f'{host_name}',
        ip=f'{ip}'
    )


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000
        )