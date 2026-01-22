# Create a new project graph
import requests

API_KEY = "YOUR_API_KEY_HERE"
PROJECT_ID = "YOUR_PROJECT_ID_HERE"
GRAPH_NAME = "YOUR_GRAPH_NAME_HERE"

response = requests.post(
    "https://prodaus.api.airia.ai/v1/ProjectGraph",
    headers={
        "X-API-Key": API_KEY,
        "Content-Type": "application/json"
    },
    json={
        "name": GRAPH_NAME,
        "projectId": PROJECT_ID
    }
)

print("Status:", response.status_code)
print("Response:", response.text)