# Delete all nodes and relationships from the graph
import requests

GRAPH_ID = "YOUR_GRAPH_ID_HERE"
API_KEY = "YOUR_API_KEY_HERE"

response = requests.post(
    f"https://prodaus.api.airia.ai/v1/ProjectGraph/{GRAPH_ID}/cypher",
    headers={
        "X-API-Key": API_KEY,
        "Content-Type": "application/json"
    },
    json={
        "query": "MATCH (n) DETACH DELETE n",
        "readonly": False
    }
)

print("Status:", response.status_code)
print("Response:", response.text)