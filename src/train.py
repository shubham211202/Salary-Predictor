import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import joblib

def train_model():
    df = pd.read_csv("C:/Users/Shubham Kumar/Documents/Salary-Predict/data/Salary_Data.csv")
    df = df.dropna(subset="Salary")
    
    X = df[["Years of Experience"]]
    y = df["Salary"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)

    print(f"Model MAE: {mae}")

    joblib.dump(model, "models/salary_model.pkl")
    print("Model trained and saved.")

if __name__=="__main__":
    train_model()



