import bentoml
import numpy as np
from bentoml.models import BentoModel

demo_image = bentoml.images.PythonImage(python_version="3.11") \
    .python_packages("mlflow", "scikit-learn")

target_names = ['setosa', 'versicolor', 'virginica']

@bentoml.service(
    image=demo_image,
    resources={"cpu": "2"},
    traffic={"timeout": 10},
)
class IrisClassifier:
    bento_model = BentoModel("iris:latest")

    def __init__(self):
        self.model = bentoml.mlflow.load_model(self.bento_model)

    # Enable adaptive batching
    @bentoml.api(batchable=True)
    def predict(
        self,
        input_data: np.ndarray
    ) -> list[str]:
        print(f"batch_size: {len(input_data)}")
        preds = self.model.predict(input_data)
        return [target_names[i] for i in preds]
