# Knowledge Graph API Examples

Simple Python scripts demonstrating how to interact with the Airia Knowledge Graph API.

## Why Knowledge Graphs?

Knowledge graphs are ideal for storing and querying relationship-based data using nodes and edges. They excel at traversing connections and finding patterns across complex networks.

**Common use cases:**
- **Social networks** - model friendships, posts, likes, memberships
- **Supply chain** - track products, suppliers, warehouses, shipments
- **Healthcare** - connect genes, proteins, diseases, treatments
- **Fraud detection** - analyse account relationships and transaction patterns
- **Recommendations** - link users, products, purchases, reviews
- **Access control** - manage employees, roles, permissions (like our RBAC demo)
- **IoT systems** - map sensors, devices, locations, connections
- **Research** - connect authors, papers, citations, institutions

## Setup

Install required dependencies:
```bash
pip install requests openpyxl
```

> **Note:** `openpyxl` is only needed for the demo scripts that work with Excel files

Update the placeholder values in each script:
- `YOUR_API_KEY_HERE`
- `YOUR_GRAPH_ID_HERE`
- `YOUR_PROJECT_ID_HERE`

## Basic API Scripts

| Script | Description |
|--------|-------------|
| `create_graph.py` | Create a new project graph |
| `get_graph.py` | Retrieve graph information |
| `get_nodes.py` | Get node count in a graph |
| `clear_graph.py` | Delete all nodes and relationships |
| `add_data.py` | Execute custom Cypher queries against the graph |

## Employee RBAC Demo

A complete example showing how to model employee access control in a knowledge graph.

### Step 1: Generate Demo Data
```bash
python demo_create_data.py
```
Creates `employee_rbac_demo.xlsx` with:
- 50 employees across 10 departments
- 100 RBAC groups
- ~2,000 group memberships (avg 40 groups per employee)

### Step 2: Load into Graph
```bash
python demo_populate_graph.py
```
Populates your knowledge graph with:
- Employee nodes with personal details
- Department nodes
- RBAC group nodes
- Relationships: `WORKS_IN` and `MEMBER_OF`

## Graph Schema

```
(Employee)-[:WORKS_IN]->(Department)
(Employee)-[:MEMBER_OF]->(RBACGroup)
```

## API Endpoint

All scripts use: `https://prodaus.api.airia.ai/v1/ProjectGraph`