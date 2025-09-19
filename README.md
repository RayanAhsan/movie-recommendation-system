# Movie Recommendation System (MLOps End-to-End Project)

## Overview

This project is a sophisticated, production-ready **Movie Recommendation System** that leverages advanced machine learning and MLOps practices. It demonstrates the full lifecycle of a real-world ML application, from data ingestion and feature engineering to model training, deployment, and user interaction via a modern frontend and API.

---

## Key Features

- **Hybrid Recommendation Engine:**  
  Combines collaborative filtering and content-based methods, achieving a robust cosine similarity score of **0.81** for user-item matching.

- **Scalable Data Pipelines:**  
  Automated data preprocessing, feature engineering, and model training using Python, Pandas, and scikit-learn.

- **MLOps Integration:**  
  End-to-end automation with Docker and MLflow for reproducible experiments, model versioning, and seamless deployment.

- **FastAPI Backend:**  
  High-performance RESTful API built with FastAPI, enabling real-time recommendations and feedback collection.

- **Modern Frontend:**  
  User-friendly interface for movie exploration and personalized recommendations, built with JavaScript.

---


## End-to-End Workflow

1. **Data Collection & Preprocessing:**  
   - Ingest raw movie and user data  
   - Clean, normalize, and transform datasets

2. **Feature Engineering:**  
   - Extract relevant features for both collaborative and content-based filtering  
   - Construct user-item matrices

3. **Model Training & Evaluation:**  
   - Train recommendation models  
   - Evaluate using cosine similarity and other metrics

4. **MLOps Automation:**  
   - Containerize the application with Docker  
   - Track experiments and models with MLflow  
   - Enable CI/CD for continuous integration and deployment

5. **API & Frontend Integration:**  
   - Serve recommendations via FastAPI endpoints  
   - Interactive React frontend for users to receive and rate recommendations

---

## Technologies Used

- **Python, Pandas, scikit-learn** (ML & Data Processing)
- **FastAPI** (Backend API)
- **React** (Frontend)
- **Docker** (Containerization)
- **MLflow** (Experiment Tracking & Model Management)
- **Git & GitHub** (Version Control & Collaboration)

---

## Why I am really proud of this project

- **Production-Grade MLOps:**  
  Not just a model—this project covers the full ML lifecycle, including deployment, monitoring, and scalability.

- **Real-Time Recommendations:**  
  Users receive instant, personalized movie suggestions based on their preferences and feedback.

- **Robust Evaluation:**  
  Achieved a high cosine similarity score, demonstrating strong recommendation accuracy.

- **Extensible & Maintainable:**  
  Modular codebase and automated pipelines make it easy to extend and maintain.

---

## Getting Started

1. **Clone the repository:**
   ```
   git clone https://github.com/RayanAhsan/movie-recommendation-system.git
   ```

2. **Build and run with Docker:**
   ```
   docker-compose up --build
   ```

3. **Access the frontend:**
   - Open [http://localhost:3000](http://localhost:3000) in your browser.

4. **API Documentation:**
   - Visit [http://localhost:8000/docs](http://localhost:8000/docs) for interactive FastAPI docs.

---

## License

This project is licensed under the MIT License.

---

## Contact

For questions or collaboration, please reach out via [GitHub Issues](https://github.com/RayanAhsan/movie-recommendation-system/issues).

