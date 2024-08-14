import csv

# File paths
csv_file_path = 'commerce_data.csv'  
nodes_output_path = 'nodes.cypher'
edges_output_path = 'edges.cypher'

# Open the CSV file with utf-8-sig encoding
with open(csv_file_path, 'r', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)

    # Create nodes.cypher to store node creation queries
    with open(nodes_output_path, 'w') as nodes_file:
        # Create edges.cypher to store relationship creation queries
        with open(edges_output_path, 'w') as edges_file:
            for row in reader:
                # Create Invoice node
                nodes_file.write(
                    f"CREATE (i:Invoice {{invoiceno: '{row['InvoiceNo']}', "
                    f"invoicedate: '{row['InvoiceDate']}'}});\n"
                )

                # Create Product node
                nodes_file.write(
                    f"CREATE (p:Product {{stockcode: '{row['StockCode']}', "
                    f"description: '{row['Description']}', "
                    f"unitprice: {row['UnitPrice']}}});\n"
                )

                # Create Customer node
                nodes_file.write(
                    f"CREATE (c:Customer {{customerid: '{row['CustomerID']}', "
                    f"country: '{row['Country']}'}});\n"
                )

                # Match nodes and create relationships
                edges_file.write(
                    f"MATCH (i:Invoice {{invoiceno: '{row['InvoiceNo']}'}}), "
                    f"(p:Product {{stockcode: '{row['StockCode']}'}}), "
                    f"(c:Customer {{customerid: '{row['CustomerID']}'}}) "
                    f"CREATE (i)-[:CONTAINS {{quantity: {row['Quantity']}}}]->(p), "
                    f"(i)-[:PURCHASED_BY]->(c);\n"
                )
