"""
Crop Recommendation System
Sample Implementation

This file illustrates the workflow of the original project.
"""

import streamlit as st

st.set_page_config(page_title="Crop Recommendation", layout="wide")

st.title("Crop Recommendation System")

st.markdown("""
## Workflow

1. User selects a district.
2. Soil nutrients (N, P, K, pH) are retrieved.
3. User enters cultivation month, year, temperature and humidity.
4. A Random Forest Regressor predicts rainfall.
5. The following features are combined:
   - Nitrogen
   - Phosphorous
   - Potassium
   - pH
   - Temperature
   - Humidity
   - Predicted Rainfall
6. An XGBoost Classifier recommends the most suitable crop.
""")

st.info(
    "Original datasets and trained model files are intentionally "
    "excluded from this repository."
)
