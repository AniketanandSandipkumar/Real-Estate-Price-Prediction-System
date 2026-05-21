import joblib
import pandas as pd

from ml_pipeline.feature_engineering import create_features

model = joblib.load(
    "backend/models/production_model.pkl"
)

def predict_price(data):

    input_data = data.model_dump()

    df = pd.DataFrame([input_data])

    df = create_features(df)

    prediction = model.predict(df)[0]

    return round(float(prediction), 2)
