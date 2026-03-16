import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("movies.csv")

tfidf = TfidfVectorizer(token_pattern='[^|]+')
tfidf_matrix = tfidf.fit_transform(movies['genres'])

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

def recommend_movies(title):

    idx = indices[title]

    sim_scores = list(enumerate(cosine_sim[idx]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:6]

    movie_indices = [i[0] for i in sim_scores]

    return movies['title'].iloc[movie_indices]


st.title("🎬 AI Movie Recommendation System")

movie_name = st.text_input("Enter a movie name")

if movie_name:

    results = movies[movies['title'].str.contains(movie_name, case=False)]

    if len(results) > 0:

        selected_movie = results.iloc[0]['title']

        st.write("Recommendations for:", selected_movie)

        recs = recommend_movies(selected_movie)

        for movie in recs:
            st.write(movie)

    else:
        st.write("Movie not found")