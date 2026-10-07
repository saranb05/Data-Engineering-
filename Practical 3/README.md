Practical 3 – Handling Missing Values, Duplicate Records, and Data Normalization

Aim

To handle missing values, remove duplicate records, and normalize numerical data using Pandas.

Library Used
- Pandas – for data creation, cleaning, duplicate removal, normalization, and CSV output
Practical Description

This practical demonstrates basic data preprocessing techniques using a sample student dataset.

The program performs three main operations:
1. Handling missing values
2. Removing duplicate records
3. Normalizing numerical columns using Min-Max scaling

1. Sample Dataset

The sample dataset contains the following columns:
- Name
- Age
- Marks
The dataset includes missing values and a duplicate record to demonstrate data cleaning.

2. Handling Missing Values

Missing values are handled as follows:
- Missing Age values are replaced with the mean age.
- Missing Marks values are replaced with the mean marks.
- Missing Name values are replaced with Unknown.

3. Removing Duplicate Records

Duplicate rows are removed using:
df.drop_duplicates()
This removes repeated records from the dataset.

4. Data Normalization

The Age and Marks columns are normalized using Min-Max Scaling.
The formula used is:
(x - min) / (max - min)
Two new columns are created:
- Age_Normalized
- Marks_Normalized
The normalized values are scaled between 0 and 1.

5. Save Final Processed Data

After cleaning and normalization, the final processed dataset is saved as:
output/cleaned_data.csv

How to Run
Install Pandas if required:
pip install pandas
Run the Python program:
python practical_03.py
Make sure the output folder exists before running the program so that the cleaned CSV can be saved successfully.

Process Flow
Sample Student Data
        ↓
Handle Missing Values
        ↓
Remove Duplicate Rows
        ↓
Min-Max Normalization
        ↓
Final Processed Data
        ↓
output/cleaned_data.csv

Result

The program successfully handles missing values, removes duplicate records, normalizes the Age and Marks columns using Min-Max scaling, and saves the final processed data as a CSV file.

Conclusion

This practical demonstrates important data preprocessing techniques using Pandas. Handling missing values improves data completeness, removing duplicates improves data quality, and normalization brings numerical values to a common scale for further analysis.
