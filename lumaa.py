# -*- coding: utf-8 -*-
"""Lumaa.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hXSmacOFWw6GH9ZmnH8pV6FbDeKhLa39

Importing libararies
"""

#Importing Libraries
import pandas as pd
from collections import defaultdict
import string
import math

#loading data
df = pd.read_csv("movie_dataset.csv")

#gathering information about the dataset
df.info()

#consideing only the files that will be useful
df = df[['title', 'overview', 'keywords', 'genres','popularity']]

df.info()

df.head()

# checking before merging colums
df['keywords'] = df['keywords'].astype(str)
df['overview'] = df['overview'].astype(str)

#merging colums
df['merged'] = df['keywords'] + " " + df['overview']

# list of dictionaries, ech dictioanry: movies and movie_description
dataset = [
    {"movie": row["title"], "movie_description": row["merged"]}
    for _, row in df.iterrows()
]

dataset[0]

wordCount = defaultdict(int)
punctuation = set(string.punctuation)
for d in dataset:
    r = ''.join([c for c in d['movie_description'].lower() if not c in punctuation])
    for w in r.split():
        wordCount[w] += 1

# Get a list of the top 1000 words (by frequency)
counts = [(wordCount[w], w) for w in wordCount]
counts.sort(reverse=True)
words = [x[1] for x in counts[:1000]]

dfreq = defaultdict(int)
for d in dataset:
    r = ''.join([c for c in d['movie_description'].lower() if c not in punctuation])
    for w in set(r.split()):
        dfreq[w] += 1

def Cosine(x1,x2):
    numer = 0
    norm1 = 0
    norm2 = 0
    for a1,a2 in zip(x1,x2):
        numer += a1*a2
        norm1 += a1**2
        norm2 += a2**2
    if norm1*norm2:
        return numer / math.sqrt(norm1*norm2)
    return 0

query_text = input("Enter your query: ")

tf_query = defaultdict(int)
r = ''.join([c for c in query_text.lower() if c not in punctuation])
for w in r.split():
    tf_query[w] = 1
tfidf_query = [tf_query[w] * math.log2(len(dataset) / dfreq[w]) for w in words]

similarities = []
for d in dataset:
    tf = defaultdict(int)
    r = ''.join([c for c in d['movie_description'].lower() if c not in punctuation])
    for w in r.split():
        tf[w] = 1
    tfidf_movie = [tf[w] * math.log2(len(dataset) / dfreq[w]) for w in words]
    sim = Cosine(tfidf_query, tfidf_movie)
    similarities.append((sim, d['movie']))

# Sort the movies by similarity
similarities.sort(reverse=True)
top_5 = similarities[:5]

print("\nTop 5 Recommended Movies:")
for sim, movie in top_5:
    print(f"Movie: {movie}, Similarity: {sim:.4f}")