#import libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity 

#load cleaned dataset 
df = pd.read_csv("./cleaned_data.csv")
df.head()

# Vectorize combined features column using TF-IDF 
tfidfvec = TfidfVectorizer() 
tfidf_matrix = tfidfvec.fit_transform((df["combined_features"])) 

# compute cosine similarity between vectors 
sim_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix) 

def recommendations(movie_title, sim=sim_matrix): 	
    """
    This function takes in the title of a movie and returns recommendations for the input movie
    params: movie title, similarity matrix
    returns: top 5 recommendations based on similarity score
    rtype: list    
    """
    
    # Find the index of the movie that matches the movie name
    idx = df[df['original_title'] == movie_title].index[0]
    
    # get the similarity score between target movie and every other movie
    sim_scores = list(enumerate(sim[idx]))
    
    # Sort the movies based on the similarity scores (in descending order)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the top 5 most similar movies (excluding the movie itself)
    top_5_movies = sim_scores[1:6]
    
    # Get movie titles for the top 5 similar movies
    recommended_movies = [df['original_title'].iloc[i[0]] for i in top_5_movies]
    
    return recommended_movies

if __name__ == '__main__':
    print(f"enter movie title:")
    movie_title = str(input())
    recommender = recommendations(movie_title)
    print(recommender)