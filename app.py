import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "status": "ok",
        "message": "Dummy server Flask aktif 🚀",
        "version": "1.0"
    })

@app.route("/predict", methods=["POST"])
def predict():
    print("📩 Dummy route /predict dipanggil.")
    return jsonify({
        "status": "success",
        "detections": [
            {
                "jenis_sampah": "cardboard",
                "confidence": 0.95,
                "bounding_box (xyxy)": [10, 10, 100, 100]
            }
        ]
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
