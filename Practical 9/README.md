Practical 9 – E-Commerce ETL Pipeline with SQL Database

Aim

To perform an end-to-end ETL process for e-commerce data using Pandas and SQLite, including data extraction, cleaning, transformation, SQL loading, reporting, and incremental data loading.

Libraries Used

- Pandas – for data extraction, cleaning, transformation, merging, and reporting
- SQLite3 – for creating and managing the SQL database

Practical Description

This practical demonstrates a complete e-commerce ETL pipeline. Historical customer, product, order, and payment data is created as CSV files, extracted using Pandas, cleaned and transformed, and then loaded into an SQLite database.

The practical also generates sales reports, handles newly arriving orders, performs incremental loading, and produces a final updated sales report.

1. Create Historical E-Commerce Data

Four datasets are created:
- Customers – Customer ID, name, and city
- Products – Product ID, product name, category, and price
- Orders – Order ID, customer ID, product ID, quantity, and order date
- Payments – Payment ID, order ID, payment mode, and payment status

The datasets are saved as:
customers.csv
products.csv
orders.csv
payments.csv

2. Extract Data from CSV

The four CSV files are read using Pandas read_csv() and displayed.

3. Data Cleaning

The data is cleaned by:
- Removing duplicate records.
- Filling missing customer cities with Unknown.
- Filling missing product categories with Unknown.
- Converting Order_Date into proper date format.
- Removing orders with quantity less than or equal to zero.
- Standardizing payment status using title case.

4. Data Transformation

Orders are joined with product information using Product_ID.
A new Total_Amount column is calculated using:
Total_Amount = Quantity × Price
The transformed data is stored in sales_df.

5. Connect to SQL Database

An SQLite database named:
ecommerce.db
is created and connected using SQLite3.

6. Load Data into SQL Database

The following tables are created in the database:
- Customers
- Products
- Orders
- Payments
- Sales_Report
The cleaned and transformed data is loaded into these tables.

7. Generate Sales Report

A SQL query groups sales by product category and calculates:
- Total Quantity
- Total Sales
The report is ordered by total sales in descending order.

8. Customer Sales Report

A SQL query joins the Customers, Orders, and Sales_Report tables to calculate the total spending of each customer.
The report contains:
- Customer Name
- City
- Total Spending
Customers are ordered by total spending in descending order.

9. Handle Newly Arriving Data

Two new orders are created with Order IDs 1006 and 1007.
These represent newly arriving e-commerce records.

10. Incremental Data Loading

The existing Order IDs are retrieved from the SQL database.
Only orders whose IDs are not already present are selected for incremental loading.
The new records are then appended to the Orders table.

11. Update Sales Data

The newly loaded orders are joined with the product data.
Their Total_Amount is calculated and the resulting data is stored in:
New_Sales

12. Final Sales Report

The original sales data and newly arriving sales data are combined.
The final report calculates:
- Total Quantity by category
- Total Sales by category

13. Verify Database

The practical retrieves and displays the names of all tables available in the SQLite database.
The database connection is then closed.
How to Run
Run the notebook cells in order.
The complete ETL workflow is:
Historical E-Commerce Data
          ↓
      CSV Files
          ↓
       Extract
          ↓
     Data Cleaning
          ↓
    Transformation
          ↓
    SQLite Database
          ↓
    Sales Reports
          ↓
 Newly Arriving Orders
          ↓
 Incremental Loading
          ↓
    Final Sales Report
          ↓
 Database Verification

Result

The e-commerce data is successfully extracted from CSV files, cleaned and transformed using Pandas, loaded into an SQLite database, and used to generate category-wise and customer-wise sales reports. Newly arriving orders are identified and loaded incrementally, after which the final sales report is generated.

Conclusion

This practical demonstrates a complete e-commerce ETL pipeline using Pandas and SQLite. It covers data extraction, cleaning, transformation, database loading, SQL reporting, incremental data loading, and final database verification


