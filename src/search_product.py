from db_connection import conn

cursor = conn.cursor()

product_id = int(input("Enter Product ID: "))

cursor.execute(
    "SELECT * FROM products WHERE product_id = %s",
    (product_id,)
)

product = cursor.fetchone()

if product:
    print("\nProduct Found:")
    print(product)
else:
    print("\nProduct Not Found")

conn.close()