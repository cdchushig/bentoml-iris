import bentoml
from datetime import date

model_uri = 'runs:/6b9db8fe70b04428a9e8fc0a9b8b260d/iris_model'

bento_model = bentoml.mlflow.import_model(
    'iris_nov',
    model_uri=model_uri,
    labels={
        "team": "bento",
        "stage": "dev",
        "accuracy": 1.0,
        "training_date": str(date.today())
    }
)
