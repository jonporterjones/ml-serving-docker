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

## Docker setup

### push image to ecr
aws ecr create-repository --repository-name ml-serving-docker
docker tag ml-serving-docker-image <your-account-id>.dkr.ecr.us-east-2.amazonaws.com/ml-serving-docker

Login to ecr
aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin <your-account-id>.dkr.ecr.us-east-2.amazonaws.com
docker push <your-account-id>.dkr.ecr.us-east-2.amazonaws.com/ml-serving-docker

Done!

## ECS

Create cluster for Fargate services
Create task definition for fargate - this will refer to the docker image uri - did this in console without JSON
Create the service in your cluster using the task definition - it did all the VPC/Subnet stuff automatically
Careful with the architecture of your docker container and ecs service - make sure they align

## Networking

My VPC/Subnets route to an Internet Gateway
Simply adding an inbound rule to my security group from my IP over port 8000 allowed traffic in.

Works




