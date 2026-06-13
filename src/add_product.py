from db_connection import conn

cursor = conn.cursor()

product_id = int(input("Enter Product ID: "))
product_name = input("Enter Product Name: ")
category = input("Enter Category: ")
quantity = int(input("Enter Quantity: "))
price = float(input("Enter Price: "))
supplier = input("Enter Supplier: ")

query = """
INSERT INTO products
(product_id, product_name, category, quantity, price, supplier)
VALUES (%s, %s, %s, %s, %s, %s)
"""

values = (
    product_id,
    product_name,
    category,
    quantity,
    price,
    supplier
)

cursor.execute(query, values)

conn.commit()

print("\nProduct Added Successfully!")

conn.close()