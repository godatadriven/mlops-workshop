# Automate deployment with (CI)/CD 🤖

We already went from a local notebook to a container to cloud. But we can do better!

So far, we have run things ourself, either in the UI, or through the CLI. But we can automate this process, so that our application is automatically deployed to the cloud when we push a new version of the code to our repository.

To do so, we will use GitHub Actions, a CI/CD tool that is integrated with GitHub.

## Github Actions

We have already created a start for a GitHub Actions workflow in `.github/workflows/pipeline.yml`. This workflow will run every time a pull request is merged in our repository (also when one is only *closed*, but let's ignore that for now).

The workflow contains the following steps:
- Build and push the container image to Docker Hub
- Deploy the container image to Azure or GCP

## Running the workflow as-is

1. Inspect the workflow file
2. Try to run the workflow as-is:
   - Copy or fork this repository to your own account
   - Go to Settings for repository in your account in the Github UI 
   - Go to "Sectrets and variables" > "Actions"
   - Add new repository secrets:
     - `DOCKERHUB_USERNAME`: your Docker Hub username
     - `DOCKERHUB_PASSWORD`: your Docker Hub passwords
   - Create a branch, make a change, and open a pull request
   - Close the pull request
   - Check out the Actions tab in the Github UI
   - Can you see the workflow run? Does it succeed?

## Extend the workflow with your specific deployment step

### Azure

1. Uncomment the Azure deployment step
2. To find necessary credentials which allow you to login in your Github workflow, run:

```bash
az ad sp create-for-rbac --name "github-actions" --role contributor \                        
                            --scopes /subscriptions/<your-subscription-id>/resourceGroups/mlops-tutorial \
                            --sdk-auth
```
- With `<your-subscription-id>`, which you can [find here](https://portal.azure.com/#blade/Microsoft_Azure_Billing/SubscriptionsBlade).

3. Copy the output of this command and add it as a secret in your repository, called `AZURE_CREDENTIALS`.
4. Create a branch, make a change, and open a pull request
5. Close the pull request, and inspect the workflow run in the Github UI 🎉

### GCP

1. Uncomment the GCP deployment step
2. Go to the [GCP console](https://console.cloud.google.com/)
3. Navigate to IAM & Admin from the top menu
4. Go to Service Accounts from the left menu
5. Click on Create Service Account
6. Give it a name (e.g. github-actions) and access rights (e.g. Cloud Run Admin & Service Account User)
7. Once created, click on the options next to the service account and select Manage Keys
8. Click Create New Key and select JSON
9. A file will be downloaded. Copy its content into a GitHub secret called `GCP_SERVICE_ACCOUNT_KEY`.
10. Create a branch, make a change, and open a pull request
11. Close the pull request, and inspect the workflow run in the Github UI 🎉

> <br>**Note:** If CGP complains about permissions, try the following: <br><br>
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Navigate to the IAM & Admin page.
3. Find the user github-actions@mlops-tutorial-project.iam.gserviceaccount.com in the list of members.
4. Click on the pencil icon next to the user to edit its permissions.
5. Add more permissions. (make sure it has Cloud Run Admin & Service Account User)
6. Save the changes.
After granting the required permissions, you can retry the deployment to Cloud Run.
