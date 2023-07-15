import mlflow
import pandas as pd
import plotly.express as px

from turbine_power.model_utils import get_feature_names, load_model

def run_inference():
    """This function is only used for illustration purposes and runs 
    the same code as in the notebook 03-load-model-for-inference.ipynb"""

    print("Loading model...")
    stage = "production"
    model_name = "my-epic-model"
    mlflow.set_tracking_uri("http://20.4.198.104:5000")
    model = load_model(model_name, stage)
    features = get_feature_names(model_name, stage)

    print("Loading data...")
    data_url = "https://raw.githubusercontent.com/ykerus/experiment-tracking-with-mlflow/main/data/turbine-data.csv"
    data = pd.read_parquet(data_url).set_index("timestamp")
    data.index = pd.to_datetime(data.index)

    print("Preparing data...")
    data_without_na = data.dropna()
    X = data_without_na[features]
    y = data_without_na["active_power"]

    print("Running inference...")
    data.loc[X.index, "predictions"] = model.predict(X)

    print("Evaluating and logging to MLflow...")
    score = model.score(X, y)
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
