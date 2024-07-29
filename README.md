# ML Serving Docker

A simpled demonstration of serving a ML Model and an API in a Docker container.
Bonus if I can make a streamlit app to do data entry and prediction.
Double bonus if I can then host the container in AWS.

## API Inputs

The API expects inputs that are de-serializable as a pydantic model.  
Therefore inputs must be list of dictionaries:

[
  {"sepal_length": 7.2, "sepal_width": 3.6, "petal_length": 4.1, "petal_width": 5.0},
  {"sepal_length": 3.1, "sepal_width": 2.7, "petal_length": 0.1, "petal_width": 3.0}
]