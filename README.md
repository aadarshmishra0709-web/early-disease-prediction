[README.md](https://github.com/user-attachments/files/32843386/README.md)
# 🩺 Early Disease Prediction

A machine learning-based web application that predicts a possible
disease from user-selected symptoms.

The system uses a **Gaussian Naive Bayes** classifier trained on a
symptom-based disease dataset and provides an interactive Streamlit
interface.

> ⚠️ **Medical Disclaimer:** This is an educational machine-learning
> project, not a medical diagnostic tool. Predictions should not replace
> advice or evaluation from a qualified healthcare professional.

## 🌐 Links

-   **Live Demo:**
    https://early-disease-prediction-ksmtxxvp4plz65lwoztplk.streamlit.app
-   **GitHub:**
    https://github.com/aadarshmishra0709-web/early-disease-prediction

## ✨ Features

-   Search and select symptoms
-   Machine learning-based disease prediction
-   Model-estimated probability for the predicted class
-   Interactive dark-themed Streamlit UI
-   Fast prediction using Gaussian Naive Bayes
-   Public Streamlit deployment

## 🧠 Machine Learning

The project evaluates:

-   Decision Tree
-   Random Forest
-   Gaussian Naive Bayes
-   Support Vector Machine (SVM)
-   K-Nearest Neighbors (KNN)

**Final model:** Gaussian Naive Bayes

It was selected because it achieved comparable measured performance
while remaining simple, fast, and lightweight for deployment.

## 📊 Dataset

-   Training records: **4,920**
-   Symptom features: **132**
-   Disease classes: **42**
-   Duplicate records: **4,616**
-   Unique symptom patterns: **304**
-   Missing values: **None found**

Because the dataset contains many duplicate records, evaluation was also
performed using unique symptom patterns.

## 📈 Results

On the provided `Testing.csv` dataset:

**Gaussian Naive Bayes accuracy: 100%**

Duplicate-aware 5-fold stratified cross-validation on the **304 unique
symptom patterns** also produced:

**Mean accuracy: 100%**

These results describe performance on this dataset only and must not be
interpreted as clinical or real-world diagnostic accuracy.

## 🔄 Workflow

``` text
Symptom Dataset
      ↓
Data Cleaning
      ↓
Duplicate & Data Analysis
      ↓
Feature / Target Separation
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Gaussian Naive Bayes
      ↓
Model Serialization
      ↓
Streamlit Web Application
      ↓
Public Deployment
```

## 🛠️ Technology Stack

-   **Python**
-   **Pandas**
-   **NumPy**
-   **Scikit-learn**
-   **Gaussian Naive Bayes**
-   **Joblib**
-   **Streamlit**
-   **Git & GitHub**
-   **Streamlit Community Cloud**

## 📁 Project Structure

``` text
early-disease-prediction/
│
├── app.py
├── requirements.txt
├── .gitignore
│
└── models/
    ├── disease_model.pkl
    └── feature_names.pkl
```

## ⚙️ Run Locally

### 1. Clone the repository

``` bash
git clone https://github.com/aadarshmishra0709-web/early-disease-prediction.git
cd early-disease-prediction
```

### 2. Install dependencies

``` bash
pip install -r requirements.txt
```

### 3. Run the application

``` bash
streamlit run app.py
```

Open:

``` text
http://localhost:8501
```

## 🧪 Example

Select symptoms such as:

``` text
skin_rash
itching
```

Then click **Predict Disease**.

The trained model generates a prediction based on the selected symptom
pattern.

## 🔮 Future Improvements

-   Use a larger and more diverse medical dataset
-   Validate with clinically curated external data
-   Add top-3 predictions
-   Add symptom descriptions
-   Improve model interpretability
-   Improve mobile accessibility
-   Add more robust external validation

## 👨‍💻 Author

**Aadarsh Mishra**

Computer Science & Engineering - Data Science\
ABES Engineering College

## 📜 License

This project is intended for educational and academic purposes.
