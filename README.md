# Freight Cost Predictor & Invoice Approval System

**Vendor Invoice Intelligence System**  
An End-to-End Machine Learning Solution for Freight Cost Prediction and Automated Invoice Risk Flagging

![Streamlit App](https://freight-cost-predictor-and-approval-system-ftjrpdwuhzjptvpwsvy.streamlit.app/)  

## 🎯 Project Overview

This project automates vendor invoice processing for finance and procurement teams by solving two critical business problems:

- **Freight Cost Prediction (Regression)**: Predicts accurate freight/shipment cost based on quantity and dollar value to improve budgeting, forecasting, and vendor negotiations.
- **Invoice Risk Flagging (Classification)**: Automatically flags high-risk invoices that require manual approval (e.g., quantity/dollar mismatches, unusual delays) while allowing low-risk invoices for auto-approval.

The system reduces manual effort, minimizes cost leakage, and lowers audit risks — making it a strong **portfolio project** for Data Science / ML Engineer roles.

## ✨ Key Features

- **Freight Cost Prediction** using Linear Regression (Best R² Score: **93.66%**)
- **Invoice Flagging System** using Random Forest Classifier (Accuracy: **~89%**, optimized with GridSearchCV)
- Interactive **Streamlit Web Application** for real-time predictions
- Modular code structure with separate pipelines for regression and classification
- Data preprocessing from SQLite database with feature engineering (receiving delay, PO to invoice days, etc.)
- Model saving/loading using Joblib
- Clean folder structure for production readiness

## 🛠️ Tech Stack

- **Language**: Python
- **Data Handling**: Pandas, NumPy, SQLite3
- **Machine Learning**: Scikit-learn (Linear Regression, Random Forest, etc.)
- **Frontend**: Streamlit
- **Model Serialization**: Joblib
- **Version Control**: Git & GitHub

## 📁 Project Structure

```bash
Freight-Cost-Predictor-and-Approval-System/
├── Data/                  # SQLite database and raw data
├── models/                # Trained models (.pkl files)
├── Nootbooks/             # EDA and experimentation notebooks
├── freight_cost_prediction/   # Regression pipeline
├── invoice_flagging/      # Classification pipeline
├── inference/             # Prediction scripts
├── app.py                 # Main Streamlit application
├── requirements.txt
├── .gitignore
└── README.md
```
## 📊 Data Source

The dataset used in this project is the **Invoice Intelligence Data**, stored in an SQLite Database (`inventory.db`).
* **Link:** [Invoice Intelligence Data](https://topmate.io/ayushi_mishra/1981139)

## 📁 How to Run Project

### 1. Clone the Repository
```bash
git clone https://github.com/U10Umair/Freight-Cost-Predictor-and-Approval-System.git
cd Freight-Cost-Predictor-and-Approval-System
```
### 2. Create Virtual Environment
```bash
python -m venv forProjects
forProjects\Scripts\activate     # For Windows
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the Streamlit App
```bash
streamlit run app.py
```

### 📊 Model Performance

| Task | Best Model | Metric | Score |
| :--- | :--- | :--- | :--- |
| **Freight Cost Prediction** | Linear Regression | R² Score | 93.66% |
| **Invoice Risk Flagging** | Random Forest Classifier | Accuracy | ~89% |

### 🌟 What I Learned

* **End-to-End ML Pipeline:** Building a complete workflow from raw SQLite data ingestion to a fully deployed web application.
* **Real-World Feature Engineering:** Transforming raw invoice and freight data into model-ready features.
* **Advanced Model Development:** Implementation of model training, evaluation, and hyperparameter optimization using **GridSearchCV**.
* **Interactive Web Interface:** Developing a user-friendly frontend using **Streamlit** for real-time predictions.
* **Production-Ready Code:** Adhering to project structuring and modular coding best practices for scalability.
* **Project Management:** Best practices for managing ML projects on **GitHub**, including handling large files and effective use of `.gitignore`.
