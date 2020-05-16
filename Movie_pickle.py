import pickle
from sklearn.externals import joblib
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

mdl=joblib.load('movie_recommender.pkl')
df=pd.read_csv('movie_name.csv')

#first i will create a pandas series of all the movie titles to access the
#movies using indices of the series in the function
from collections import defaultdict

indices=pd.Series(df['movie_title'])
indices=indices.str.replace("\xa0","")
#now we define the function which takes the movie title as input
    
def recommender(title,cosine_matrix=mdl):
    #initializing empty dictionary
        recommendations=defaultdict(list)
    #getting the index of the movie that matches the title
    #for title in query["movie"]:
        idx=0
        while True:
            if indices[idx]==title:
                break
            else:
                idx+=1
    #idx=indices[indices==title].index[0]
    #creating a series with the similarity scores
        sim_series=pd.Series(cosine_matrix[idx]).sort_values(ascending=False)
    #slicing the top 10 movies 
        top_10_index=list(sim_series.iloc[1:11].index)
    
    #The function will return the important data
        important_features=['movie_title','imdb_score','director_name','genres','plot_keywords','actors','movie_imdb_link']
        for i in top_10_index:
            for feature in important_features:
                recommendations[feature].append(df.xs(i)[feature])   
        return recommendations 
