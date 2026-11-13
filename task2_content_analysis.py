
# Auspify Technologies Internship
# Project: Netflix Data Analysis
# Task 2: Content Type Analysis

print("Auspify Technologies Internship")
print("Task 2: Netflix Content Type Analysis")

import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the cleaned dataset
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)

file_path = os.path.join(
    PROJECT_DIR,
    "Task_1_Data_Cleaning",
    "netflix_cleaned.csv"
)

df = pd.read_csv(file_path)


print("\nDataset Loaded Successfully!")
print("Dataset Shape:", df.shape)

# Count Movies and TV Shows
content_counts = df['type'].value_counts()

print("\nContent Type Count:")
print(content_counts)

# Calculate percentages
content_percentage = df['type'].value_counts(normalize=True) * 100

print("\nContent Type Percentage:")
print(content_percentage.round(2))

# Create a bar chart
plt.figure(figsize=(8, 5))

plt.bar(content_counts.index, content_counts.values)

plt.title("Netflix Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")

plt.tight_layout()
plt.savefig(
    r"C:\Users\VICTUS\Auspify_Internship\Netflix_Data_Analysis\Task_2_Content_Analysis\content_type_analysis.png"
)

plt.show()

print("\nContent Type Analysis Completed!")
