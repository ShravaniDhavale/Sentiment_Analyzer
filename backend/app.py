from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)

analyzer = pipeline("sentiment-analysis")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data.get("text", "")
    result = analyzer(text)[0]
    return jsonify({
        "label": result["label"],
        "score": result["score"]
    })

if __name__ == "__main__":
    app.run(debug=True)
