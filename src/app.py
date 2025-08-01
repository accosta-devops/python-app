from flask import Flask, jsonify
import datetime, socket

app = Flask(__name__)

@app.route("/api/v1/details")

def details():
    return jsonify({
        'time': datetime.datetime.now().strftime("%d/%m/%Y"),
        'hostname': socket.gethostname() 
    })

@app.route("/api/v1/healthz")

def health():
    return jsonify({
        'status': 'up'
    }), 200


if __name__=='__main__':

    app.run(host="0.0.0.0")

