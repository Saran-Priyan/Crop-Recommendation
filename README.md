
# Crop Recommendation System

## Overview

The Crop Recommendation System is a machine learning application developed using **Python** and **Streamlit** to assist farmers in selecting suitable crops based on environmental and soil conditions.

The application first predicts rainfall for the selected cultivation period using a **Random Forest Regressor**, then combines the predicted rainfall with soil nutrients and environmental parameters to recommend a suitable crop using an **XGBoost Classifier**.

---

## Problem Statement

Choosing crops based only on experience can result in lower productivity due to changing weather conditions and soil characteristics.

This project helps farmers make data-driven decisions by combining historical rainfall trends, district-wise soil nutrient information and machine learning.

---

## Workflow

```text
District
   │
   ▼
Retrieve Soil Parameters (N, P, K, pH)
   │
Month + Year
   │
   ▼
Random Forest Regressor
Rainfall Prediction
   │
Temperature + Humidity
   │
   ▼
Feature Vector
(N, P, K, pH, Temp, Humidity, Predicted Rainfall)
   │
   ▼
XGBoost Classifier
   │
   ▼
Recommended Crop
```

---

## Datasets

### Soil Dataset
- District-wise Nitrogen
- Phosphorous
- Potassium
- pH

### Historical Rainfall Dataset
Monthly rainfall records collected across Tamil Nadu over multiple years.

### Crop Recommendation Dataset
Contains:
- Nitrogen
- Phosphorous
- Potassium
- Temperature
- Humidity
- pH
- Rainfall
- Crop Label

---

## Machine Learning Models

### Rainfall Forecasting
- Random Forest Regressor

### Crop Recommendation
- XGBoost Classifier

---

## Features

- Streamlit dashboard
- District-wise soil lookup
- Rainfall forecasting
- Crop recommendation
- Data visualization
- Dataset explorer

---

## Tech Stack

- Python
- Streamlit
- Pandas
- Scikit-learn
- XGBoost
- Matplotlib
- Seaborn

---

## Project Structure

```text
crop-recommendation-system/
│
├── README.md
├── sample_code.py
├── screenshots/
├── docs/
└── LICENSE
```

---

## Screenshots

Add your screenshots inside the `screenshots` folder and reference them like:

```markdown
![Home](screenshots/home.png)

![Prediction](screenshots/prediction.png)

![Analysis](screenshots/analysis.png)
```

---

## Repository Note

This repository contains project documentation and a sample implementation.

The original datasets and trained model files are not included.

---

## Future Improvements

- Live weather API
- Fertilizer recommendation
- Crop yield prediction
- Satellite imagery integration

---

## License

For learning and portfolio purposes.
