import logging
from src.logger import *   # ensures logger is initialized
import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "salary_model.pkl")
MODEL_PATH = os.path.abspath(MODEL_PATH)

model = joblib.load(MODEL_PATH)

def predict_salary(exp: float) -> float:
    logging.info(f"Received input: {exp}")

    if exp < 0:
        logging.error("Negative experience received")
        raise ValueError("Experience cannot be negative")

    prediction = model.predict([[exp]])

    logging.info(f"Prediction: {prediction[0]}")

    return float(prediction[0])