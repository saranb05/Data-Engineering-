Practical 7 – ETL Pipeline with Multiple Data Sources and SQLite

Aim

To perform an ETL process using multiple CSV files and JSON data, validate and transform the data, load it into a relational SQLite database, and perform incremental data loading.

Libraries Used

- Pandas – for data extraction, transformation, validation, and loading
- JSON – for reading and writing JSON data
- SQLite3 – for creating and managing the relational database
- OS – for file and system operations

Practical Description

This practical demonstrates a complete ETL pipeline using multiple data sources. Student data is extracted from two CSV files and a JSON file, combined and transformed, validated, and loaded into a SQLite database.

1. Create Sample CSV Files

Two CSV files are created:
- students1.csv
- students2.csv
Both files contain:
- Student ID
- Name
- Age
- Marks

2. Extract Data from Multiple CSV Files

The two CSV files are read using Pandas and stored as DataFrames.

3. Combine Multiple CSV Files

The two datasets are combined into a single DataFrame using pd.concat().

4. Identify and Remove Invalid Records

Records are checked using the following conditions:
- Age must be between 18 and 25.
- Marks must be between 0 and 100.
Invalid records are identified and then removed from the dataset.

5. Transform Data

The cleaned data is transformed by:
- Converting student names to uppercase.
- Creating a Performance category based on marks.

The performance categories are:
- Excellent – Marks ≥ 85
- Good – Marks ≥ 70
- Needs Improvement – Marks < 70

6. Create and Transform JSON Data

A JSON file named students.json is created containing:
- Student ID
- Course
- City
The JSON data is converted into a DataFrame. The student_id field is renamed to Student_ID, and city names are converted to uppercase.

7. Create Relational Database

A SQLite database named:
ETL_Practical7.db
is created and connected using SQLite3.

8. Data Validation

Before loading the data into the database, the program checks:
- Missing values
- Duplicate Student IDs
- Valid age range
- Valid marks range
If all validation conditions are satisfied, the data is considered ready for database loading.

9. Load Data into Database

The cleaned CSV data is loaded into the:
Students
table.
The transformed JSON data is loaded into the:
Student_Courses
table.

10. Verify Database Data

The contents of both database tables are retrieved using SQL queries and displayed to verify that the data was loaded successfully.

11. Incremental Data Loading

New student records are introduced later.
The program checks the existing Student IDs in the database and selects only records that are not already present.
Only the new records are appended to the Students table.

12. Final Database Check

The final Students table is displayed after incremental loading.
The database connection is then closed and the ETL pipeline is completed.
How to Run
Run the notebook cells in order.
The practical follows this ETL flow:
CSV Files + JSON
       ↓
   Extraction
       ↓
   Combination
       ↓
  Data Validation
       ↓
 Transformation
       ↓
 SQLite Database
       ↓
 Incremental Loading
       ↓
 Final Verification

Result

The practical successfully extracts student data from multiple CSV files and JSON, combines and transforms the data, validates it, loads it into SQLite tables, verifies the database contents, and performs incremental loading of new records.

Conclusion

This practical demonstrates a complete ETL workflow using multiple data sources and a relational SQLite database. It also shows how data validation, transformation, database loading, verification, and incremental loading can be performed using Python.
