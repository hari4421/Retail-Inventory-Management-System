from db_connection import conn

cursor = conn.cursor()

product_id = int(input("Enter Product ID: "))
new_quantity = int(input("Enter New Quantity: "))

query = """
UPDATE products
SET quantity = %s
WHERE product_id = %s
"""

cursor.execute(query, (new_quantity, product_id))

conn.commit()

print("Product Updated Successfully!")

conn.close()