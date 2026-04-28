from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
from src.logger import *
from src.predict import predict_salary

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    logging.info("Home route accessed")
    return "API is running"

@app.route("/predict", methods=["POST"])
def predict():
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
    app.run(host="0.0.0.0", port="10000", debug=True)