import bentoml
import numpy as np

client = bentoml.SyncHTTPClient("http://localhost:3000")
pred = client.predict(np.array([[5.9, 3, 5.1, 1.8]])) # ['virginica']

print('prediction: ', pred)