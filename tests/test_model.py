import joblib
import pandas as pd


model = joblib.load(
    "backend/models/production_model.pkl"
)


def test_prediction():

    sample = pd.DataFrame([
        {
            "area": 1500,
            "bedrooms": 3,
            "bathrooms": 2,
            "age": 5,
            "location": "Mumbai",
            "property_type": "Apartment"
        }
    ])

    pred = model.predict(sample)

    assert pred[0] > 0
