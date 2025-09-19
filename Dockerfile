FROM python:3.12-slim

WORKDIR /app

# Install system deps including git for dvc (if you still want to use dvc commands inside container)
RUN apt-get update && apt-get install -y build-essential gcc git curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Optionally install dvc if you still want it inside container (can be removed if unused)
RUN pip install --no-cache-dir "dvc[gdrive]"

# Copy all your code, models, and data folders
COPY . ./

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
