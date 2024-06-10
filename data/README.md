# Data Folder

This folder contains the datasets used in the phishing detection project.

## Contents

- **raw** sub-folder: Contains the original dataset used for training and testing the models.
  - `phishing_data.csv`: Original dataset with features and labels.

- **processed** sub-folder: Contains processed datasets and model results.
  - `phishing_processed.csv`: Processed dataset ready for model training.
  - `model_results.csv`: Results of machine learning models trained on the processed dataset.

## Description

- **phishing_data.csv**: This CSV file contains the original dataset used for training and testing the machine learning models. It includes features extracted from various webpages along with labels indicating whether each webpage is a phishing website or not.

- **phishing_processed.csv**: After preprocessing the original dataset, the data is saved in this file. It contains cleaned and preprocessed features, which are ready for training machine learning models.

- **model_results.csv**: This file stores the results of the machine learning models trained on the processed dataset. It includes metrics such as accuracy, F1 score, precision, and recall for each model.

## Usage

- The `raw` sub-folder contains the original dataset, which can be used for data exploration, preprocessing, and model training.

- After preprocessing the data, the cleaned dataset is saved in the `processed` sub-folder as `phishing_processed.csv`.

- The `model_results.csv` file in the `processed` sub-folder provides insights into the performance of the trained machine learning models.