import pandas as pd
from db_connection import conn

# Read CSV file
df = pd.read_csv("data/inventory_dataset.csv")
print("Reading CSV successful")

cursor = conn.cursor()

# Insert data into table
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO products
        (product_id, product_name, category, quantity, price, supplier)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()

print("Data Uploaded Successfully")
conn.close()