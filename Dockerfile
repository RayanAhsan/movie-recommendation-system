# Use official Python image as base
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .

RUN apt-get update && apt-get install -y build-essential gcc
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code and model files
COPY app/ ./app/
COPY models/ ./models/
COPY data/processed/ ./data/processed/

# Expose port for FastAPI
EXPOSE 8000

# Command to run FastAPI app using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
