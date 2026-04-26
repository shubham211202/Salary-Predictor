import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

# Get current directory (backend/)
BASE_DIR = os.path.dirname(__file__)

# Build model path
MODEL_PATH = os.path.join(BASE_DIR, "salary_model.pkl")

# Load model
model = joblib.load(MODEL_PATH)

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://www.technoxyz.shop"}})

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
        prediction = model.predict([[exp]])

        return jsonify({
            "experience": exp,
            "predicted_salary": float(prediction[0])
        })

    except ValueError:
        return jsonify({"error": "Experience must be a number"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)