import os
import mlflow

mlflow_tracking_uri = os.environ.get("MLFLOW_TRACKING_URI", "<fill in right before workshop>")
mlflow.set_tracking_uri(mlflow_tracking_uri)

mlflow.set_experiment("test_experiment")
mlflow.log_metric("metric", 1.0)