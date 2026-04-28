import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "../models", "salary_model.pkl")
MODEL_PATH = os.path.abspath(MODEL_PATH)

model = joblib.load(MODEL_PATH)

def predict_salary(exp: float) -> float:
    """
    Predict salary based on years or experience

    Args:
         exp(float): Years of experience
    
    Return:
        float: Predicted Salary
    """

    if exp < 0:
        raise ValueError("Experience can't be negative")
    
    prediction = model.predict([[exp]])

    return float(prediction[0])


