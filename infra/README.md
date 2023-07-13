
# How to set up the MLflow tracking server


## Pre-requisites

- Docker installed
- Kubernetes CLI
- ...

## Setup on Azure Kubernetes Service (AKS)

The following setup is tailored towards Azure, but can easily extended to other cloud services, as we only need a container registry, a kubernetes cluster, and a place for us to ...

1. Create an Azure Container Registry if you don't have one yet:
```bash
az acr create --resource-group <YOUR_RESOURCE_GROUP> --name <YOUR_ACR_REGISTRY_NAME> --sku Basic --admin-enabled true
```

1. Fill in the `.env` file in this project:
   - `RESOURCE_GROUP`: The name of your resource group (`<YOUR_RESOURCE_GROUP>` from step 1)
   - `ACR_NAME`: The name of your Azure Container Registry (`<YOUR_ACR_REGISTRY_NAME>` from step 1)
   - `ACR_IMAGE_NAME`: The name of your container image (e.g. `mlflow_image`)
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
docker build --platform linux/amd64 . -t ${ACR_NAME}.azurecr.io/${ACR_IMAGE_NAME}:latest
```

5. Push the container image to your ACR:
```bash
az login
az acr login --name $ACR_NAME
docker push ${ACR_NAME}.azurecr.io/${ACR_IMAGE_NAME}:latest
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

11. Troubleshoot <br>

11.1 If the above step seems to fail, you may want to check your pods:
```bash
kubectl get pods
```
To get more information about a specific pod, you can use:
```bash
kubectl describe pod <POD_NAME>
```
If it states the image name is incorrect, you may need to update the line with `image: ${ACR_NAME}.azurecr.io/${ACR_IMAGE_NAME}:latest` in `mlflow-deployment.yaml`, replacing the placeholders `${...}` with the actual values. Run `kubectl apply -f mlflow-deployment.yaml` again to apply the changes. Go back to step 10 to check the status of the service.

11.2 If computational limits are reached, increase the number of replicas in `mlflow-deployment.yaml` and apply the changes with `kubectl apply -f mlflow-deployment.yaml`.


1.  Cleanup

```bash
az group delete --name $RESOURCE_GROUP
```

Or, if you want to keep your resource group, you can delete the AKS cluster and/or the ACR registry:
```bash
az aks delete --resource-group $RESOURCE_GROUP --name $AKS_CLUSTER_NAME --yes --no-wait
az acr delete --resource-group $RESOURCE_GROUP --name $ACR_NAME --yes --no-wait
```
