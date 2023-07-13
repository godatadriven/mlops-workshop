from fastapi import FastAPI
from pydantic import BaseModel, Field
from turbine_power import model_utils
import uvicorn
import pandas as pd
from typing import List
import os

class InputData(BaseModel):
    wind_speed: List[float] = Field(examples=[[10, 11]])
    wind_direction: List[float] = Field(examples=[[45, 45]])
    is_curtailed: List[float] = Field(examples=[[False, False]])

stage = "production"
model_name = "my-epic-model"
model = model_utils.load_model(model_name, stage)
features = model_utils.get_features(model_name, stage)
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hi there! This is the root endpoint of the API. Try adding /docs to the URL to see the Swagger UI"}

@app.post("/predict")
async def predict(input_data: InputData):
    data = pd.DataFrame(input_data.dict())
    X = data[features]
    output = model.predict(X)
    return {"prediction": output.tolist()}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
