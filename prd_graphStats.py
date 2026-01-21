import requests

def graph_stats(api_key):
    out = requests.get(
        "https://prodaus.api.airia.ai/v1/Graphs/project-graph-7795f113-9dfe-4ecc-be68-b4a17c0684d7/nodes/count",
        headers={"X-API-Key" : api_key}
    )
    print("Status Code:", out.status_code)
    print("Response:", out.text)

graph_stats()