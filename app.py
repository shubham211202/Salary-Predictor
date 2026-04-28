from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
from src.logger import *
from src.predict import predict_salary
import os
port = int(os.getenv("PORT", 10000))
app.run(host="0.0.0.0", port=port)

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    logging.info("Home route accessed")
    return "API is running 🚀 CI/CD Working"


# ✅ Updated: Added GET + POST
@app.route("/predict", methods=["GET", "POST"])
def predict():

    # 🔹 GET method (for browser testing)
    if request.method == "GET":
        return {
            "message": "Use POST request with JSON: { experience: number }"
        }

    # 🔹 POST method (actual prediction)
    try:
        data = request.get_json()
        logging.info(f"Request data: {data}")

        if not data or "experience" not in data:
            logging.error("Missing experience field")
            return jsonify({"error": "Missing 'experience' field"}), 400

        exp = float(data["experience"])

        result = predict_salary(exp)

        return jsonify({
            "experience": exp,
            "predicted_salary": result
        })

    except ValueError as ve:
        logging.error(f"ValueError: {str(ve)}")
        return jsonify({"error": str(ve)}), 400

    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500


if __name__ == "__main__":
    # ❗ FIXED: port should be integer, not string
    app.run(host="0.0.0.0", port=10000, debug=True)