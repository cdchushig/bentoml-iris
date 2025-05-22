iris-bentoml
====

Crear cuenta en bentoml:

https://www.bentoml.com/

Login en bentouml desde ordenador local:

```shell
bentoml cloud login
```

Instalar librerías Python:
```shell
pip install bentoml mlflow scikit-learn
```

Iniciar MLflow tracking server:
```shell
mlflow server --host 127.0.0.1 --port 8080
```

Verify the model is saved to the Model Store:
```shell
bentoml models list
```

Serve the model using the BentoML CLI:
```shell
bentoml serve bentoml_service.py:IrisClassifier --port=3001
bentoml serve bentoml_service_advanced.py:IrisClassifier --port=3002
bentoml serve bentoml_service_multiple.py:IrisClassifier --port=3003
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


Inspect the OpenAPI documentation to see the required schema for your service:
```shell
curl localhost:3000/docs.json
```

Deploying to Production

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
