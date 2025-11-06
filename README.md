bentoml-iris
====

This repository is part of the course of MLOPs for USFQ. To work with pipelines of ML, and the
deployment in production, we will use **BentoML**. BentoML is an open-source ML model serving
framework that helps developers package, deploy, and serve ML models in production easily and
efficiently.

First of all, the student has to create an account in bentoml, in the next URL:
https://www.bentoml.com/

### Getting ready

To install Python libraries:
```shell
pip install bentoml mlflow scikit-learn
```

Login in bentoml using local computer:
```shell
bentoml cloud login
```

To verify the model is saved to the Model Store:
```shell
bentoml models list
```

To start MLflow tracking server:
```shell
mlflow server --host 127.0.0.1 --port 8080
```

### Basic commands for bentoml

To serve the model using the BentoML CLI:
```shell
bentoml serve 04_bentoml_service.py:IrisClassifier --port=3001
```

Make requests by curl:

```shell
curl -X 'POST'   'http://localhost:3000/predict'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{
  "input_data": [[
    5.9, 3.0, 5.1, 1.8
  ]]
}'
```

```shell
curl -X 'POST'   'http://localhost:3000/predict'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{
  "input_data": [[
    5.9, 3.0, 5.1, 1.8
  ]]
}'
```
```shell
curl -X 'POST'   'http://localhost:3000/predict'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{
  "input_data": [[
    5.9, 3.0, 5.1, 1.8
  ]]
}'
```

```shell
curl -X 'POST'   'http://localhost:3002/v1/predict'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{
  "input_data": [[
    5.9, 3.0, 5.1, 1.8
  ]]
}'
```

```shell
curl -X 'POST'   'http://localhost:3002/v2/predict'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{
  "input_data": [[
    5.9, 3.0, 5.1, 1.8
  ]]
}'
```

```shell
curl -X 'POST'   'http://localhost:3002/predict_combined/predict'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{
  "input_data": [[
    5.9, 3.0, 5.1, 1.8
  ]]
}'
```

To inspect the OpenAPI documentation to see the required schema for your service:
```shell
curl localhost:3000/docs.json
```

To execute a server with batching requests:
```shell
bentoml serve bentoml_service_advanced.py:IrisClassifier --port=3002
```

To execute two endpoints and an ensemble prediction:
```shell
bentoml serve bentoml_service_multiple.py:IrisClassifier --port=3003
```

### Deploying to Production

BentoML provides multiple options for production deployment:

Containerization: Build an OCI-compliant image for your ML service for deployment on any container platform:
```shell
bentoml build
bentoml containerize iris_classifier:latest
```

Next steps: 

* Deploy to BentoCloud:
```shell
bentoml deploy iris_classifier:mmd2rarxb6fexe65 -n ${DEPLOYMENT_NAME}
```

* Update an existing deployment on BentoCloud:
```shell
bentoml deployment update --bento iris_classifier:mmd2rarxb6fexe65 ${DEPLOYMENT_NAME}
```

* Containerize your Bento with `bentoml containerize`:
```shell
bentoml containerize iris_classifier:mmd2rarxb6fexe65
```

* Push to BentoCloud with `bentoml push`:
    $ bentoml push iris_classifier:mmd2rarxb6fexe65 
