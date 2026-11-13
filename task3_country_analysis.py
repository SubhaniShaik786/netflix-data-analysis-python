
# Auspify Technologies Internship
# Project: Netflix Data Analysis
# Task 3: Country-Wise Analysis

import pandas as pd
import matplotlib.pyplot as plt
import os

print("Auspify Technologies Internship")
print("Task 3: Country-Wise Netflix Analysis")

# Load cleaned dataset
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)
base = PROJECT_DIR

file_path = os.path.join(
    PROJECT_DIR,
    "Task_1_Data_Cleaning",
    "netflix_cleaned.csv"
)

df = pd.read_csv(file_path)

print("\nDataset Loaded Successfully!")
print("Dataset Shape:", df.shape)

# Create output folders
task_folder = os.path.join(base, "Task_3_Country_Analysis")
screenshot_folder = os.path.join(base, "Screenshots")

os.makedirs(task_folder, exist_ok=True)
os.makedirs(screenshot_folder, exist_ok=True)

# Clean country column and count individual countries
countries = (
    df['country']
    .dropna()
    .str.split(',')
    .explode()
    .str.strip()
)

countries = countries[countries != 'Not Available']

country_counts = countries.value_counts()

print("\nTop 10 Countries Producing Netflix Content:")
print(country_counts.head(10))

# Create Top 10 countries bar chart
top_10 = country_counts.head(10)

fig = plt.figure(figsize=(11, 6))

plt.bar(top_10.index, top_10.values)

plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)

plt.tight_layout()

# Save chart in both folders
fig.savefig(
    os.path.join(task_folder, "top_10_countries.png"),
    dpi=150
)

fig.savefig(
    os.path.join(screenshot_folder, "Task3_Top_10_Countries.png"),
    dpi=150
)

plt.close(fig)

# Create a pie chart for the top 5 countries
top_5 = country_counts.head(5)

fig = plt.figure(figsize=(9, 7))

plt.pie(
    top_5.values,
    labels=top_5.index,
    autopct='%1.1f%%',
    startangle=90
)

plt.title("Top 5 Countries - Netflix Content")
plt.tight_layout()

fig.savefig(
    os.path.join(task_folder, "top_5_countries_pie.png"),
    dpi=150
)

fig.savefig(
    os.path.join(screenshot_folder, "Task3_Top_5_Countries_Pie.png"),
    dpi=150
)

plt.close(fig)

print("\nTask 3 Charts Saved Successfully!")
print("Task Folder:", task_folder)
print("Screenshots Folder:", screenshot_folder)
print("\nCountry-Wise Analysis Completed!")
