import streamlit as st
import pickle
import pandas as pd
import requests

# ==============================
# 1. Load Data and Model
# ==============================
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# ==============================
# 2. Helper Functions
# ==============================
def fetch_poster(movie_id):
    """Fetch movie poster from TMDb API."""
    try:
        url = url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=1234567890abcdef1234567890abcdef&language=en-US"
        response = requests.get(url)
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500" + poster_path
    except:
        return "https://via.placeholder.com/500x750?text=No+Image"
    return "https://via.placeholder.com/500x750?text=No+Image"

def recommend(movie):
    """Recommend top 5 similar movies."""
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    
    return recommended_movies, recommended_posters

# ==============================
# 3. Streamlit Frontend
# ==============================
st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")
st.title("🎬 Movie Recommendation System")
st.markdown("### Find movies similar to your favorite ones!")

selected_movie_name = st.selectbox(
    'Type or select a movie from the dropdown:',
    movies['title'].values
)

if st.button('Recommend 🎥'):
    names, posters = recommend(selected_movie_name)

    # Display in columns (side-by-side)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
