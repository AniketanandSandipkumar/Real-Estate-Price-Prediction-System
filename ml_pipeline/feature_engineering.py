import pandas as pd


def create_features(df):

    # Safe engineered features

    df["property_age_score"] = 100 - df["age"]

    df["luxury_score"] = (
        df["bedrooms"] * 2 +
        df["bathrooms"] * 2 +
        df["area"] / 1000
    )

    return df
