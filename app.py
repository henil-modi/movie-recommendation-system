import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Page configuration
st.set_page_config(
    page_title="AI Movie Recommender",
    page_icon="🎬",
    layout="centered"
)

# Title
st.title("🎬 AI Movie Recommendation System")
st.write("Find movies similar to your favorite ones using Machine Learning.")

# Sidebar
st.sidebar.header("About")
st.sidebar.write(
    """
    This AI system recommends movies using **TF-IDF vectorization**
    and **Cosine Similarity**.

    Dataset: MovieLens
    """
)

# Load dataset
movies = pd.read_csv("movies.csv")

# TF-IDF processing
tfidf = TfidfVectorizer(token_pattern='[^|]+')
tfidf_matrix = tfidf.fit_transform(movies['genres'])

# Similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Movie index mapping
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

# Recommendation function
def recommend_movies(title):

    idx = indices[title]

    sim_scores = list(enumerate(cosine_sim[idx]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:6]

    movie_indices = [i[0] for i in sim_scores]

    return movies['title'].iloc[movie_indices]

# User input
movie_name = st.text_input("Enter a movie name")

if movie_name:

    results = movies[movies['title'].str.contains(movie_name, case=False)]

    if len(results) > 0:

        selected_movie = results.iloc[0]['title']

        st.subheader(f"Recommendations for: {selected_movie}")

        recs = recommend_movies(selected_movie)

        for i, movie in enumerate(recs, 1):
            st.write(f"{i}. {movie}")

    else:
        st.error("Movie not found. Try another title.")

# Footer
st.markdown("---")
st.write("Built with ❤️ using Python, Streamlit, and Machine Learning")
