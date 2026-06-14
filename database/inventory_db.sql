-- Create Database
CREATE DATABASE inventory_db;

-- Use Database
USE inventory_db;

-- Create Products Table
CREATE TABLE products (
product_id INT PRIMARY KEY,
product_name VARCHAR(100),
category VARCHAR(50),
quantity INT,
price DECIMAL(10,2),
supplier VARCHAR(100)
);

-- Verify Database and Table
SHOW DATABASES;
SHOW TABLES;
DESCRIBE products;

-- Sample Queries Used in the Project

SELECT * FROM products;

SELECT COUNT(*) FROM products;

SELECT * FROM products
WHERE product_id = 1;

-- UPDATE products
-- SET quantity = 20
-- WHERE product_id = 1;

-- DELETE FROM products
-- WHERE product_id = 3;
