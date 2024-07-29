"""FastAPI for serving a ML Model."""
from contextlib import asynccontextmanager
import pickle
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np


class IrisInput(BaseModel):
    sepal_length: float 
    sepal_width: float 
    petal_length: float
    petal_width: float

class IrisOutput(BaseModel):
    predicted_class: str
    predicted_probability: float


iris_resources = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    iris_resources["model"] = pickle.load(open('./resources/model.pkl', mode='r+b'))

    output_classes = {
        0: "Setosa",
        1: "Versicolour",
        2: "Virginica"
    }
    iris_resources["output_classes"] = output_classes
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def iris_info():
    return "API For IRIS Classification."

@app.post("/predict/")
def classify(iris_input: List[IrisInput]) -> List[IrisOutput]:
    """
    Classify iris from inputs

    Args:
        iris_input (List[IrisInput]): input features

    Returns:
        IrisOutput: The predicted class and probability for each input.
    """
    iris_output = []

    # Convert iris_input into an np.array
    iris_input_array = np.array([[iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width] for iris in iris_input])
    predictions = iris_resources["model"].predict_proba(iris_input_array)

    #Outputs will be the predicted output class and probability
    predicted_classes = [iris_resources["output_classes"][arg] for arg in np.argmax(predictions, axis=1)]
    predicted_probabilities = np.max(predictions, axis=1)

    for predicted_class, predicted_probability in zip(predicted_classes, predicted_probabilities):
        iris_output.append(
            IrisOutput(predicted_class=predicted_class, predicted_probability=round(predicted_probability,2))
        )

    return iris_output