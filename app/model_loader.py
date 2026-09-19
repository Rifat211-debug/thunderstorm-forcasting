import joblib
from app.config import MODEL_PATH

def load_model():
    with open(MODEL_PATH, "rb") as file:
        model = joblib.load(file)
    return model

model = load_model()    