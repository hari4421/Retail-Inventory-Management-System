# Retail-Inventory-Management-System
Retail Inventory Management System developed using Python, MySQL, and Pandas. Features include product inventory management with CRUD operations (Add, View, Search, Update, Delete), CSV data import, database connectivity, and a menu-driven interface for efficient inventory tracking and management.

## Features

* View all products
* Search products by Product ID
* Add new products
* Update product quantity
* Delete products
* Import inventory data from CSV
* MySQL database integration
* Menu-driven console application

## Technologies Used

* Python
* MySQL
* Pandas
* MySQL Connector

## Project Structure

Retail-Inventory-Management-System/

├── data/
│   └── inventory_dataset.csv

├── database/
│   └── inventory_db.sql

├── src/
│   ├── db_connection.py
│   ├── upload_data.py
│   ├── view_products.py
│   ├── search_product.py
│   ├── add_product.py
│   ├── update_product.py
│   ├── delete_product.py
│   └── main.py

├── requirements.txt
├── README.md
└── .gitignore

## Installation

1. Clone or download the project.
2. Create a MySQL database named `inventory_db`.
3. Execute `database/inventory_db.sql`.
4. Update MySQL credentials in `src/db_connection.py`.
5. Install dependencies:

pip install -r requirements.txt

## Run the Project

Upload CSV Data:

python src/upload_data.py

Run Main Application:

python src/main.py

## Sample Operations

* View Products
* Search Product
* Add Product
* Update Product Quantity
* Delete Product
* Exit Application

## Skills Demonstrated

* Python Programming
* SQL Database Management
* CRUD Operations
* Data Handling with Pandas
* Database Connectivity
* Project Structure and Documentation

## Author

Hari Krishna
