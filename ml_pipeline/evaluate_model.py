import pandas as pd
import joblib

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


def evaluate_model():

    model = joblib.load(
        "backend/models/production_model.pkl"
    )

    df = pd.read_csv("data/raw/house_prices.csv")

    X = df.drop("price", axis=1)
    y = df["price"]

    preds = model.predict(X)

    mae = mean_absolute_error(y, preds)
    mse = mean_squared_error(y, preds)
    r2 = r2_score(y, preds)

    print("MAE:", mae)
    print("MSE:", mse)
    print("R2 Score:", r2)


if __name__ == "__main__":
    evaluate_model()
