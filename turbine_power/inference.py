import mlflow
import pandas as pd
import plotly.express as px

from turbine_power.model_utils import get_features, load_model

# Load model
stage = "production"
model_name = "my-epic-model"
mlflow.set_tracking_uri("http://20.31.225.193")
model = load_model(model_name, stage)
features = get_features(model_name, stage)

# Load data
data_url = "https://raw.githubusercontent.com/ykerus/experiment-tracking-with-mlflow/main/data/scada.parquet" # noqa
data = pd.read_parquet(data_url)


# Prepare data
data_without_na = data.dropna()
X = data_without_na[features]
y = data_without_na["active_power"]

# Inference
data.loc[X.index, "predictions"] = model.predict(X)

# Evaluate
score = model.score(X, y)
mlflow.log_metric("R2_score", score)

# Plot
plot_start = pd.Timestamp("2018-12-15")
fig = px.line(
    data[plot_start:],
    y=["active_power", "predictions"]
)
mlflow.log_figure(fig, "predictions.html")
