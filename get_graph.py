# Get information about a project graph
import requests
import json

API_KEY = "YOUR_API_KEY_HERE"
PROJECT_ID = "YOUR_PROJECT_ID_HERE"

response = requests.get(
    "https://prodaus.api.airia.ai/v1/ProjectGraph",
    headers={"X-API-Key": API_KEY},
    params={"projectId": PROJECT_ID}
)

data = response.json()
print(json.dumps(data, indent=2))