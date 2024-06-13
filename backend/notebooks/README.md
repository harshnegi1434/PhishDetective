# Notebooks Overview

This directory contains Jupyter notebooks used in the phishing detection project. Each notebook serves a distinct purpose in the data analysis and model development workflow.

## Notebooks

### 01_data_loading_and_exploration.ipynb
- **Purpose**: 
  - Load the phishing dataset and perform initial checks.
  - Conduct Exploratory Data Analysis (EDA) to understand the data distribution, identify potential issues, and visualize key features.
- **Key Steps**:
  - Data Loading
  - Data Familiarization
  - EDA (Exploratory Data Analysis)
  - Data Visualization

### 02_data_preparation_and_modeling.ipynb
- **Purpose**: 
  - Preprocess and prepare the data for modeling.
  - Train and evaluate a range of machine learning models to detect phishing websites.
- **Key Steps**:
  - Data Preprocessing (cleaning, feature engineering, etc.)
  - Splitting the data into training and testing sets
  - Model Training with various algorithms:
    - Logistic Regression
    - k-Nearest Neighbors
    - Support Vector Classifier
    - Naive Bayes
    - Decision Tree
    - Random Forest
    - Gradient Boosting
    - Catboost
    - Xgboost
    - Multilayer Perceptrons
  - Model Performance Comparison

### 03_results_and_conclusion.ipynb
- **Purpose**: 
  - Analyze and compare the performance of the trained models.
  - Summarize findings and draw conclusions from the project.
- **Key Steps**:
  - Detailed analysis of model performance metrics
  - Visual comparison of model results
  - Final model selection and reasoning
  - Project conclusions and potential next steps

## Additional Notes
- **Dependencies**: Ensure all necessary libraries and packages are installed as listed in the `requirements.txt` file.
- **Data Files**: Raw and processed data files are located in the `data/` directory. Refer to the respective notebooks for details on data handling.


