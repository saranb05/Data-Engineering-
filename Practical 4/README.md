Practical 4 – Noise Elimination, Feature Selection and EDA
Aim
To perform Noise Elimination, Feature Selection, and Exploratory Data Analysis (EDA) using Python.
Description
This practical uses a sample student dataset containing Age, Marks, Attendance, and Constant.
The program performs:
- Noise elimination using the IQR method.
- Feature selection using VarianceThreshold.
- Exploratory Data Analysis using dataset information, statistical summary, correlation matrix, histogram, and boxplot.
Dataset
The dataset is stored in data/sample_student_data.csv.
The Age = 100 value is included as a potential outlier, while Constant contains the same value in every row to demonstrate zero-variance feature removal.
Files
- practical_4.py – Python program for the practical.
- data/sample_student_data.csv – Sample student dataset.
- README.md – Practical documentation.
- requirements.txt – Required Python libraries.
Libraries Used
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
How to Run
Install the required libraries:
pip install -r requirements.txt
Run the program:
python practical_4.py
Result
The program removes the noisy/outlier value using IQR, removes the zero-variance Constant feature, and performs EDA using statistical analysis and visualizations.
