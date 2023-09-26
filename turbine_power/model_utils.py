"""Some useful functions for working with MLflow models."""

from typing import List

import mlflow
import sklearn.pipeline
from mlflow.entities.model_registry import ModelVersion

mlflow.set_tracking_uri("http://20.4.198.104:5000")


def load_model(model_name: str, stage: str) -> sklearn.pipeline.Pipeline:
    model: sklearn.pipeline.Pipeline = mlflow.sklearn.load_model(
        f"models:/{model_name}/{stage}"
    )
    return model


def get_feature_names(model_name: str, stage: str) -> List[str]:
    """Get the feature names from the model metadata, given its name and stage."""

    client = mlflow.tracking.MlflowClient()
    latest_versions: List[ModelVersion] = client.get_latest_versions(
        name=model_name, stages=[stage]
    )
    model_version = latest_versions[0]
    run_id = model_version.run_id
    run = client.get_run(run_id)
    features: str = run.data.params["features"]
    return features.split(", ")
