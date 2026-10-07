"""
Practical 10: Mini Project - End-to-End Data Engineering Solution

Design and implement an end-to-end data engineering solution including:
1. Data ingestion
2. Data cleaning
3. Data transformation
4. Data storage
5. Data warehouse design
6. Reporting
"""

import os
import sqlite3
import pandas as pd


# ============================================================
# 1. DATA INGESTION
# ============================================================

print("=" * 60)
print("PRACTICAL 10 - END-TO-END DATA ENGINEERING MINI PROJECT")
print("=" * 60)

os.makedirs("data", exist_ok=True)
os.makedirs("output", exist_ok=True)

# Sample source data
customers_data = {
    "Customer_ID": [101, 102, 103, 104, 105],
    "Customer_Name": ["Amit", "Riya", "Neha", "Rahul", "Sneha"],
    "City": ["Mumbai", "Pune", "Delhi", "Mumbai", None]
}

products_data = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Laptop", "Phone", "Headphones", "Keyboard", "Mouse"],
    "Category": ["Electronics", "Electronics", "Accessories", "Accessories", "Accessories"],
    "Price": [60000, 30000, 2000, 1500, 800]
}

orders_data = {
    "Order_ID": [1001, 1002, 1003, 1004, 1005, 1005],
    "Customer_ID": [101, 102, 103, 104, 105, 105],
    "Product_ID": [1, 2, 3, 4, 5, 5],
    "Quantity": [1, 2, 3, 2, 4, 4],
    "Order_Date": [
        "2026-09-01",
        "2026-09-02",
        "2026-09-03",
        "2026-09-04",
        "2026-09-05",
        "2026-09-05"
    ]
}

payments_data = {
    "Payment_ID": [501, 502, 503, 504, 505, 506],
    "Order_ID": [1001, 1002, 1003, 1004, 1005, 1005],
    "Payment_Mode": ["UPI", "Card", "Cash", "UPI", "Card", "Card"],
    "Payment_Status": ["Paid", "Paid", "Paid", "Pending", "Paid", "Paid"]
}

# Write source files
pd.DataFrame(customers_data).to_csv("data/customers.csv", index=False)
pd.DataFrame(products_data).to_csv("data/products.csv", index=False)
pd.DataFrame(orders_data).to_csv("data/orders.csv", index=False)
pd.DataFrame(payments_data).to_csv("data/payments.csv", index=False)

print("\nSource files created successfully.")


# ============================================================
# 2. EXTRACT / INGEST DATA
# ============================================================

customers = pd.read_csv("data/customers.csv")
products = pd.read_csv("data/products.csv")
orders = pd.read_csv("data/orders.csv")
payments = pd.read_csv("data/payments.csv")

print("\n--- Customers ---")
print(customers)

print("\n--- Products ---")
print(products)

print("\n--- Orders ---")
print(orders)

print("\n--- Payments ---")
print(payments)


# ============================================================
# 3. DATA CLEANING
# ============================================================

print("\n" + "=" * 60)
print("DATA CLEANING")
print("=" * 60)

# Fill missing city
customers["City"] = customers["City"].fillna("Unknown")

# Remove duplicate orders and payments
orders = orders.drop_duplicates()
payments = payments.drop_duplicates()

# Remove invalid quantities
orders = orders[orders["Quantity"] > 0].copy()

# Convert order date to datetime
orders["Order_Date"] = pd.to_datetime(orders["Order_Date"])

# Standardize text fields
customers["Customer_Name"] = customers["Customer_Name"].str.title()
customers["City"] = customers["City"].str.title()
payments["Payment_Status"] = payments["Payment_Status"].str.title()

print("\nCleaned Customers:")
print(customers)

print("\nCleaned Orders:")
print(orders)

print("\nCleaned Payments:")
print(payments)


# ============================================================
# 4. DATA TRANSFORMATION
# ============================================================

print("\n" + "=" * 60)
print("DATA TRANSFORMATION")
print("=" * 60)

# Join orders with products
sales = orders.merge(
    products,
    on="Product_ID",
    how="left"
)

# Calculate total amount
sales["Total_Amount"] = sales["Quantity"] * sales["Price"]

# Add payment information
sales = sales.merge(
    payments[["Order_ID", "Payment_Mode", "Payment_Status"]],
    on="Order_ID",
    how="left"
)

# Add customer information
sales = sales.merge(
    customers[["Customer_ID", "Customer_Name", "City"]],
    on="Customer_ID",
    how="left"
)

# Select final transformed columns
sales = sales[
    [
        "Order_ID",
        "Order_Date",
        "Customer_ID",
        "Customer_Name",
        "City",
        "Product_ID",
        "Product_Name",
        "Category",
        "Quantity",
        "Price",
        "Total_Amount",
        "Payment_Mode",
        "Payment_Status"
    ]
]

