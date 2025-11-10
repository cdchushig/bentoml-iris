import bentoml
from datetime import date

model_uri = 'runs:/7d441b63729f408a972cd2e02463e283/iris_model'

bento_model = bentoml.mlflow.import_model(
    'iris_nov_10',
    model_uri=model_uri,
    labels={
        "team": "bento",
        "stage": "dev",
        "accuracy": 1.0,
        "training_date": str(date.today())
    }
)
