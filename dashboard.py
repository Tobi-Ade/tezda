import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#load data
df = pd.read_csv("cleaned_data.csv")

# Streamlit Dashboard Header
st.title("Movie Insights Dashboard")
st.subheader("Explore the key insights of the movie dataset")

# Top 10 Movies by Revenue or Vote Average
st.header("Top 10 Movies")

# Choose whether to display by revenue or vote average
top_movies = df.nlargest(10, 'revenue')
# st.write("Top 10 Movies by Revenue", top_movies[['original_title', 'revenue']])

# Plotting using Plotly (Interactive)
fig = px.bar(top_movies, x='original_title', y='revenue', title='Top 10 Movies by Revenue')
st.plotly_chart(fig)
    


# Distribution of genres
st.header("Distribution of genres")
genre_counts = genres_df = df['genres'].str.split(' ').explode().value_counts()

# Plotting using 
fig = px.bar(genre_counts, x=genre_counts.index, y=genre_counts.values, title="Distribution of genress", labels={'x': 'genres', 'y': 'Count'})
st.plotly_chart(fig)


# Interactive Filter for Year or Runtime
st.header("Filter by Year or Runtime")

# Year filter
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')  # Convert to datetime
df['release_year'] = df['release_date'].dt.year
year_filter = st.slider("Select Year", int(df['release_year'].min()), int(df['release_year'].max()), (1916, 2017))
filtered_by_year = df[df['release_year'].between(year_filter[0], year_filter[1])]
st.write(f"Movies released between {year_filter[0]} and {year_filter[1]}", filtered_by_year)

# Runtime filter
runtime_filter = st.slider("Select Runtime (in minutes)", int(df['runtime'].min()), int(df['runtime'].max()), (0, 150))
filtered_by_runtime = df[df['runtime'].between(runtime_filter[0], runtime_filter[1])]
st.write(f"Movies with runtime between {runtime_filter[0]} and {runtime_filter[1]} minutes", filtered_by_runtime)
