import mlflow

mlflow.set_tracking_uri("http://20.31.225.193")

def load_model(model_name: str, stage: str):
    model =mlflow.sklearn.load_model(f"models:/{model_name}/{stage}")
    return model

def get_features(model_name: str, stage: str):
    client = mlflow.tracking.MlflowClient()
    model_version = client.get_latest_versions(name=model_name, stages=[stage])[0]
    run_id = model_version.run_id
    run = client.get_run(run_id)
    features = run.data.params["features"]
    return features.split(", ")
