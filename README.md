# Experiment Tracking with MLflow 📈

Interactive guide to experiment tracking with MLflow.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dunnkers/experiment-tracking-with-mlflow/blob/main/notebooks/mlflow-demo.ipynb)

## Set up `mlflow` tracking server

```
ACR_NAME=<YOUR_ACR_REGISTRY_NAME>
ACR_CONTAINER_NAME=<YOUR_ACR_IMAGE_NAME>
docker build --platform linux/amd64 . -t $ACR_NAME.azurecr.io/$ACR_CONTAINER_NAME:latest
az login
az acr login --name $ACR_NAME
docker push $ACR_NAME.azurecr.io/$ACR_CONTAINER_NAME:latest
```
