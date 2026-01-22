# Add data to the graph using Cypher queries
import requests

GRAPH_ID = "YOUR_GRAPH_ID_HERE"
API_KEY = "YOUR_API_KEY_HERE"

# Example: Create a node
# Replace with your own Cypher query
query = "CREATE (n:Node {name: 'Example'}) RETURN n"

response = requests.post(
    f"https://prodaus.api.airia.ai/v1/ProjectGraph/{GRAPH_ID}/cypher",
    headers={
        "X-API-Key": API_KEY,
        "Content-Type": "application/json"
    },
    json={
        "query": query,
        "readonly": False
    }
)

print("Status:", response.status_code)
print("Response:", response.text)