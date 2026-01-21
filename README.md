# Knowledge Graph Management Scripts

This collection of Python scripts manages a Neo4j knowledge graph for organizational data, including employees, positions, departments, and RBAC groups.

## Graph Identification Scripts

These scripts help you identify and verify your knowledge graph:

### `prd_findGraphs.py`
Lists all available graphs in your Airia account. Use this to find your graph ID.

### `prd_graphStats.py`
Returns node count statistics for the specified graph. Useful for verifying data has been loaded.

## Data Population Scripts

These scripts populate the knowledge graph with organizational data from CSV files:

### `prd_findEmployees.py`
Reads `output.csv` and generates a Cypher query to create:
- Employee nodes (by user code)
- Position nodes and relationships
- Manager position relationships
- Department nodes and relationships

### `prd_findGroups.py`
Scans `output.csv` for all unique group names and generates a query to create RBACGroup nodes.

### `prd_populateGroups.py`
Reads `input.csv` and creates PART_OF relationships between employees and their RBAC groups. Includes retry logic and processes up to 4000 rows.

### `prd_cypher.py`
Utility module that executes Cypher queries against the Airia API. Used by all population scripts.

### `prd_main.py`
Orchestration script with three main functions:
- `addEmployees()` - Populate employee data
- `addGroups()` - Create RBAC groups
- `addRelationships()` - Link employees to groups

## Workflow

1. Run `prd_findGraphs.py` to identify your graph
2. Uncomment and run `addEmployees()` in `prd_main.py`
3. Uncomment and run `addGroups()` in `prd_main.py`
4. Uncomment and run `addRelationships()` in `prd_main.py`
5. Use `prd_graphStats.py` to verify data was loaded

## Requirements

- Python 3.x
- `requests` library
- CSV files: `output.csv` and `input.csv`
- Valid Airia API key (replace `akey-placeholder` in scripts)