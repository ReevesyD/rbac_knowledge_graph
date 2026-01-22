# Get the number of nodes in the graph
import requests

GRAPH_ID = "YOUR_GRAPH_ID_HERE"
API_KEY = "YOUR_API_KEY_HERE"

response = requests.get(
    f"https://prodaus.api.airia.ai/v1/ProjectGraph/{GRAPH_ID}/nodes/count",
    headers={"X-API-Key": API_KEY}
)

print("Status:", response.status_code)
print("Node count:", response.text)