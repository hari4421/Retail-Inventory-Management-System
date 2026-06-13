from db_connection import conn

cursor = conn.cursor()

cursor.execute("SELECT * FROM products")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()