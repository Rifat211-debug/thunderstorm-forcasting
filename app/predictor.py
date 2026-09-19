import pandas as pd
from  app.model_loader import model

FEATURES_COLUMNS = [
    "SWEAT index",  
    "K index",
    "Totals totals index",
    "Environmental_Stability",
    "Moisture_Indices",
    "Convective_Potential",
    "Temperature_Pressure",
    "Moisture_Temperature_Profiles"
]


def predict_thunder(features : list):
    df = pd.DataFrame(data = [features], columns = FEATURES_COLUMNS)

    prediction = model.predict(df)
    prediction_probability = model.predict_proba(df)[:,1] if hasattr(model, 'predict_proba') else None

    return {
        "prediction" : int(prediction[0]),
        "prediction_probability" : float(prediction_probability[0]) if prediction_probability is not None else None
    }

