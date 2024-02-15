# Movie Recommender System
![](https://github.com/Shaishta-Anjum/Movie-Recommender-System/blob/main/Image%20File/Movie%20Recommender%20(1).png?raw=true)

This project implements a movie recommender system using machine learning techniques. The system suggests movies to users based on the similarity between movies in a dataset.

## Dataset

The project utilizes the [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata), which contains information about thousands of movies, including their titles, overviews, genres, keywords, cast, and crew.

## Steps

1. **Data Loading**: The project starts by loading the dataset files (`tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`) using pandas.

2. **Data Integration**: The two datasets are merged based on the movie title to create a single dataframe containing comprehensive movie information.

3. **Data Preprocessing**:
   - Irrelevant columns are dropped from the dataframe, retaining only relevant columns such as movie ID, title, overview, genres, keywords, cast, and crew.
   - Missing values are handled by dropping rows with missing data.
   - Duplicate entries are removed from the dataframe.

4. **Feature Engineering**:
   - The 'genres', 'keywords', 'cast', and 'crew' columns are processed to extract meaningful tags for each movie.
   - The tags are combined to form a single 'tags' column, which represents the combined features used for similarity calculation.
   - Only the top 3 actors from the cast and the director from the crew are included in the tags to focus on the most influential contributors to the movie.

5. **Text Vectorization**:
   - The tags are vectorized using the CountVectorizer from scikit-learn to convert them into numerical vectors.
   - Stop words are removed, and the maximum number of features is limited to improve performance.

6. **Stemming**:
   - Stemming is applied to reduce words to their root form, helping to normalize the text data and reduce noise.

7. **Cosine Similarity**:
   - Cosine similarity is calculated between the vectorized representations of movies to measure their similarity.
   - Similarity scores are computed for each pair of movies in the dataset.

8. **Recommendation Function**:
   - A function is implemented to recommend similar movies based on a given movie title.
   - The function retrieves the index of the input movie, calculates similarity scores, and returns a list of recommended movies sorted by similarity.

9. **User Interface**:
   - The recommendation functionality is integrated into a user-friendly interface using Streamlit.
   - Users can interact with the recommender system by selecting a movie from the dropdown menu and clicking the 'Recommend' button to receive personalized movie recommendations.
   - The front end of the app displays recommended movies with their titles and posters in a visually appealing format.

**Machine Learning Techniques**:
   - This project utilizes machine learning techniques, particularly natural language processing (NLP) and similarity calculations, to recommend movies based on their similarity to a given movie. The process includes data preprocessing, feature engineering, text vectorization, and cosine similarity calculations, which are common tasks in machine learning projects. The final recommendation functionality is implemented using a machine learning model to provide personalized movie suggestions to users.
