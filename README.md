# Relational to Neo4j Conversion

## Project Aim

The goal of this project is to convert relational dataset files (CSV format) into Neo4j-compatible Cypher queries. This involves creating nodes and relationships in a graph database, enabling better visualization and analysis of relational data using Neo4j.

## Dataset

The project uses the e-commerce dataset `commerce_data.csv`, which includes the following columns:
- `InvoiceNo`
- `StockCode`
- `Description`
- `Quantity`
- `InvoiceDate`
- `UnitPrice`
- `CustomerID`
- `Country`

This dataset represents transactional information, including details about products, invoices, and customers. The dataset is already included in the project directory.

## Implementations

There are two implementations for generating Cypher queries from the dataset:

### 1. Single File Implementation

- **File**: `toGraph.py`
- **Description**: This script generates Cypher queries that create both nodes and relationships in a single `.cypher` file. The file contains `MATCH` and `CREATE` statements for both node creation and relationship establishment in a combined format.

### 2. Separate Files Implementation

- **File**: `toGraph_separete.py`
- **Description**: This script generates two separate `.cypher` files:
  - `node.cypher`: Contains Cypher queries for creating nodes.
  - `edges.cypher`: Contains Cypher queries for creating relationships between nodes.

## How to Use

1. **Run the Script**:
   - To create a single file with both nodes and relationships, run:
     ```bash
     python toGraph.py
     ```
   - To create separate files for nodes and relationships, run:
     ```bash
     python toGraph_separete.py
     ```

2. **Check the Output**:
   - For the single file implementation, check the generated `output.cypher`.
   - For the separate files implementation, check the generated `node.cypher` and `edges.cypher`.

## Note:
   - The generated cypher files are already present on this folder to demonstarate the output. But delete them before trying the script.
