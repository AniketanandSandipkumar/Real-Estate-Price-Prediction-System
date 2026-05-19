from prometheus_client import Counter


prediction_counter = Counter(
    "predictions_total",
    "Total number of predictions"
)
