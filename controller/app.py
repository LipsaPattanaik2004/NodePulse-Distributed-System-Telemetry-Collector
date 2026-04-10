from flask import Flask, request, jsonify
from processor import process_data

app = Flask(__name__)

data_store = []

@app.route("/ingest", methods=["POST"])
def ingest():
    data = request.json
    processed = process_data(data)
    data_store.append(processed)
    return jsonify({"status": "received", "data": processed})

@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(data_store)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
