import streamlit as st
import pickle
import pandas as pd
import requests
import time

# Define the function to set background image

def set_bg_hack_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url("https://raw.githubusercontent.com/Shaishta-Anjum/Movie-Recommender-System/main/Image%20File/bg8.png");
             background-size: cover;
         }}
         </style>
         """,
        unsafe_allow_html=True
    )

# Call the function to set the background image
set_bg_hack_url()

# Title of the app
st.title('Movie Recommender System')

# Load the files from pickle
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Function to fetch movie poster
def fetch_poster(movie_id):
    """
    Fetches the poster URL for a given movie ID from TMDB API.
    """
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# Function to recommend similar movies based on user selection
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:11]:
        # Fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

# Dropdown to select movie
movie_list = movies['title'].values
selected_movie = st.selectbox(
    'Discover Your Next Movie Adventure!',
    movies['title'].values)

# Spinner while loading recommendations
with st.spinner('Wait for it...'):
    time.sleep(0.8)

# Button to trigger movie recommendation
if st.button('Recommend'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    num_recommendations = len(recommended_movie_names)
    num_rows = (num_recommendations + 1) // 2
    for i in range(num_rows):
        columns = st.columns(2)
        for j in range(2):
            index = i * 2 + j
            if index < num_recommendations:
                with columns[j]:
                    # Apply HTML styling to the text
                    st.markdown(f'<p style="font-family: sans-serif; font-size: 25px; font-weight: bold; text-align: center;">{recommended_movie_names[index]}</p>', unsafe_allow_html=True)
                    st.image(recommended_movie_posters[index])
