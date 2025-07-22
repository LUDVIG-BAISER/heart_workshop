# test_client.py
import requests

response = requests.post(
    "http://127.0.0.1:8000/predict",
    json={"path": "heart_test.csv"}
)

print(response.status_code)
print(response.json())
