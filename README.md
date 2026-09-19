# 🌦 Thunderstorm (TH) Forecasting System

A machine learning–based application for **Thunderstorm (TH) occurrence prediction** using atmospheric indices.  
The project uses a **pre-trained & compressed Decision Tree Classifier model** and provides an **interactive Streamlit web interface** for real-time predictions.

---

## 🚀 Live Demo

[![Open Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://thunderstrom-forcasting.streamlit.app/)

### 🌩️ Try the Thunder Forecasting App

**[👉 Click here to make a prediction](https://thunderstrom-forcasting.streamlit.app/)**

---

## 🚀 Features

- ✅ Pre-trained **Decision Tree Classifier**
- ✅ Model size optimized using **Joblib compression**
- ✅ Interactive **Streamlit UI**
- ✅ No retraining required (inference-only)
- ✅ Ready for **Docker** and **Cloud deployment (Render / AWS)**
- ✅ Modular & production-ready project structure

---

## 📊 Input Features

The model predicts thunderstorm occurrence using the following atmospheric parameters:

- SWEAT Index  
- K Index  
- Totals Totals Index  
- Environmental Stability  
- Moisture Indices  
- Convective Potential  
- Temperature Pressure  
- Moisture Temperature Profiles  

---

## 🧠 Model Details

- **Algorithm**: Decision Tree Classifier  
- **Training**: Offline (not included in this repo)  
- **Class Imbalance Handling**: SMOTE  
- **Evaluation Metrics**:
  - Accuracy
  - Precision
  - Recall
  - F1-score
  - Probability of Detection (POD)
  - False Alarm Rate (FAR)
  - Heidke Skill Score (HSS)
  - Critical Success Index (CSI)

- **Model Format**: `joblib`  
- **Compressed Size**: ~5–10 MB  


---



