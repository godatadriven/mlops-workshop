# Experiment Tracking with MLflow 📈

Interactive guide to experiment tracking with MLflow.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dunnkers/experiment-tracking-with-mlflow/blob/main/notebooks/mlflow-demo.ipynb)

## Set up `mlflow` tracking server

1. Create an Azure Container Registry if you don't have one yet:
```bash
az acr create --resource-group <YOUR_RESOURCE_GROUP> --name <YOUR_ACR_REGISTRY_NAME> --sku Basic --admin-enabled true
```

2. Fill in the `.env` file in this project:
   - `RESOURCE_GROUP`: The name of your resource group (`<YOUR_RESOURCE_GROUP>` from step 1)
   - `ACR_NAME`: The name of your Azure Container Registry (`<YOUR_ACR_REGISTRY_NAME>` from step 1)
   - `ACR_CONTAINER_NAME`: The name of your container image (e.g. `mlflow_image`)
   - `ACR_USERNAME`: The username of your ACR 
   - `ACR_PASSWORD`: The  password of your ACR
   - `AKS_CLUSTER_NAME`: The name of your AKS cluster (free to choose)

> **Note**: You can find your ACR credentials with: `az acr credential show --name <YOUR_ACR_REGISTRY_NAME>`

3. Export the environment variables from the `.env` file:
```bash
set -a
source .env
set +a
```

4. Build the container image:
```bash
docker build --platform linux/amd64 . -t ${ACR_NAME}.azurecr.io/${ACR_CONTAINER_NAME}:latest
```

5. Push the container image to your ACR:
```bash
az login
az acr login --name $ACR_NAME
docker push ${ACR_NAME}.azurecr.io/${ACR_CONTAINER_NAME}:latest
```

> **Note**: You can check if the image is pushed to your ACR with: `az acr repository list --name $ACR_NAME --output table`

6. Create an AKS cluster:
```bash
az aks create --resource-group $RESOURCE_GROUP --name $AKS_CLUSTER_NAME --node-count 1 --generate-ssh-keys
```

7. Get the credentials for your AKS cluster:
```bash
az aks get-credentials --resource-group $RESOURCE_GROUP --name $AKS_CLUSTER_NAME
```

8. Create a Kubernetes secret for your ACR:
```bash
kubectl create secret docker-registry acr-secret --docker-server=$ACR_NAME.azurecr.io --docker-username=$ACR_USERNAME --docker-password=$ACR_PASSWORD
```

9. Apply the deployment file to your AKS cluster:
```bash
kubectl apply -f mlflow-deployment.yaml
```

10. Wait for the external IP to be assigned to the service. You can check the status with:
```bash
kubectl get service mlflow-service --watch
```
Once the EXTERNAL-IP is assigned, you can access your MLflow instance using that IP address on port 80 (i.e., http://< EXTERNAL-IP >/).

11. Cleanup

```bash
az group delete --name $RESOURCE_GROUP
```

Or, if you want to keep your resource group, you can delete the AKS cluster and/or the ACR registry:
```bash
az aks delete --resource-group $RESOURCE_GROUP --name $AKS_CLUSTER_NAME --yes --no-wait
az acr delete --resource-group $RESOURCE_GROUP --name $ACR_NAME --yes --no-wait
```
