import joblib
import pandas as pd

from ml_pipeline.feature_engineering import create_features


model = joblib.load(
    "backend/models/production_model.pkl"
)


def predict_price(data):

    df = pd.DataFrame([data])

    df = create_features(df)

    prediction = model.predict(df)[0]

    return round(prediction, 2)
