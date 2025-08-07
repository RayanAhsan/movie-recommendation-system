#This file handles the preprocessing of the dataset
import pandas as pd
from pathlib import Path

RAW_DATA_PATH = Path("data/raw")
PROCESSED_DATA_PATH = Path("data/processed")
PROCESSED_DATA_PATH.mkdir(parents=True, exist_ok=True)

#loading the raw dataset

ratings = pd.read_csv(RAW_DATA_PATH / "u.data", sep="\t", names=["user_id", "movie_id", "rating", "timestamp"])

movies = pd.read_csv(RAW_DATA_PATH / "u.item", sep="|", encoding="latin-1", header=None)

#only need movie_id and title
movies = movies[[0, 1]]
movies.columns = ["movie_id", "title"]

#merging the ratings with movie titles
ratings = ratings.merge(movies, on="movie_id")

#user-item matrix
user_item_matrix = ratings.pivot_table(index="user_id", columns="title", values="rating")

#save the processed data
ratings.to_csv(PROCESSED_DATA_PATH / "ratings.csv", index=False)
user_item_matrix.to_csv(PROCESSED_DATA_PATH / "user_item_matrix.csv")

print("Preprocessing complete. Processed data saved to:", PROCESSED_DATA_PATH)
print("Ratings shape:", ratings.shape)
print("User-item matrix shape:", user_item_matrix.shape)