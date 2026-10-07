Practical 10 – End-to-End Data Engineering Mini Project

Aim

To design and implement an end-to-end data engineering solution including data ingestion, cleaning, transformation, storage, data warehouse design, and reporting.

Libraries Used

- Pandas – for data ingestion, cleaning, transformation, and reporting
- SQLite3 – for data storage and data warehouse implementation
- OS – for creating required directories

Practical Description

This mini project implements a complete e-commerce data engineering pipeline using Python, Pandas, and SQLite.
The pipeline starts with sample customer, product, order, and payment data. The data is ingested from CSV files, cleaned and transformed, loaded into a SQLite-based data warehouse, and finally used to generate reports.

1. Data Ingestion

The program creates and stores four source datasets:
- customers.csv
- products.csv
- orders.csv
- payments.csv

The CSV files are then read using Pandas.
Customers

Contains:
- Customer ID
- Customer Name
- City

Products

Contains:

- Product ID
- Product Name
- Category
- Price

Orders

Contains:

- Order ID
- Customer ID
- Product ID
- Quantity
- Order Date

Payments

Contains:

- Payment ID
- Order ID
- Payment Mode
- Payment Status

2. Data Cleaning

The program performs the following cleaning operations:
- Missing customer cities are replaced with Unknown.
- Duplicate orders and payment records are removed.
- Orders with invalid quantities are removed.
- Order dates are converted to datetime format.
- Customer names and cities are standardized.
- Payment status values are standardized.

3. Data Transformation

The cleaned datasets are combined using joins.
Orders are joined with product information to calculate:
Total_Amount = Quantity × Price
Customer and payment information is also added to create the final transformed sales dataset.

4. Data Warehouse Design

A star schema is designed for the data warehouse.
The warehouse contains the following tables:
Dimension Tables
- dim_customer
- dim_product
- dim_date
Fact Table
- fact_sales
The fact_sales table stores sales measures and connects the dimension tables through their respective IDs.
The data warehouse structure is:
             dim_customer
                   |
                   |
dim_product — fact_sales — dim_date

5. Data Storage

An SQLite database is created as the data warehouse:
output/data_warehouse.db
The dimension and fact tables are loaded into the database using Pandas and SQLite.

6. Reporting

Two reports are generated from the data warehouse.
Category-wise Sales Report
The report calculates:
- Total Quantity
- Total Sales
for each product category.
It is saved as:
output/category_sales_report.csv
Customer-wise Sales Report
The report calculates:
- Customer Name
- City
- Total Spending
for each customer.
It is saved as:
output/customer_sales_report.csv

7. Data Quality Check

The program checks:
- Missing values in the fact table
- Duplicate fact records
- Total number of fact records
This helps verify the quality of the processed data before completing the pipeline.

8. Data Warehouse Verification

The program retrieves and displays all tables present in the SQLite database to verify that the data warehouse has been created successfully.
How to Run
Install Pandas if required:
pip install pandas
Run the Python program:
python practical_10.py
Process Flow
Source Data
    ↓
Data Ingestion
    ↓
Data Cleaning
    ↓
Data Transformation
    ↓
Data Warehouse Design
    ↓
SQLite Data Warehouse
    ↓
Data Quality Checks
    ↓
Reporting
    ↓
Final Reports
Generated Files
After running the program, the following files are generated:
data/
├── customers.csv
├── products.csv
├── orders.csv
└── payments.csv

output/
├── data_warehouse.db
├── category_sales_report.csv
└── customer_sales_report.csv

Result

The end-to-end data engineering pipeline is successfully implemented. The program ingests e-commerce data, cleans and transforms it, stores the processed data in a SQLite data warehouse using a star schema, performs data quality checks, and generates category-wise and customer-wise sales reports.

Conclusion

This mini project demonstrates a complete data engineering workflow using Python, Pandas, and SQLite. It covers the major stages of an ETL pipeline, including data ingestion, cleaning, transformation, storage, data warehouse design, validation, and reporting.
