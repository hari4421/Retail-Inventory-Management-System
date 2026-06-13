# Retail Inventory Management System

## Overview

## Overview

Retail Inventory Management System is a Python-based application developed using Python, MySQL, and Pandas. The system is designed to manage and track inventory records efficiently through CRUD operations (Create, Read, Update, Delete). It allows users to import product data from CSV files, store and manage data in a MySQL database, and perform inventory management through a simple menu-driven interface. This project demonstrates database connectivity, data handling, and inventory management concepts using Python.

## Features

* View Products
* Search Products
* Add Products
* Update Products
* Delete Products
* Import Data from CSV
* MySQL Database Connectivity

## Technologies Used

* Python
* MySQL
* Pandas
* MySQL Connector

## How the Project Works

Step 1:
Create MySQL Database (`inventory_db`)


Step 2:
Run `inventory_db.sql` to create the `products` table


Step 3:
Prepare `inventory_dataset.csv` containing product information


Step 4:
Run `upload_data.py` to upload CSV data into MySQL


Step 5:
Run `main.py`


Step 6:
Choose an option from the menu

1 → View Products

2 → Search Product

3 → Add Product

4 → Update Product

5 → Delete Product

6 → Exit


Step 7:
Database gets updated automatically based on user operations


Step 8:
View results in MySQL Workbench or through the application

## Requirements

* pandas
* mysql-connector-python

## Run the Project

```bash
python src/main.py
```

