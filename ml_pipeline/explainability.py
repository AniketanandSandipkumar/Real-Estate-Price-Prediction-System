import shap
import joblib
import pandas as pd
import matplotlib.pyplot as plt


model = joblib.load(
    "backend/models/production_model.pkl"
)

sample = pd.read_csv("data/raw/house_prices.csv")

X = sample.drop("price", axis=1)

explainer = shap.Explainer(model.named_steps["model"])

shap_values = explainer(
    model.named_steps["preprocessor"].transform(X)
)

shap.summary_plot(shap_values)

plt.savefig("screenshots/shap_summary.png")
