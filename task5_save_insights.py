import os
import pandas as pd

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

# Analyse ratings
rating_counts = df[
    df["rating"] != "Not Available"
]["rating"].value_counts()

# Analyse genres
genres = df["listed_in"].dropna().str.split(",").explode().str.strip()
genre_counts = genres.value_counts()

# Prepare insights
insights = f"""
TASK 5: ADVANCED RATING AND GENRE ANALYSIS

Dataset Overview:
Total Netflix titles analysed: {len(df)}

RATING ANALYSIS:
Most common rating: {rating_counts.index[0]}
Number of titles: {rating_counts.iloc[0]}

Top 5 Ratings:
{rating_counts.head(5).to_string()}

GENRE ANALYSIS:
Most common genre: {genre_counts.index[0]}
Number of titles: {genre_counts.iloc[0]}

Top 10 Genres:
{genre_counts.head(10).to_string()}

KEY FINDINGS:
1. TV-MA is the most common content rating in the dataset.
2. TV-14 is the second most common rating.
3. International Movies is the most frequently listed genre.
4. Dramas and Comedies are also among the leading genres.
5. Netflix offers content across a wide range of genres and audience ratings.

CONCLUSION:
The analysis shows that Netflix has a strong presence of mature-rated
content and a broad variety of movie and television genres.
These findings can help understand the platform's content distribution.
"""

# Save insights
output_file = os.path.join(BASE_DIR, "Task5_Insights.txt")

with open(output_file, "w", encoding="utf-8") as file:
    file.write(insights)

print("Task 5 insights saved successfully!")
print("File location:", output_file)
print("\n", insights)

