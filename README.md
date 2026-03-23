# 💰 Salary Prediction System

A complete end-to-end Machine Learning application that predicts salaries using user inputs and a trained regression model, deployed with an interactive Streamlit interface.

---

##  Project Overview

The **Salary Prediction System** is a data-driven application that estimates an individual's salary based on multiple input parameters such as experience, education, and job-related features.

This project demonstrates the complete ML pipeline:

* Data preprocessing
* Model training
* Model deployment
* Interactive frontend

---

##  Objective

* Predict salaries using machine learning
* Provide insights for job seekers and students
* Demonstrate real-world ML deployment

---

##  Technologies & Tools Used

###  Programming Language

* Python 3.10

###  Libraries Used

#### 🔹 Data Handling

* Pandas → Data cleaning & manipulation
* NumPy → Numerical computations

#### 🔹 Machine Learning

* Scikit-learn

  * Linear Regression
  * Polynomial Regression
  * Train-Test Split
  * Feature Scaling
  * Model Evaluation

#### 🔹 Model Saving & Loading

* Pickle / Joblib

  * Save trained model (`model.pkl`)
  * Save preprocessing objects (`poly.pkl`, `columns.pkl`)

---

###  Frontend

* Streamlit

  * Interactive UI
  * Input forms
  * Real-time prediction display

---

###  Development Tools

* VS Code / PyCharm
* Jupyter Notebook (for model training)
* Git & GitHub (version control)

---

##  Machine Learning Workflow

### 1. Data Collection

Dataset containing:

* Experience
* Education
* Job role
* Salary

---

### 2. Data Preprocessing

* Handling missing values
* Encoding categorical data
* Feature scaling
* Feature transformation (Polynomial Features if used)

---

### 3. Model Training

Algorithm used:

* Linear Regression
* Polynomial Regression

---

### 4. Model Evaluation

Metrics:

* R² Score
* Mean Squared Error

---

### 5. Model Deployment

* Model saved using `pickle`
* Integrated into Streamlit app

---

## 📂 Project Structure

```
salary-prediction/
│
├── app.py                 # Streamlit UI application
├── model.pkl              # Trained ML model
├── poly.pkl               # Polynomial transformer
├── columns.pkl            # Feature columns
├── requirements.txt       # Project dependencies
├── README.md              # Documentation
│
├── notebooks/
│   └── model_training.ipynb   # Model training code
│
└── data/
    └── salary_data.csv    # Dataset
```

---

## ▶️ How to Run the Project

### 1. Clone Repository

```
git clone https://github.com/Hariom-patidar-tech/salary-prediction.git
cd salary-prediction
```

### 2. Create Virtual Environment

```
python -m venv venv
```

### 3. Activate Environment

```
venv\Scripts\activate
```

### 4. Install Dependencies

```
pip install -r requirements.txt
```

### 5. Run Application

```
streamlit run app.py
```

---

##  How the System Works

### User Inputs:

* Experience
* Education
* Job details

### Backend Processing:

* Input converted into numerical format
* Passed through preprocessing pipeline

### Prediction:

* Model predicts salary

### Output:

* Salary displayed on UI

---

##  Key Features

* Real-time prediction
* Clean and modern UI
* End-to-end ML pipeline
* Scalable architecture
* Fast execution

---

##  Future Enhancements

* User authentication system
* API integration (FastAPI backend)
* Advanced ML models (XGBoost, Random Forest)
* Deployment on cloud
* AI-based career recommendation

---

##  Author

**Hariom Patidar**

---

##  Support

If you found this project useful, consider giving it a ⭐ on GitHub.
