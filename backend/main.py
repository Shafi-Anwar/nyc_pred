from fastapi import FastAPI
from schema import TaxiInput
import numpy as np
import pandas as pd
import joblib

app = FastAPI()

# Load model
model = joblib.load("../models/taxi_model.pkl")

# Load training columns
model_columns = joblib.load(
    "../models/model_columns.pkl"
)


def haversine(lat1, lon1, lat2, lon2):

    R = 6371

    lat1, lon1, lat2, lon2 = map(
        np.radians,
        [lat1, lon1, lat2, lon2]
    )

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        np.sin(dlat / 2) ** 2
        + np.cos(lat1)
        * np.cos(lat2)
        * np.sin(dlon / 2) ** 2
    )

    c = 2 * np.arcsin(np.sqrt(a))

    return R * c


@app.get("/")
def home():
    return {
        "message": "NYC Taxi Duration Prediction API"
    }


@app.post("/predict")
def predict(data: TaxiInput):

    input_dict = data.dict()
    distance = haversine(
    input_dict["pickup_latitude"],
    input_dict["pickup_longitude"],
    input_dict["dropoff_latitude"],
    input_dict["dropoff_longitude"]
    )
    input_dict["distance_km"] = distance
    df = pd.DataFrame([input_dict]) 
    # Encode categorical
    df = pd.get_dummies(df)

    # Match training columns
    df = df.reindex(
        columns=model_columns,
        fill_value=0
    )

    prediction = model.predict(df)

    return {
        "predicted_duration_seconds":
        float(prediction[0])
    }