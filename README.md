## mlflow tracking server

```
docker build --platform linux/amd64 . -t a59bf2b7938a4e2f97757d53b4f0e602.azurecr.io/data-engineering-mlops-workshop:latest
az login
az acr login --name a59bf2b7938a4e2f97757d53b4f0e602
docker push a59bf2b7938a4e2f97757d53b4f0e602.azurecr.io/data-engineering-mlops-workshop:latest
```# experiment-tracking-with-mlflow
