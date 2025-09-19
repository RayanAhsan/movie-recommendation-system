import pandas as pd
import pickle

# Load the trained model
with open("models/svd_model.pkl", "rb") as f:
    model = pickle.load(f)

movies = pd.read_csv("data/processed/ratings.csv")[['movie_id', 'title']].drop_duplicates().set_index('movie_id')
some_movie_id = list(movies.index)[0]

print("Testing movie_id:", some_movie_id)

try:
    inner_id = model.trainset.to_inner_iid(str(some_movie_id))
    print("Inner ID:", inner_id)
    print("Factor vector:", model.qi[inner_id])
except ValueError as e:
    print("Error:", e)

missing = []
present = []

for mid in movies.index:
    try:
        model.trainset.to_inner_iid(str(mid))
        present.append(mid)
    except ValueError:
        missing.append(mid)

print(f"Movies with factors: {len(present)}")
print(f"Movies without factors: {len(missing)}")
print(model.qi.shape)
