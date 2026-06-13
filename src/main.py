from db_connection import conn

cursor = conn.cursor()

while True:
    print("\n===== Retail Inventory Management System =====")
    print("1. View Products")
    print("2. Search Product")
    print("3. Add Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()

        print("\nProducts List:\n")
        for row in rows:
            print(row)

    elif choice == "2":
        product_id = int(input("Enter Product ID: "))

        cursor.execute(
            "SELECT * FROM products WHERE product_id=%s",
            (product_id,)
        )

        product = cursor.fetchone()

        if product:
            print(product)
        else:
            print("Product Not Found")

    elif choice == "3":
        product_id = int(input("Enter Product ID: "))
        product_name = input("Enter Product Name: ")
        category = input("Enter Category: ")
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))
        supplier = input("Enter Supplier: ")

        cursor.execute(
            """
            INSERT INTO products
            (product_id, product_name, category,
             quantity, price, supplier)
            VALUES (%s,%s,%s,%s,%s,%s)
            """,
            (
                product_id,
                product_name,
                category,
                quantity,
                price,
                supplier
            )
        )

        conn.commit()

        print("Product Added Successfully")

    elif choice == "4":
        product_id = int(input("Enter Product ID: "))
        quantity = int(input("Enter New Quantity: "))

        cursor.execute(
            """
            UPDATE products
            SET quantity=%s
            WHERE product_id=%s
            """,
            (quantity, product_id)
        )

        conn.commit()

        print("Product Updated Successfully")

    elif choice == "5":
        product_id = int(input("Enter Product ID: "))

        cursor.execute(
            "DELETE FROM products WHERE product_id=%s",
            (product_id,)
        )

        conn.commit()

        print("Product Deleted Successfully")

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")

conn.close()