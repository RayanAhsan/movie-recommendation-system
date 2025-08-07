import pandas as pd
import pickle
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
from surprise import accuracy
import mlflow
import os

# This file handles the training of the model

os.makedirs("models", exist_ok=True)
#load the processed ratings data
ratings = pd.read_csv("data/processed/ratings.csv")

#splitting the dataset into train and test sets
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(ratings[['user_id', 'movie_id', 'rating']], reader)
trainset, testset = train_test_split(data, test_size=0.2, random_state=42)

#training the SVD model
model = SVD()
model.fit(trainset)

#evaluating the model
predictions = model.test(testset)
rmse = accuracy.rmse(predictions)

#save the model
with open("models/svd_model.pkl", "wb") as f:
    pickle.dump(model, f)
print("Model training complete. RMSE:", rmse)
print("Model saved to: models/svd_model.pkl")

#log the model with MLflow

mlflow.start_run()
mlflow.log_param("model_type", "SVD")
mlflow.log_metric("rmse", rmse)
mlflow.log_artifact("models/svd_model.pkl", artifact_path="model")
mlflow.end_run()
print("Model logged with MLflow.")