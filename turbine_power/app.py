"""API serving our turbine power prediction model from MLflow.

Run using: `python turbine_power/app.py`
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field
from turbine_power import model_utils
import uvicorn
import pandas as pd
from typing import List
import mlflow

mlflow.set_tracking_uri("http://20.4.198.104:5000")

class InputData(BaseModel):
    wind_speed: List[float] = Field(examples=[[10, 11]])
    wind_direction: List[float] = Field(examples=[[45, 45]])
    is_curtailed: List[float] = Field(examples=[[False, False]])

stage = "production"
model_name = "turbine-model"
model = model_utils.load_model(model_name, stage)
features = model_utils.get_feature_names(model_name, stage)
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hi there! This is the root endpoint of the API. Try adding /docs to the URL to see the Swagger UI"}

@app.post("/predict")
async def predict(input_data: InputData):
    data = pd.DataFrame(input_data.dict())
    X = data[features]
    
    # Exercise: use the model to make predictions
    # ...
    output = pd.Series(["TODO: implement me!"])  # replace this line
    
    return {"prediction": output.tolist()}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
