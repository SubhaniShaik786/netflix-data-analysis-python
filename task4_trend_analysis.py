
# Auspify Technologies Internship
# Project: Netflix Data Analysis
# Task 4: Trend Analysis by Release Year

import pandas as pd
import matplotlib.pyplot as plt
import os

print("Auspify Technologies Internship")
print("Task 4: Netflix Release Year Trend Analysis")

# Load dataset
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)
base = PROJECT_DIR

file_path = os.path.join(
    PROJECT_DIR,
    "Task_1_Data_Cleaning",
    "netflix_cleaned.csv"
)

df = pd.read_csv(file_path)

# Create folders
task_folder = os.path.join(base, "Task_4_Trend_Analysis")
screenshot_folder = os.path.join(base, "Screenshots")

os.makedirs(task_folder, exist_ok=True)
os.makedirs(screenshot_folder, exist_ok=True)

print("\nDataset Loaded Successfully!")
print("Dataset Shape:", df.shape)

# Count titles by release year
year_counts = df['release_year'].value_counts().sort_index()

print("\nTop 10 Release Years:")
print(year_counts.sort_values(ascending=False).head(10))

# Chart 1: Release Year Trend
fig = plt.figure(figsize=(12, 6))

plt.plot(year_counts.index, year_counts.values, marker='o')

plt.title("Netflix Content Release Year Trend")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.grid(True)

plt.tight_layout()

fig.savefig(
    os.path.join(task_folder, "01_Release_Year_Trend.png"),
    dpi=150
)
fig.savefig(
    os.path.join(screenshot_folder, "Task4_Release_Year_Trend.png"),
    dpi=150
)
plt.close(fig)

# Chart 2: Movies vs TV Shows by Release Year
year_type = df.pivot_table(
    index='release_year',
    columns='type',
    values='show_id',
    aggfunc='count',
    fill_value=0
)

fig = plt.figure(figsize=(12, 6))

for content_type in year_type.columns:
    plt.plot(
        year_type.index,
        year_type[content_type],
        label=content_type
    )

plt.title("Movies vs TV Shows by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.legend()
plt.grid(True)

plt.tight_layout()

fig.savefig(
    os.path.join(task_folder, "02_Movies_vs_TV_Shows_Trend.png"),
    dpi=150
)
fig.savefig(
    os.path.join(screenshot_folder, "Task4_Movies_vs_TV_Shows.png"),
    dpi=150
)
plt.close(fig)

# Chart 3: Top 10 Release Years
top_years = year_counts.sort_values(ascending=False).head(10)
top_years = top_years.sort_index()

fig = plt.figure(figsize=(11, 6))

plt.bar(top_years.index.astype(str), top_years.values)

plt.title("Top 10 Years by Netflix Content Release")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.tight_layout()

fig.savefig(
    os.path.join(task_folder, "03_Top_10_Release_Years.png"),
    dpi=150
)
fig.savefig(
    os.path.join(screenshot_folder, "Task4_Top_10_Release_Years.png"),
    dpi=150
)
plt.close(fig)

# Final results
print("\nMost Productive Release Year:")
print(year_counts.idxmax())

print("Number of Titles:", year_counts.max())

print("\nAll Task 4 Charts Saved Successfully!")
print("Task Folder:", task_folder)
print("Screenshots Folder:", screenshot_folder)

print("\nTrend Analysis Completed!")
