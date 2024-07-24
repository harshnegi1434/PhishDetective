# PhishDetective: Online Phishing Detection System

PhishDetective is an online phishing detection system designed to identify phishing websites using machine learning. This project consists of a frontend created with Next.js, Tailwind CSS, and Acertainity UI, and a backend built with Python Flask. The dataset used for model training was sourced from Kaggle and pre-processed to create a refined dataset for training various ML algorithms. The best model, Gradient Boosting Classifier, was then deployed. The entire project is migrated to Azure using Docker, Azure Container Registry (ACR), and Azure Container Instances (ACI).

You can access the website here - [Deployed Link](https://phishdetective.vercel.app)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Project Structure](#project-structure)
- [Setup and Deployment](#setup-and-deployment)
- [Usage](#usage)
- [Screenshots](#screenshots)


## Overview

PhishDetective leverages machine learning to detect phishing websites. The project consists of a user-friendly frontend interface and a robust backend server that processes and classifies URLs. The trained machine learning model is deployed to Azure for reliable and scalable operation.

## Features

- **Next.js Frontend**: Built with Next.js, Tailwind CSS, and Acertainity UI for a responsive and interactive user interface.
- **Flask Backend**: Python Flask server handling the backend logic and API endpoints.
- **Machine Learning Model**: Gradient Boosting Classifier trained on a pre-processed dataset.
- **Azure Deployment**: Dockerized application deployed to Azure Container Registry and Azure Container Instances.

## Dataset

The dataset used for training the model was sourced from Kaggle. It contains various features extracted from URLs to identify whether they are phishing sites. The dataset was pre-processed to enhance the accuracy of the model.

## Model Training

Multiple machine learning algorithms were applied to the dataset, and the Gradient Boosting Classifier was selected as the best performing model. The model was trained, saved, and integrated into the backend server for real-time phishing detection.

## Project Structure

```plaintext
PhishDetective/
├── backend/
│   ├── data/
│   ├── models/
│   ├── notebooks/
│   ├── .dockerignore 
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── urlanalyzer.py
├── frontend/
│   ├── app/
│   ├── components/
│   ├── public/
│   ├── utils/
│   ├── tailwind.config.js
│   ├── next.config.js
│   ├── package-lock.json
│   ├── package.json
│   ├── tailwind.config.js
│   ├── README.md
│   ├── .dockerignore
│   ├── Dockerfile
├── .gitignore
├── README.md
└── docker-compose.yml
```

## Setup and Deployment
#### Prerequisites
1. Docker
2. Azure CLI
3. Git


#### Steps
1. Clone the Repository

```bash
git clone https://github.com/yourusername/PhishDetective.git
cd PhishDetective
```

2. Build Docker Images
```bash
docker-compose build
```

3. Push to Azure Container Registry (ACR)
```bash
az acr login --name youracrname
docker tag phishdetective-frontend:latest youracrname.azurecr.io/phishdetective-frontend:latest
docker tag phishdetective-backend:latest youracrname.azurecr.io/phishdetective-backend:latest
docker push youracrname.azurecr.io/phishdetective-frontend:latest
docker push youracrname.azurecr.io/phishdetective-backend:latest
```
4. Deploy to Azure Container Instances (ACI)
```bash
az container create --resource-group yourResourceGroup --name phishdetective-frontend --image youracrname.azurecr.io/phishdetective-frontend:latest --dns-name-label phishdetective-frontend --ports 80
az container create --resource-group yourResourceGroup --name phishdetective-backend --image youracrname.azurecr.io/phishdetective-backend:latest --dns-name-label phishdetective-backend --ports 5000
```

**Some of the Commands for Azure Deployment and switching between production/deployment is also mentioned in other .md Files**

## Usage
Access the frontend through the deployed DNS name and use the provided interface to enter URLs and receive phishing detection results.


## Screenshots

![Home Page](/images/homepage.png)

![Safe](/images/safe.png)

![Unsafe](/images/unsafe.png)

