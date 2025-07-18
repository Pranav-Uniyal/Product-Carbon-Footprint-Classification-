# 🌱 Product-Carbon-Footprint-Classification

A machine learning-based project that classifies products into **Low**, **Medium**, or **High** carbon footprint categories using structured product and environmental data. The goal is to raise sustainability awareness and help businesses evaluate the environmental impact of their products.

---

## Project Overview

This project involves:
- Exploratory Data Analysis (EDA)
- Data cleaning and preprocessing
- Model training and evaluation
- Classification using **Random Forest**
- Streamlit web application for interactive usage

---

##  Features

- 🧼 Cleaned and preprocessed dataset
- 🔍 Feature engineering and selection
- 🧠 Model trained to predict carbon footprint class
- 📉 Model saved as `.pkl` for reuse
- 🌐 Streamlit-based UI for real-time predictions

---

## Tech Stack

- **Python**
- **Pandas, NumPy, Scikit-Learn**
- **Matplotlib, Seaborn**
- **Streamlit**
- **Pickle** (for model serialization)

---

## 📁 Project Structure

```
├── EDA+Preprocessing.ipynb            # EDA and data cleaning notebook
├── df_cleaned.csv                     # Cleaned dataset used for modeling
├── carbonfootprint_prediction.ipynb   # Model training & evaluation notebook
├── carbon-footprint_model.pkl         # Trained classification model
├── app.py                             # Streamlit app for prediction
├── LICENSE                            # Apache-2.0 License
├── README.md                          # Project documentation
```
----
# Model Performance
The model was trained using a Decision Tree Classifier and evaluated on a test set of 29 samples. Below are the classification metrics:
```
              precision    recall  f1-score   support

      Low        0.62       1.00      0.76        8
   Medium        0.90       0.60      0.72       15
     High        0.83       0.83      0.83        6

accuracy                             0.76       29
macro avg        0.78       0.81      0.77       29
weighted avg     0.81       0.76      0.76       29
```
---
# Installation & Usage
## Step 1: Clone the Repository
```bash
git clone https://github.com/Pranav-Uniyal/Product-Carbon-Footprint-Classification-.git
cd Product-Carbon-Footprint-Classification-
```
## Step 2: Install Dependencies
```
pip install pandas numpy scikit-learn matplotlib seaborn streamlit
```
## Step 3: Run the App
```
streamlit run app.py
```
Then go to http://localhost:8501 in your browser to access the app.

----
## Data Description
df_cleaned.csv: Cleaned dataset containing relevant features

carbon-footprint_model.pkl: Serialized trained classifier

EDA+Preprocessing.ipynb: Data exploration and cleaning

carbonfootprint_prediction.ipynb: Model training and evaluation logic

----
# 📌 Future Enhancements
Add deep learning model (e.g., MLP) for better accuracy

Use external product APIs (like OpenLCA or Ecoinvent) for carbon data

Visualize feature importance using SHAP or LIME

Deploy on HuggingFace or Streamlit Cloud

## Author
# Pranav Uniyal


## 📜 License
**Licensed under the Apache-2.0 License.**
