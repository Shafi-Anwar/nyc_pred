import streamlit as st
import requests

st.title("🚕 NYC Taxi Duration Predictor")

vendor_id = st.selectbox(
    "Vendor ID",
    [1, 2]
)

passenger_count = st.slider(
    "Passenger Count",
    1,
    6,
    1
)

pickup_longitude = st.number_input(
    "Pickup Longitude",
    value=-73.982155
)

pickup_latitude = st.number_input(
    "Pickup Latitude",
    value=40.767937
)

dropoff_longitude = st.number_input(
    "Dropoff Longitude",
    value=-73.964630
)

dropoff_latitude = st.number_input(
    "Dropoff Latitude",
    value=40.765602
)

pickup_hour = st.slider(
    "Pickup Hour",
    0,
    23,
    17
)

pickup_day = st.slider(
    "Pickup Day",
    1,
    31,
    14
)

pickup_weekday = st.slider(
    "Pickup Weekday",
    0,
    6,
    0
)

pickup_month = st.slider(
    "Pickup Month",
    1,
    12,
    3
)

store_and_fwd_flag = st.selectbox(
    "Store and Forward Flag",
    ["N", "Y"]
)

if st.button("Predict Duration"):

    data = {
        "vendor_id": vendor_id,
        "passenger_count": passenger_count,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "pickup_hour": pickup_hour,
        "pickup_day": pickup_day,
        "pickup_weekday": pickup_weekday,
        "pickup_month": pickup_month,
        "store_and_fwd_flag": store_and_fwd_flag
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=data
    )

    prediction = response.json()

    seconds = prediction[
        "predicted_duration_seconds"
    ]

    minutes = seconds / 60

    st.success(
        f"🚕 Estimated Duration: "
        f"{minutes:.2f} minutes"
    )