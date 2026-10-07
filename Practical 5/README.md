Practical 5 – Data Extraction and ETL Pipeline

Aim

To extract data from different sources, perform data transformation and merging, and save the cleaned data using Python.

Libraries Used

- Pandas – for data handling, transformation, merging, and CSV operations
- Requests – for making API requests

Data Sources

This practical extracts data from two sources:

1. REST API – User data is extracted from the JSONPlaceholder API.
2. CSV File – Location data containing city and country information is created and extracted from a CSV file.

1. API Data Extraction

The program uses a function named extract_api_data() to fetch data from the REST API.
The API used is:
https://jsonplaceholder.typicode.com/users
The JSON response is converted into a Pandas DataFrame using pd.json_normalize().
The required columns are:
- id
- name
- email
- company

2. CSV Data Extraction

The program uses extract_csv_data() to read a flat CSV file using Pandas.
A sample location dataset is created with:
- id
- city
- country
The data contains locations such as New York, London, Paris, Tokyo, Delhi, Sydney, Moscow, Cairo, and Beijing.

3. Data Transformation and Merging

The API data and CSV data are merged using the common id column.
An inner join is used to create the final merged dataset.
The resulting data contains user information along with the corresponding location information.

4. Save Cleaned Data

The merged data is saved as:
cleaned_warehouse_profiles.csv

How to Run

Install the required libraries:
pip install pandas requests
Run the notebook cells in order.

Result

The program successfully:
- Extracts user data from a REST API.
- Extracts location data from a CSV file.
- Transforms and merges the datasets using id.
- Displays the API, CSV, and merged data.
- Saves the final merged dataset as cleaned_warehouse_profiles.csv.

Conclusion

This practical demonstrates a basic ETL pipeline where data is extracted from an API and a CSV file, transformed and merged using Pandas, and finally saved as a cleaned CSV dataset.
