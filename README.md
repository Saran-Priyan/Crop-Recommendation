# Crop Recommendation System

## Overview

Crop Recommendation System is a machine learning application developed using **Python** and **Streamlit** to recommend suitable crops for cultivation based on soil properties, weather conditions, and predicted rainfall.

The application combines district-wise soil nutrient information, historical rainfall records, and machine learning models to assist farmers in making data-driven crop selection decisions.

---

## Problem Statement

Selecting crops based only on traditional farming practices may lead to lower yields due to changing environmental conditions.

This project aims to recommend suitable crops by combining:

- District-wise soil nutrients
- Historical rainfall patterns
- Temperature
- Humidity
- Soil pH
- Machine Learning

---

## Solution

The application follows two machine learning stages:

1. Predict rainfall for the selected cultivation period using historical rainfall data.
2. Use the predicted rainfall together with soil nutrients and environmental conditions to recommend the most suitable crop.

---

## Workflow

```text
Select District
        │
        ▼
Retrieve Soil Parameters
(Nitrogen, Phosphorous, Potassium, pH)

        │

Enter Month & Year
        │
        ▼

Predict Rainfall
(Random Forest Regressor)

        │

Enter Temperature
Enter Humidity

        │
        ▼

Feature Vector

N
P
K
pH
Temperature
Humidity
Predicted Rainfall

        │
        ▼

XGBoost Classifier

        │
        ▼

Recommended Crop
```

---

## Features

- Streamlit web interface
- District-wise soil lookup
- Rainfall forecasting
- Crop recommendation
- Dataset explorer
- Interactive visualizations using Matplotlib and Seaborn
- Multiple data analysis charts

---

## Machine Learning Models

### Rainfall Forecasting

- Random Forest Regressor

### Crop Recommendation

- XGBoost Classifier

---

## Datasets

### Soil Dataset

Contains district-wise soil nutrient information including:

- Nitrogen
- Phosphorous
- Potassium
- Soil pH

### Rainfall Dataset

Historical monthly rainfall records collected across Tamil Nadu over multiple years.

### Crop Dataset

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
Crop-Recommendation-System/
│
├── app.py
├── Crop.csv
├── Soil.csv
├── Rainfall.csv
├── xgboost_crop_model.pkl
├── requirements.txt
├── README.md
├── screenshots/
└── docs/
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/Saran-Priyan/crop-recommendation-system.git
cd crop-recommendation-system
```

### Create a Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

If your main file is named **app.py**:

```bash
streamlit run app.py
```

If it is still named **MyApp.py**:

```bash
streamlit run MyApp.py
```

The application will start at:

```
http://localhost:8501
```

---

## Screenshots

Create a folder named **screenshots** and place your application screenshots inside it.

Example:

```markdown
![Home](screenshots/home.png)

![Data](screenshots/data.png)

![Analysis](screenshots/analysis.png)

![Prediction](screenshots/prediction.png)
```

---

## Future Improvements

- Live weather API integration
- Fertilizer recommendation
- Crop yield prediction
- Disease prediction
- Satellite imagery integration

---

## License

This project is intended for educational and portfolio purposes.