print("\nTransformed Sales Data:")
print(sales)


# ============================================================
# 5. DATA WAREHOUSE DESIGN
# ============================================================

print("\n" + "=" * 60)
print("DATA WAREHOUSE DESIGN")
print("=" * 60)

# Star schema:
# Dimension tables:
#   dim_customer
#   dim_product
#   dim_date
# Fact table:
#   fact_sales

dim_customer = customers[
    ["Customer_ID", "Customer_Name", "City"]
].drop_duplicates()

dim_product = products[
    ["Product_ID", "Product_Name", "Category", "Price"]
].drop_duplicates()

dim_date = sales[["Order_Date"]].drop_duplicates().copy()
dim_date["Date_ID"] = dim_date["Order_Date"].dt.strftime("%Y%m%d").astype(int)
dim_date["Year"] = dim_date["Order_Date"].dt.year
dim_date["Month"] = dim_date["Order_Date"].dt.month
dim_date["Day"] = dim_date["Order_Date"].dt.day

dim_date = dim_date[
    ["Date_ID", "Order_Date", "Year", "Month", "Day"]
]

fact_sales = sales.copy()
fact_sales["Date_ID"] = fact_sales["Order_Date"].dt.strftime("%Y%m%d").astype(int)

fact_sales = fact_sales[
    [
        "Order_ID",
        "Date_ID",
        "Customer_ID",
        "Product_ID",
        "Quantity",
        "Total_Amount",
        "Payment_Status"
    ]
]

print("\nDimension - Customer:")
print(dim_customer)

print("\nDimension - Product:")
print(dim_product)

print("\nDimension - Date:")
print(dim_date)

print("\nFact - Sales:")
print(fact_sales)


# ============================================================
# 6. DATA STORAGE - SQLITE DATA WAREHOUSE
# ============================================================

print("\n" + "=" * 60)
print("LOADING DATA INTO SQLITE DATA WAREHOUSE")
print("=" * 60)

database_path = "output/data_warehouse.db"

conn = sqlite3.connect(database_path)

dim_customer.to_sql("dim_customer", conn, if_exists="replace", index=False)
dim_product.to_sql("dim_product", conn, if_exists="replace", index=False)
dim_date.to_sql("dim_date", conn, if_exists="replace", index=False)
fact_sales.to_sql("fact_sales", conn, if_exists="replace", index=False)

print(f"\nData warehouse created: {database_path}")


# ============================================================
# 7. REPORTING
# ============================================================

print("\n" + "=" * 60)
print("REPORTING")
print("=" * 60)

# Category-wise sales report
category_report = pd.read_sql_query(
    """
    SELECT
        p.Category,
        SUM(f.Quantity) AS Total_Quantity,
        ROUND(SUM(f.Total_Amount), 2) AS Total_Sales
    FROM fact_sales f
    JOIN dim_product p
        ON f.Product_ID = p.Product_ID
    GROUP BY p.Category
    ORDER BY Total_Sales DESC;
    """,
    conn
)

print("\nCategory-wise Sales Report:")
print(category_report)

# Customer-wise sales report
customer_report = pd.read_sql_query(
    """
    SELECT
        c.Customer_Name,
        c.City,
        ROUND(SUM(f.Total_Amount), 2) AS Total_Spending
    FROM fact_sales f
    JOIN dim_customer c
        ON f.Customer_ID = c.Customer_ID
    GROUP BY c.Customer_ID, c.Customer_Name, c.City
    ORDER BY Total_Spending DESC;
    """,
    conn
)

print("\nCustomer-wise Sales Report:")
print(customer_report)

# Save reports
category_report.to_csv("output/category_sales_report.csv", index=False)
customer_report.to_csv("output/customer_sales_report.csv", index=False)


# ============================================================
# 8. DATA QUALITY CHECK
# ============================================================

print("\n" + "=" * 60)
print("DATA QUALITY CHECK")
print("=" * 60)

print("Missing values in fact table:")
print(fact_sales.isnull().sum())

print("\nDuplicate fact records:")
print(fact_sales.duplicated().sum())

print("\nTotal fact records:", len(fact_sales))


# ============================================================
# 9. VERIFY DATA WAREHOUSE
# ============================================================

print("\n" + "=" * 60)
print("DATA WAREHOUSE TABLES")
print("=" * 60)

tables = pd.read_sql_query(
    "SELECT name FROM sqlite_master WHERE type='table';",
    conn
)

print(tables)

conn.close()

print("\n" + "=" * 60)
print("ETL PIPELINE COMPLETED SUCCESSFULLY")
print("=" * 60)
print("\nGenerated files:")
print("1. output/data_warehouse.db")
print("2. output/category_sales_report.csv")
print("3. output/customer_sales_report.csv")
