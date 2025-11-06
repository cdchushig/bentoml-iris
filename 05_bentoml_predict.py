import numpy as np
import bentoml

# Load the latest version of iris model:
iris_model = bentoml.mlflow.load_model("iris_nov:latest")

# Alternatively, load the model by specifying the model tag
# iris_model = bentoml.mlflow.load_model("iris:hu5d7xxs3oxmnuqj")

input_data = np.array([[5.9, 3, 5.1, 1.8]])
res = iris_model.predict(input_data)
print(res)