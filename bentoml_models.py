import bentoml
from datetime import date

model_uri = 'runs:/ace812f2413e41189a06c89659ac1b51/iris_model'

bento_model = bentoml.mlflow.import_model(
    'iris',
    model_uri=model_uri,
    labels={
        "team": "bento",
        "stage": "dev",
        "accuracy": 1.0,
        "training_date": str(date.today())
    }
)