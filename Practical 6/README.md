Practical 6 – ETL Pipeline Orchestration using Apache Airflow

Aim

To create and orchestrate an ETL pipeline using Apache Airflow.

Libraries and Tools Used

- Apache Airflow – workflow orchestration
- Pandas – data handling and CSV operations
- Requests – API data extraction
- Python – ETL scripting

Practical Description

This practical demonstrates how an ETL pipeline can be created and scheduled using Apache Airflow.
The pipeline extracts data from a REST API and a CSV file, transforms and merges the data, saves the final dataset, and then uses an Airflow DAG to orchestrate the complete process.

1. Airflow Setup

Apache Airflow is installed and its version is checked.
The Airflow home directory is configured as:
/content/airflow
A dags folder is created for storing the Airflow DAG.
The Airflow database is then initialized/migrated.

2. Data Extraction Script

The ETL script data_extraction.py performs the following operations:
API Extraction
Data is extracted from:
https://jsonplaceholder.typicode.com/users

The required columns are:
- id
- name
- email
- company

The company column is renamed from company.name to company.

CSV Extraction

A sample locations.csv file is created containing:
- id
- city
- country

The locations included are Mumbai, Pune, Delhi, Chennai, and Bangalore.

Data Merging

The API data and CSV data are merged using the common id column with an inner join.

Save Final Data

The merged dataset is saved as:
/content/cleaned_warehouse_profiles.csv

3. Airflow DAG

The Airflow DAG is named:
university_etl_orchestration

The DAG contains three tasks:

1. start_pipeline – starts the pipeline.
2. run_extraction_script – executes data_extraction.py.
3. log_pipeline_success – displays a successful completion message.

The task flow is:

start_pipeline
      ↓
run_extraction_script
      ↓
log_pipeline_success

The DAG is configured to run daily, with catchup disabled.

4. DAG Verification and Execution

The practical checks the available DAGs and verifies that the university_etl_orchestration DAG is loaded correctly.

The DAG is also displayed using:
airflow dags show university_etl_orchestration

The DAG is triggered using:
airflow dags trigger university_etl_orchestration

DAG runs and task states can then be checked using the Airflow commands included in the notebook.

How to Run

Run the notebook cells in order.

The practical performs the following sequence:
Install Airflow
      ↓
Configure Airflow
      ↓
Create ETL script
      ↓
Create Airflow DAG
      ↓
Verify DAG
      ↓
Trigger DAG
      ↓
Check DAG run and task state

Result

The ETL pipeline is successfully created and orchestrated using Apache Airflow. The pipeline extracts data from an API and CSV file, merges the data, saves the final dataset, and executes the ETL process through an Airflow DAG.

Conclusion

This practical demonstrates how Apache Airflow can be used to automate and orchestrate an ETL workflow. The DAG provides a structured sequence for executing the extraction script and confirming successful completion.
