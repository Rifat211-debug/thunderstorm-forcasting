from fastapi import FastAPI
from app.schemas import Weather_Input
from app.predictor import predict_thunder

app = FastAPI(title = "Thunderstorm Predictor API")

@app.get("/")
def home():
    return {"message" : "Thunderstorm Predictor API is running!"}

@app.post("/predict")
def get_prediction(data : Weather_Input):
    features = data.to_list()
    result = predict_thunder(features)

    return result