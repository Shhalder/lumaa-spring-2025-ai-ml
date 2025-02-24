# Content-Based Movie Recommendation System

This project implements a simple content-based recommendation system for movies. Given a short text description of a user's preferences (e.g., "I love thrilling action movies set in space, with a comedic twist."), the system uses TF-IDF vectorization and cosine similarity to return the top 5 most similar movie titles from a dataset.

## Dataset

- **Source:** The dataset is provided as a CSV file named `movie_dataset.csv` can be downloaded from https://www.kaggle.com/datasets/utkarshx27/movies-dataset
- **Content:** The dataset contains columns such as `title`, `overview`, `keywords`, `genres`, and `popularity`.
- **Preprocessing:** Only the columns that contribute to text similarity (`title`, `overview`, `keywords`, `genres`, and `popularity`) are used. The textual columns `keywords` and `overview` are merged to create a combined description for each movie.

## Setup

1. **Python Version:** This code requires Python 3.11.11
2. **Dependencies:** Install the required packages using:
   ```bash
   pip install pandas


## Video RecordingA video recording  explaining the code is accessible at https://drive.google.com/file/d/1B1aJj2MQml3ScDnuwuwdz7LSkux9PpLp/view?usp=sharing 