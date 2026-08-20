# AI-Based Smart Tourism Safety and Crowd Prediction System for Sri Lanka

## Project Overview

This project proposes an AI-Based Smart Tourism Safety and Crowd Prediction System for Sri Lanka.

The system uses tourism data, weather information, seasonal patterns, event schedules and tourist-related data to predict crowd density and identify potential tourism safety risks.

The main objective is to provide intelligent safety recommendations, travel alerts and route suggestions to improve tourist safety and travel experiences.

## Research Question

How can the use of AI-based predictive analytics improve tourist safety and crowd management in Sri Lanka?

## Main Objectives

- Predict tourist crowd density at selected Sri Lankan tourism destinations.
- Identify potential tourism safety risks.
- Analyse the influence of weather, seasons and events on crowd levels.
- Provide intelligent safety recommendations.
- Support tourists with travel alerts and route suggestions.

## Proposed Machine Learning Approach

The project will compare a baseline classification model with advanced machine learning models.

### Baseline

- Logistic Regression

### Proposed Models

- Random Forest
- XGBoost

## Dataset

The planned dataset will combine tourism and environmental information from relevant sources.

Potential data sources include:

- Tourism statistics
- Weather data
- Seasonal information
- Event and festival schedules
- Tourist survey data
- Publicly available tourism-related trends

The target variable will classify crowd density into:

- Low
- Medium
- High

## Data Preprocessing

The preprocessing pipeline includes:

- Removing duplicate records
- Handling missing values
- Data cleaning
- Encoding categorical variables
- Numerical feature processing
- Feature engineering
- Preparing the dataset for machine learning

The preprocessing implementation is available in:

`src/preprocessing/preprocess_data.py`

## Evaluation

The planned evaluation metrics include:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC

The models will be evaluated using Stratified 5-Fold Cross-Validation.

## Project Structure

```text
tourism-safety-crowd-prediction-sl/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── diagrams/
│
├── notebooks/
│
├── results/
│
├── src/
│   └── preprocessing/
│       └── preprocess_data.py
│
├── README.md
└── requirements.txt
