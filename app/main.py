from fastapi import FastAPI
import pickle
import pandas as pd
from surprise import SVD

#load the model
with open("models/svd_model.pkl", "rb") as f:
    model = pickle.load(f)

#load the metadata
movies = pd.read_csv("data/processed/ratings.csv")[['movie_id', 'title']].drop_duplicates().set_index('movie_id')

app = FastAPI(title="Movie Recommendation API", version="1.0")

@app.get("/")

def home():
    return {"message": "Welcome to the Movie Recommendation API. Use the /recommend/{user_id} endpoint to get recommendations."}

@app.get("/recommend/{user_id}")
def recommend(user_id: int, n: int = 5):
    predictions = []
    for movie_id in movies.index:
        #predict the rating for each movie
        pred = model.predict(user_id, movie_id)
        predictions.append((movie_id, pred.est))
    
    #sort the predictions by estimated rating
    predictions.sort(key=lambda x: x[1], reverse=True)
    top_n = predictions[:n]
    
    #map movie ids to titles
    recommended_movies = [{"movie_id": movie_id, "title": movies.loc[movie_id, "title"], "estimated_rating": est} for movie_id, est in top_n]

    return {"user_id": user_id, "recommendations": recommended_movies}
