from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pickle
import pandas as pd
from surprise import SVD
from typing import List

# Load the model
with open("models/svd_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load the metadata
movies = pd.read_csv("data/processed/ratings.csv")[['movie_id', 'title']].drop_duplicates().set_index('movie_id')

# Create a mapping from title -> movie_id
title_to_id = {title.lower(): mid for mid, title in movies["title"].items()}

app = FastAPI(title="Movie Recommendation API", version="1.0")

# ✅ Enable CORS for all origins (or specify just your frontend URL)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace ["*"] with ["http://localhost:3000", "https://your-frontend-url.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Welcome to the Movie Recommendation API. Use /recommend/{user_id} for existing users or /recommend_by_movies for new users."
    }

@app.get("/recommend/{user_id}")
def recommend(user_id: int, n: int = 5):
    predictions = []
    for movie_id in movies.index:
        pred = model.predict(user_id, movie_id)
        predictions.append((movie_id, pred.est))
    
    predictions.sort(key=lambda x: x[1], reverse=True)
    top_n = predictions[:n]
    
    recommended_movies = [
        {"movie_id": movie_id, "title": movies.loc[movie_id, "title"], "estimated_rating": est}
        for movie_id, est in top_n
    ]

    return {"user_id": user_id, "recommendations": recommended_movies}

@app.get("/recommend_by_movies")
def recommend_by_movies(liked_movies: List[str] = Query(..., description="List of liked movie titles"), n: int = 5):
    # Pick an ID that doesn't exist in the training data for the pseudo user
    new_user_id = 999999

    # Get the movie_ids for the provided titles
    liked_ids = []
    for title in liked_movies:
        movie_id = title_to_id.get(title.lower())
        if movie_id:
            liked_ids.append(movie_id)
        else:
            return {"error": f"Movie '{title}' not found in database."}

    predictions = []
    for movie_id in movies.index:
        if movie_id in liked_ids:
            continue  # Skip already liked movies
        pred = model.predict(new_user_id, movie_id)
        predictions.append((movie_id, pred.est))
    
    predictions.sort(key=lambda x: x[1], reverse=True)
    top_n = predictions[:n]

    recommended_movies = [
        {"movie_id": movie_id, "title": movies.loc[movie_id, "title"], "estimated_rating": est}
        for movie_id, est in top_n
    ]

    return {"input_movies": liked_movies, "recommendations": recommended_movies}
