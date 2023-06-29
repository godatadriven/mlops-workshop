import mlflow
import pandas as pd
import plotly.express as px
import sklearn.pipeline

# Configure mlflow
mlflow.set_tracking_uri("http://20.31.89.132:5000")
mlflow.set_experiment("inference")

# Load model
model: sklearn.pipeline.Pipeline = mlflow.sklearn.load_model(
    "models:/my-epic-model/production"
)

# Load data
data_url = "https://raw.githubusercontent.com/dunnkers/experiment-tracking-with-mlflow/main/data/scada.parquet" # noqa
data = pd.read_parquet(data_url)

# Inference
data_without_na = data.dropna()
X = data_without_na[[
    "wind_speed",
    "wind_direction",
    "is_curtailed"
]]
y = data_without_na["active_power"]
data.loc[X.index, "predictions"] = model.predict(X)
score = model.score(X, y)
mlflow.log_metric("R2_score", score)

# Plot
plot_start = pd.Timestamp("2018-12-15")
fig = px.line(
    data[plot_start:],
    y=["active_power", "predictions"]
)
mlflow.log_figure(fig, "predictions.html")