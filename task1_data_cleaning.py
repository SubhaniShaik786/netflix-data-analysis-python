# Auspify Technologies Internship
# Project: Netflix Data Analysis
# Task 1: Data Cleaning and Preparation

print("Welcome to Auspify Technologies Internship!")
print("Project: Netflix Data Analysis")
print("Task 1: Data Cleaning and Preparation")
print("Python environment is ready!")

# Step 1: Import Pandas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Step 2: Load Netflix Dataset

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)

file_path = os.path.join(
    PROJECT_DIR, "Dataset", "netflix_titles.csv"
)

df = pd.read_csv(file_path)

# Step 3: Display first 5 records

print("\nFirst 5 Records:")
print(df.head())

# Step 4: Display dataset dimensions

print("\nDataset Shape:")
print(df.shape)

# Step 5: Display column names

print("\nColumn Names:")
print(df.columns)

# Step 6: Display dataset information

print("\nDataset Information:")
df.info()

# Step 7: Check missing values

print("\nMissing Values in Each Column:")

print(df.isnull().sum())

# Step 8: Calculate missing value percentage

print("\nMissing Value Percentage:")

missing_percentage = (df.isnull().sum() / len(df)) * 100

print(missing_percentage.round(2))

# Step 9: Calculate total missing values

total_missing = df.isnull().sum().sum()

print("\nTotal Missing Values:", total_missing)

# Step 10: Create a copy of original dataset

df_clean = df.copy()

# Step 11: Handle missing values

df_clean['director'] = df_clean['director'].fillna('Not Available')

df_clean['cast'] = df_clean['cast'].fillna('Not Available')

df_clean['country'] = df_clean['country'].fillna('Not Available')

df_clean['rating'] = df_clean['rating'].fillna('Not Available')

df_clean['duration'] = df_clean['duration'].fillna('Not Available')

# Step 12: Convert date_added into datetime format

df_clean['date_added'] = pd.to_datetime(
    df_clean['date_added'].str.strip(),
    format='%B %d, %Y',
    errors='coerce'
)

# Step 13: Check missing values after cleaning

print("\nMissing Values After Cleaning:")

print(df_clean.isnull().sum())

# Step 14: Display cleaned dataset information

print("\nCleaned Dataset Information:")

df_clean.info()

# Step 15: Check duplicate records

print("\nDuplicate Records Analysis:")

# Check complete duplicate rows
total_duplicates = df_clean.duplicated().sum()

print("Total Duplicate Rows:", total_duplicates)

# Check duplicate Show IDs
duplicate_ids = df_clean['show_id'].duplicated().sum()

print("Duplicate Show IDs:", duplicate_ids)

# Display duplicate records if available
if total_duplicates > 0:
    print("\nDuplicate Records:")
    print(df_clean[df_clean.duplicated()])
else:
    print("\nNo complete duplicate records found.")
    
# Step 16: Standardize text columns

text_columns = ['type', 'title', 'director', 'cast',
                'country', 'rating', 'listed_in', 'description']

for column in text_columns:
    df_clean[column] = df_clean[column].apply(
        lambda x: x.strip() if isinstance(x, str) else x
    )

print("\nText Standardization Completed!")
print("Cleaned Dataset Shape:", df_clean.shape)

# Step 17: Save the cleaned dataset

output_path = r"C:\Users\VICTUS\Auspify_Internship\Netflix_Data_Analysis\Task_1_Data_Cleaning\netflix_cleaned.csv"

df_clean.to_csv(output_path, index=False)

print("\nCleaned Dataset Saved Successfully!")
print("File Location:", output_path)

# Step 18: Verify the saved CSV file

df_check = pd.read_csv(output_path)

print("\nSaved File Verification:")
print("Shape:", df_check.shape)
print("\nFirst 5 Records:")
print(df_check.head())
print("\nMissing Values:")
print(df_check.isnull().sum())
