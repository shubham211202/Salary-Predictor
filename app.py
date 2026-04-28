import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from src.predict import predict_salary

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "Salary Prediction API is running"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Validate input
        if not isinstance(data, dict) or "experience" not in data:
            return jsonify({"error": "Missing 'experience' field"}), 400

        # Convert input
        exp = float(data["experience"])

        # Predict
        result = predict_salary(exp)

        return jsonify({
            "experience": exp,
            "predicted_salary": float(result)
        })

    except ValueError:
        return jsonify({"error": "Experience must be a number"}), 400
    except Exception as e:
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)