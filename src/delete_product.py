from db_connection import conn

cursor = conn.cursor()

product_id = int(input("Enter Product ID to Delete: "))

query = "DELETE FROM products WHERE product_id = %s"

cursor.execute(query, (product_id,))

conn.commit()

print("Product Deleted Successfully!")

conn.close()