Practical 2 – ETL Process using SQL Server

Aim
To perform the ETL (Extract, Transform, Load) process using SQL Server.
Tools Used
- SQL Server
- SQL Server Management Studio (SSMS)

Practical Description
This practical demonstrates a basic ETL process using student data in SQL Server. The data is stored in a source table, transformed to handle missing values and standardize data, and then loaded into a final table.

1. Create Database and Source Table

A database named:
ETL_Practical
is created.

A source table named Student_Data is created with the following columns:
- Student_ID
- Student_Name
- Age
- City
- Marks

Sample student records are inserted into the table. The dataset contains missing values in Age and City, as well as different capitalization for city names such as Mumbai, mumbai, Pune, and PUNE.

2. Extract

The Extract phase retrieves the data from the Student_Data table using a SELECT statement.
The original student data is displayed without applying any transformations.

3. Transform

The Transform phase cleans and standardizes the extracted data.
The following transformations are performed:
- Missing Age values are replaced with 0 using ISNULL().
- City names are standardized using UPPER().
- Mumbai and mumbai are converted to Mumbai.
- Pune and PUNE are converted to Pune.
- Missing city values are replaced with Unknown.
- A new Performance_Category column is created based on marks.

Performance Categories
Marks >= 85       → Excellent
Marks >= 70       → Good
Marks < 70        → Needs Improvement

4. Load

A final table named:
Student_Final
is created.
The transformed student data is inserted into this table using INSERT INTO ... SELECT.
The final table contains:
- Student_ID
- Student_Name
- Age
- City
- Marks
- Performance_Category

5. Verify Final Data

The final transformed and loaded data is displayed using:
SELECT * FROM Student_Final;
The output shows the cleaned age and city values along with the calculated performance category.
ETL Process Flow
Student_Data
     ↓
   Extract
     ↓
   Transform
     ↓
 Student_Final
     ↓
    Load
     ↓
 Final Output

How to Run

1. Open SQL Server Management Studio.
2. Create a new query.
3. Copy the SQL code from the practical.
4. Execute the code section by section.
5. Verify the Extract, Transform, and Load outputs.
6. Run the final SELECT * FROM Student_Final query to view the loaded data.

Result

The ETL process is successfully performed using SQL Server. The original student data is extracted, missing values and inconsistent city names are handled during transformation, performance categories are generated based on marks, and the cleaned data is loaded into the Student_Final table.

Conclusion

This practical demonstrates the three major stages of an ETL process using SQL Server. Data is extracted from the source table, transformed to improve consistency and handle missing values, and finally loaded into a separate final table for use and analysis.
