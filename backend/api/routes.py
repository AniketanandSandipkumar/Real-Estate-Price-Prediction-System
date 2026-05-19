from fastapi import APIRouter

from backend.api.schemas import PropertyInput
from backend.services.predictor import predict_price
from backend.services.logger import logger


router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "Real Estate Prediction API Running 🚀"
    }


@router.post("/predict")
def predict(data: PropertyInput):

    prediction = predict_price(data.dict())

    logger.info(f"Prediction generated: {prediction}")

    return {
        "predicted_price": prediction,
        "currency": "INR"
    }
