"""This module is only used for illustration purposes and runs 
the same code as in the notebook 03-load-model-for-inference.ipynb"""
    
import mlflow
import pandas as pd
import plotly.express as px

from turbine_power.model_utils import get_feature_names, load_model

def run_inference():
    
    stage = "production"
    model_name = "turbine-model"
    print(f"Loading model '{model_name}' from stage '{stage}'...")
    mlflow.set_tracking_uri("http://20.4.198.104:5000")
    model = load_model(model_name, stage)
    features = get_feature_names(model_name, stage)

    print("Loading data...")
    data_path = "../data/turbine-data.csv"
    data = pd.read_csv(data_path).set_index("timestamp")
    data.index = pd.to_datetime(data.index)

    print(f"Preparing data for features: {features}")
    data_without_na = data.dropna()
    X = data_without_na[features]
    y = data_without_na["active_power"]

    print("Running inference...")
    data.loc[X.index, "predictions"] = model.predict(X)

    print("Evaluating...")
    score = model.score(X, y)
    print(f"Logging score to MLflow: {score}")
    mlflow.log_metric("R2_score", score)

    print("Plotting and logging to MLflow...")
    plot_start = pd.Timestamp("2018-12-15")
    fig = px.line(
        data[plot_start:],
        y=["active_power", "predictions"]
    )
    mlflow.log_figure(fig, "predictions.html")
    
    print("Done! 🎉")
    
    
if __name__ == "__main__":
    run_inference()
