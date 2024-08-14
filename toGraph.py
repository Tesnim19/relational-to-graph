import csv

# File paths
csv_file_path = 'commerce_data.csv'  
output_path = 'output.cypher'

# track of created nodes to avoid duplicates
created_invoices = set()
created_products = set()
created_customers = set()

# Openning the CSV file 
with open(csv_file_path, 'r', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)

    with open(output_path, 'w') as output_file:
        # Loop through rows to create nodes
        for row in reader:
            # Create Invoice node if not already created
            if row['InvoiceNo'] not in created_invoices:
                output_file.write(
                    f"CREATE (i:Invoice {{invoiceno: '{row['InvoiceNo']}', "
                    f"invoicedate: '{row['InvoiceDate']}'}});\n"
                )
                created_invoices.add(row['InvoiceNo'])

            # Create Product node if not already created
            if row['StockCode'] not in created_products:
                output_file.write(
                    f"CREATE (p:Product {{stockcode: '{row['StockCode']}', "
                    f"description: '{row['Description']}', "
                    f"unitprice: {row['UnitPrice']}}});\n"
                )
                created_products.add(row['StockCode'])

            # Create Customer node if not already created
            if row['CustomerID'] not in created_customers:
                output_file.write(
                    f"CREATE (c:Customer {{customerid: '{row['CustomerID']}', "
                    f"country: '{row['Country']}'}});\n"
                )
                created_customers.add(row['CustomerID'])

        # Goes back to the beginning of the file to create relationships
        csvfile.seek(0)
        next(reader)  # Skips the header row

        # Loop through rows to create relationships
        for row in reader:
            output_file.write(
                f"MATCH (i:Invoice {{invoiceno: '{row['InvoiceNo']}'}}), "
                f"(p:Product {{stockcode: '{row['StockCode']}'}}), "
                f"(c:Customer {{customerid: '{row['CustomerID']}'}}) "
                f"CREATE (i)-[:CONTAINS {{quantity: {row['Quantity']}}}]->(p), "
                f"(i)-[:PURCHASED_BY]->(c);\n"
            )
