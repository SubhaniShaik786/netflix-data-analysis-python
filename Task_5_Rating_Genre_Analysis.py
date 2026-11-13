import os
import pandas as pd
import matplotlib.pyplot as plt

# Get project folder location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)

# Load cleaned Netflix dataset
file_path = os.path.join(
    PROJECT_DIR,
    "Task_1_Data_Cleaning",
    "netflix_cleaned.csv"
)

df = pd.read_csv(file_path)

# Display basic information
print("Netflix Dataset Loaded Successfully!")
print("Dataset Shape:", df.shape)

print("\nAvailable Columns:")
print(df.columns.tolist())

print("\nTop 10 Ratings:")
print(df["rating"].value_counts().head(10))

print("\nTop 10 Genres:")
genres = df["listed_in"].str.split(",").explode().str.strip()
print(genres.value_counts().head(10))

# Create output folders
SCREENSHOT_DIR = os.path.join(PROJECT_DIR, "Screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# -------------------------------
# Chart 1: Top 10 Netflix Ratings
# -------------------------------

rating_counts = df[
    df["rating"] != "Not Available"
]["rating"].value_counts().head(10)

plt.figure(figsize=(10, 6))
rating_counts.plot(kind="bar", edgecolor="black")

plt.title("Top 10 Netflix Content Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(os.path.join(BASE_DIR, "top_10_ratings.png"), dpi=300)
plt.savefig(os.path.join(SCREENSHOT_DIR, "Task5_Top_10_Ratings.png"), dpi=300)
plt.show()


# -------------------------------
# Chart 2: Top 10 Netflix Genres
# -------------------------------

genres = df["listed_in"].dropna().str.split(",").explode().str.strip()

genre_counts = genres.value_counts().head(10)

plt.figure(figsize=(12, 6))
genre_counts.plot(kind="bar", edgecolor="black")

plt.title("Top 10 Netflix Genres")
plt.xlabel("Genre")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig(os.path.join(BASE_DIR, "top_10_genres.png"), dpi=300)
plt.savefig(os.path.join(SCREENSHOT_DIR, "Task5_Top_10_Genres.png"), dpi=300)
plt.show()

print("\nTask 5 charts saved successfully!")