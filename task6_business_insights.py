import os
import pandas as pd
import matplotlib.pyplot as plt

# Locate project folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)

# Load cleaned dataset
file_path = os.path.join(
    PROJECT_DIR,
    "Task_1_Data_Cleaning",
    "netflix_cleaned.csv"
)

df = pd.read_csv(file_path)

# Basic analysis
print("NETFLIX BUSINESS INSIGHTS ANALYSIS")
print("----------------------------------")

print("\nTotal Titles:", len(df))

print("\nContent Type Distribution:")
print(df["type"].value_counts())

print("\nTop 5 Countries:")
countries = df["country"].dropna().str.split(",").explode().str.strip()
countries = countries[countries != "Not Available"]
print(countries.value_counts().head(5))

print("\nTop 5 Genres:")
genres = df["listed_in"].dropna().str.split(",").explode().str.strip()
print(genres.value_counts().head(5))

print("\nTop 5 Release Years:")
print(df["release_year"].value_counts().head(5))

print("\nTop 5 Ratings:")
print(df["rating"].value_counts().head(5))

print("\nBusiness analysis data loaded successfully!")

# -----------------------------------------
# TASK 6: BUSINESS INSIGHTS REPORT
# -----------------------------------------

# Calculate content type percentages
content_counts = df["type"].value_counts()
content_percentages = (content_counts / len(df)) * 100

# Country analysis
country_counts = (
    df["country"].dropna()
    .str.split(",").explode().str.strip()
)
country_counts = country_counts[country_counts != "Not Available"]
top_countries = country_counts.value_counts().head(5)

# Genre analysis
genre_counts = (
    df["listed_in"].dropna()
    .str.split(",").explode().str.strip()
)
top_genres = genre_counts.value_counts().head(5)

# Release year analysis
year_counts = df["release_year"].dropna().value_counts().sort_values(
    ascending=False
).head(5)

# Rating analysis
rating_counts = df["rating"].dropna()
rating_counts = rating_counts[rating_counts != "Not Available"]
top_ratings = rating_counts.value_counts().head(5)

# Prepare business report
report = f"""
NETFLIX DATA ANALYSIS
TASK 6: BUSINESS INSIGHTS REPORT

1. PROJECT OVERVIEW
The analysis uses {len(df)} Netflix titles to understand
content distribution, country representation, genres,
release-year patterns, and content ratings.

2. CONTENT TYPE INSIGHTS
{content_counts.to_string()}

Content Type Percentages:
{content_percentages.round(2).to_string()}

Insight:
Movies represent the larger share of titles in this dataset.
Netflix could continue evaluating its movie and TV show mix
based on its content strategy.

3. COUNTRY-WISE INSIGHTS
Top 5 Countries:
{top_countries.to_string()}

Insight:
The United States has the highest number of country credits,
followed by India and the United Kingdom.
Netflix could evaluate opportunities for regional and
international content expansion.

4. GENRE INSIGHTS
Top 5 Genres:
{top_genres.to_string()}

Insight:
International Movies, Dramas, and Comedies are the most
frequently listed categories.
These categories may be useful areas for further content
portfolio analysis.

5. RELEASE YEAR INSIGHTS
Top 5 Release Years:
{year_counts.to_string()}

Insight:
2018 has the highest number of titles by release year.
The dataset shows a concentration of titles released
between 2016 and 2020 among the leading years.

6. CONTENT RATING INSIGHTS
Top 5 Ratings:
{top_ratings.to_string()}

Insight:
TV-MA and TV-14 are the two most frequent ratings.
Netflix should maintain a balanced content portfolio
that considers different audience age groups.

7. BUSINESS RECOMMENDATIONS
1. Review the balance between movies and TV shows.
2. Explore regional content opportunities in countries
   with growing representation.
3. Evaluate popular genre categories when planning content.
4. Maintain content variety across different age ratings.
5. Monitor release-year patterns alongside newer data
   before making content investment decisions.

8. CONCLUSION
This project provides an overview of Netflix's content
distribution using data analysis and visualization.
The findings can support further investigation into
content strategy, regional representation, and genre mix.

Note:
These findings describe the available dataset. They do not
measure actual viewer demand, revenue, or content performance.
Country and genre counts represent individual credits and
may count a title under multiple categories.
"""

# Save report
output_file = os.path.join(
    BASE_DIR,
    "Task6_Business_Insights_Report.txt"
)

with open(output_file, "w", encoding="utf-8") as file:
    file.write(report)

print("\nBusiness insights report saved successfully!")
print("Report location:", output_file)