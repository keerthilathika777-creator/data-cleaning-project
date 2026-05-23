# Data Cleaning and Transformation Project

## Project Overview
This project focuses on performing data quality assessment, data cleaning, and data transformation on the Online Retail dataset.

The objective of this project is to prepare a clean and analysis-ready dataset by identifying and handling:
- Missing values
- Duplicate records
- Incorrect data types
- Outliers
- Inconsistent formatting

---

## Dataset Used
Online Retail Dataset

Dataset contains:
- Customer transactions
- Product details
- Invoice information
- Quantity purchased
- Unit prices
- Customer IDs
- Country information

---

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- VS Code

---

## Data Quality Issues Identified
The following issues were found during data profiling:
- Missing values
- Duplicate records
- Negative quantities
- Negative unit prices
- Inconsistent date formats

---

## Data Cleaning Steps Performed
- Removed missing values
- Removed duplicate rows
- Converted InvoiceDate to datetime format
- Removed invalid negative quantity values
- Removed invalid negative price values

---

## Feature Engineering
New columns created:
- TotalPrice
- Year
- Month

---

## Visualizations Created
- Missing values heatmap
- Unit price boxplot

---

## Final Output
Generated a cleaned dataset ready for analysis and machine learning tasks.

Output files:
- cleaned_retail_data.csv
- data_cleaning.py
- data_dictionary.xlsx

---

## Project Structure

Data-Cleaning-Project
│
├── data
├── notebooks
├── scripts
├── cleaned_data
├── screenshots
└── README.md

---

## How to Run the Project

1. Install required libraries:
pip install pandas numpy matplotlib seaborn

2. Open Jupyter Notebook

3. Run:
data_cleaning.ipynb

---

## Author
Keerthi Latika Yeluri