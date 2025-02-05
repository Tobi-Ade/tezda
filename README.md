### Approach to Building Recommnder system for movie dataset 
The first step was to explore the data. i found the ffg insights during exploration 
- The homepage column contained too many missing values, therefore i dropped it
- The numerical columns contained no missing values on initial viewing, but digging deeper, you find a lot of zero values, which we can equate to null and these had to be taken care of.
- The budget and revenue columns had over 1000 missing values (0), ideally I would drop them, but as they were needed for further analysis (dashboards) I let them be replaced by the median value 
- I explored correlation between columns and found that budget and revenue, as well as revenue and average voting had the most postive correlation
- Every feature was positively correlated with one another
- During analysis, I found a lot of outliers, especially within the movie budget, but this can be traced to a lot of values being 0 and therefore would be solved by imputation if we are able to get the right values


### Building the recommender 
After analysis and cleaning, the next step was building the recommender, and the follwowing steps were followed: 
- Feature engineering to create the combined_features feature, which took relevant features and made them one
- vectorize this feature and compute item-item similarity with it using cosine similarity
- write a function that takes a movie name and returns the most similar movies from our dataset after computing similarity

### Dashboard 
 I built my dashboards with streamlit and plotly to make them interactive


### How to run the code
- clone the repostitory to your local machine
- run ```pip install -r requirements.txt```
- run the notebooks in the following order: data_cleaning.ipynb -> recommendations.ipynb
- you can then run the dashboard.py file using the command ```streamlit run dashboard.py```

### Test the recommender 
- in your command line or terminal, run `python recommender.py`
- Enter the name of the movie and hit enter
- Get recommendations

### Note: Yet to be implemeted due to time constraint:
- Proper error handling
- Sorting input movie titles to match structure of movie titles in dataset
- proper training and testing splits
- Evaluation 