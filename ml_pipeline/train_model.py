import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import mean_absolute_error, r2_score

from xgboost import XGBRegressor

from preprocessing import clean_data
from feature_engineering import create_features


def train_pipeline():

    df = pd.read_csv("data/raw/house_prices.csv")
    df.columns = df.columns.str.lower()
    df = clean_data(df)

    df = create_features(df)

    X = df.drop("price", axis=1)
    y = df["price"]

    categorical = ["location", "property_type"]

    numerical = [
        "area",
        "bedrooms",
        "bathrooms",
        "age",
        "price_per_sqft",
        "property_age_score",
        "luxury_score"
    ]

    preprocessor = ColumnTransformer([
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical
        ),
        (
            "num",
            StandardScaler(),
            numerical
        )
    ])

    pipeline = Pipeline([
        (
            "preprocessor",
            preprocessor
        ),
        (
            "model",
            XGBRegressor(
                n_estimators=300,
                max_depth=8,
                learning_rate=0.05,
                subsample=0.8,
                colsample_bytree=0.8,
                random_state=42
            )
        )
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    pipeline.fit(X_train, y_train)

    preds = pipeline.predict(X_test)

    mae = mean_absolute_error(y_test, preds)
    r2 = r2_score(y_test, preds)

    print("MAE:", mae)
    print("R2:", r2)

    joblib.dump(
        pipeline,
        "backend/models/production_model.pkl"
    )


if __name__ == "__main__":
    train_pipeline()
