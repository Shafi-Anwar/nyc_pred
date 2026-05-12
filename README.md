# 🚕 NYC Taxi Trip Duration Prediction

An end-to-end Machine Learning project that predicts NYC taxi trip duration using trip metadata such as pickup/dropoff coordinates, pickup time, passenger count, and travel distance.

This project includes:

- 📊 Exploratory Data Analysis (EDA)
- 🧹 Data Cleaning & Outlier Handling
- ⚙️ Feature Engineering
- 🤖 XGBoost Regression Model
- 📈 Hyperparameter Tuning & Cross Validation
- 🚀 FastAPI Backend
- 🎨 Streamlit Frontend
- 🌍 Real-time Trip Duration Prediction

---

# 📌 Problem Statement

Predict the total trip duration of NYC taxi rides using trip information.

This can help in:
- ETA prediction systems
- Traffic analysis
- Ride optimization
- Intelligent transportation systems

---

# 📂 Dataset

Dataset used:
NYC Taxi Trip Duration Dataset from Kaggle

Main features:
- Pickup & dropoff coordinates
- Pickup datetime
- Passenger count
- Vendor ID
- Store and forward flag

Target:
- `trip_duration`

---

# 🧹 Data Cleaning

The dataset initially contained:
- Extreme outliers
- Unrealistic trip durations
- Abnormal distances

Outlier handling was performed using:
- Duration filtering
- Distance filtering
- Statistical analysis

---

# ⚙️ Feature Engineering

Created new features such as:

- `pickup_hour`
- `pickup_day`
- `pickup_weekday`
- `pickup_month`
- `distance_km`

Distance was calculated using the Haversine Formula.

---

# 🤖 Model Used

## XGBoost Regressor

Final tuned parameters:

```python
{
    'subsample': 1.0,
    'n_estimators': 200,
    'max_depth': 6,
    'learning_rate': 0.1,
    'colsample_bytree': 0.8
}
```

---

# 📈 Model Performance

## Final Results

| Metric | Score |
|---|---|
| R² Score | 0.79 |
| MAE | ~199 seconds |

## Cross Validation Score

```python
Mean CV Score: ~0.776
```

---

# 📊 Key Insights

- Distance was the most important feature
- Pickup hour significantly affected predictions
- Rush hour traffic increased predicted duration
- Night trips produced lower travel time predictions

---

# 🧠 Interesting Observation

The model learned realistic traffic behavior:

- Morning rush hour trips → longer duration
- Night short-distance rides → shorter duration

This indicates the model captured meaningful real-world relationships.

---

# 🚀 Backend API

Built using FastAPI.

Features:
- Automatic distance calculation using coordinates
- Real-time predictions
- Swagger UI support

### Run Backend

```bash
cd backend
uvicorn main:app --reload
```

Swagger Docs:
```text
http://127.0.0.1:8000/docs
```

---

# 🎨 Frontend

Built using Streamlit.

### Run Frontend

```bash
cd frontend
streamlit run app.py
```

---

# 📷 Project Screenshots

## Trip Duration Distribution
(Add image here)

## Distance Distribution
(Add image here)

## Feature Importance
(Add image here)

## Streamlit App
(Add image here)

---

# 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- FastAPI
- Streamlit
- Matplotlib
- Seaborn

---

#  Future Improvements

- API deployment
- Interactive maps integration
- Real-time geolocation APIs
- Dockerization
- Cloud deployment

---

# Conclusion

This project helped in understanding:

- Real-world regression problems
- Feature engineering
- Model tuning
- Error analysis
- ML deployment workflow
- Backend/frontend integration

It also demonstrated how data quality and realistic feature engineering significantly impact ML performance.
# nyc_taxi_duration_pred
# nyc_pred
