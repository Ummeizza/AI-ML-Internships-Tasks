# Task 10 — Pipeline Engineering with Scikit-Learn

## 📌 Project Overview

This project implements a reproducible Scikit-Learn machine learning pipeline for Titanic survival prediction.

The pipeline combines custom feature engineering, preprocessing, categorical encoding, model training, evaluation, and Joblib serialization into a single workflow.

The main goal is to prevent inconsistencies between training and inference preprocessing.

---

## 🎯 Objective

The objective is to build one reusable pipeline that handles the workflow from raw passenger data to final predictions.

The solution demonstrates:

- Scikit-Learn Pipeline
- ColumnTransformer
- Custom Transformers
- FeatureUnion concept
- Random Forest classification
- Baseline comparison
- Joblib pipeline serialization

---

## 📊 Dataset

**Dataset:** Titanic Dataset

The dataset contains information about passengers aboard the Titanic.

### Target Variable

`Survived`

- `0` — Did Not Survive
- `1` — Survived

### Selected Features

- Pclass
- Age
- Sex
- SibSp
- Parch
- Fare
- Embarked

A derived `FamilySize` feature was also created.

---

## 🧹 Data Cleaning and Preprocessing

The following transformations were applied:

### Numerical Features

- Missing values → median imputation
- Standardization → `StandardScaler`

### Categorical Features

- Missing values → most frequent value
- Encoding → `OneHotEncoder`
- Unknown categories → ignored using `handle_unknown="ignore"`

### Feature Engineering

A custom transformer creates:

`FamilySize = SibSp + Parch + 1`

This transformation is included inside the pipeline.

---

## 🔧 Pipeline Architecture

The final workflow is:

```text
Raw Titanic Data
       ↓
FamilySizeTransformer
       ↓
ColumnTransformer
       ├── Numerical Pipeline
       │     ├── Median Imputation
       │     └── Standard Scaling
       │
       └── Categorical Pipeline
             ├── Most-Frequent Imputation
             └── One-Hot Encoding
       ↓
Random Forest Classifier
       ↓
Predictions
##Clone Repository
git clone https://github.com/Ummeizza/AI-ML-Internships-Tasks.git

#Navigate to Task 10
cd AI-ML-Internships-Tasks/Task_10_Pipeline_Engineering_with_Scikit_Learn

##Install Dependencies
pip install -r requirements.txt

##Open the Notebook
jupyter notebook Task_10_Pipeline_Engineering.ipynb