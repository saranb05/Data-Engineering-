Practical 8 – Data Processing using PySpark

Aim

To perform data processing and analysis using PySpark on a sample sales dataset.

Libraries Used

- PySpark – for distributed data processing and analysis
- Spark SQL functions – for filtering, grouping, aggregation, joins, and average calculations

Practical Description

This practical demonstrates basic data processing operations using PySpark. A sample sales dataset is created and processed using a Spark DataFrame.
The practical performs filtering, grouping, aggregation, duplicate removal, joining of two datasets, and average sales calculation.

1. Create Spark Session

A Spark session is created using:
SparkSession.builder.appName("Practical8").getOrCreate()

2. Create Sample Sales Dataset

A sample sales dataset is created with the following columns:
- Product_ID
- Product
- Category
- Sales

The dataset contains products from the Electronics, Furniture, and Stationery categories.
The data is written as a CSV dataset to:
/content/sales_csv

3. Read CSV Dataset

The CSV dataset is read using Spark with headers and automatic schema inference enabled.
The complete dataset is displayed using show().

4. Display Dataset Schema

The schema of the Spark DataFrame is displayed using:
df.printSchema()

5. Filtering

Products with sales greater than 5000 are selected using a filter condition:
col("Sales") > 5000

6. Grouping

The number of products in each category is calculated using:
groupBy("Category").count()

7. Aggregation

Total sales and the number of records are calculated for each product category.
The aggregation uses:
- sum("Sales") – calculates total sales.
- count("Product_ID") – counts the number of records.

8. Remove Duplicate Records

Duplicate records are removed using:
df.dropDuplicates()
The original record count and the record count after removing duplicates are displayed.

9. Create Second Dataset

A second dataset containing product IDs and their locations is created.
The columns are:
- Product_ID
- Location

10. Join Two Datasets

The sales dataset and product location dataset are joined using Product_ID.
An inner join is used to create the joined dataset.

11. Calculate Average Sales

Average sales are calculated for each product category using:
avg("Sales")
The result is displayed as Average_Sales.

12. Stop Spark Session

After all operations are completed, the Spark session is stopped using:
spark.stop()
How to Run
Install PySpark:
pip install pyspark
Run the notebook cells in order.
The practical follows this flow:
Create Spark Session
        ↓
Create Sales Dataset
        ↓
Write CSV Dataset
        ↓
Read CSV
        ↓
Display Schema
        ↓
Filtering
        ↓
Grouping
        ↓
Aggregation
        ↓
Remove Duplicates
        ↓
Create Location Dataset
        ↓
Join Datasets
        ↓
Average Sales by Category
        ↓
Stop Spark Session

Result

The practical successfully performs data processing operations using PySpark, including CSV reading and writing, schema display, filtering, grouping, aggregation, duplicate removal, dataset joining, and average sales calculation.

Conclusion

This practical demonstrates how PySpark can be used to process and analyze structured sales data efficiently. It covers important DataFrame operations such as filtering, grouping, aggregation, duplicate removal, joins, and statistical calculations.
