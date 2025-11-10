import pandas as pd
import mlflow

model_uri = 'runs:/5abcf4be209a4a9b90e599a45d365c8b/iris_model'

pyfunc_model = mlflow.pyfunc.load_model(model_uri)
input_data = pyfunc_model.input_example

mlflow.models.predict(
    model_uri=model_uri,
    input_data=input_data,
    env_manager="uv",
)

# Make predictions
data = [
  [4.6, 3.6, 1, 0.2],
  [5.7, 4.4, 1.5, 0.4],
  [6.7, 3.1, 4.4, 1.4],
  [4.8, 3.4, 1.6, 0.2]
]

df = pd.DataFrame(data, columns=['col1', 'col2', 'col3', 'col4'])
print('Data for predictions')
print(df)

loaded_model = mlflow.pyfunc.load_model(model_uri)

print("=====")
preds = loaded_model.predict(pd.DataFrame(df))
print(preds)
print("=====")

