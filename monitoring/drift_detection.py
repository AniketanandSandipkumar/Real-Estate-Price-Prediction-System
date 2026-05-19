import pandas as pd


def detect_drift(current_df, reference_df):

    current_mean = current_df.mean()
    reference_mean = reference_df.mean()

    drift = abs(current_mean - reference_mean)

    return drift
