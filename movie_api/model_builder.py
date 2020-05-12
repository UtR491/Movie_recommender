#the dataset we are using contains 5000 imdb movies of different genres,time periods and plots.
import pandas as pd
import numpy as np
from collections import defaultdict
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

df=pd.read_csv(r'movie_name.csv')

#importing the dataset
#dropping the columns we dont need
#dropping the movies with no plots and director's name because these,I believe are these are the two most
#important features to determine the similarity between movies
df=df.dropna(axis='rows',subset=['plot_keywords','director_name','movie_title']).reset_index(drop=True)
df=df[['director_name','actor_2_name','genres','actor_1_name','movie_title','actor_3_name','plot_keywords','movie_imdb_link','imdb_score']]
#merging the actor names into one and dropping the rest
df['actors']=df['actor_1_name']+'|'+df['actor_2_name']+'|'+df['actor_3_name']
#changing the order of the columns
#this step is not necessary,I just did it because I liked it in this order 
order=[2,5,1,0,3,6,4]
df=df[df.columns[order]]
df
df=df.sort_values(by='imdb_score',ascending=False).reset_index(drop=True)
df
#sorting data based on descending imdb scores,highest first
#nobody wants low rated imdb movies so removing movies with imdb<6
df=df.drop(df[df['imdb_score']<6].index)
df
#we started with 5000 movies and now we are left with 3413
#removing spaces from actor and directors names to avoid misconception
#suppose we have Robert Duvall and Robert De Niro 
#Since their first names match our model will consider a similarity even if there isn't
df['director_name']=df['director_name'].str.replace(" ","")
df['actors']=df['actors'].str.replace(" ","")
df['movie_titles']=df['movie_title'].str.replace("\xa0","")
df.to_csv('movie_name.csv')
df
#now unless and untill the full name doesn't match our model will not consider them same

Title=df['movie_title']
finaldata=pd.DataFrame(Title)
finaldata['Title']=finaldata['movie_title']
finaldata=finaldata.drop('movie_title',axis=1)
#bag of words
finaldata['bag_of_words']=df['actors']+' '+df['plot_keywords'] +' '+df['genres']+' '+df['director_name']
#Converting the text to lowercase to avoid duplication and removing '|'
finaldata['bag_of_words']=finaldata['bag_of_words'].str.lower()
finaldata['bag_of_words']=finaldata['bag_of_words'].str.replace("|"," ")
#setting the title column as the index 
#finaldata.set_index('Title',inplace=True,drop=True)
finaldata=finaldata.fillna(' ')
finaldata
#now our dataset is ready for modelLing

#generating the count matrix
count=CountVectorizer()
count_matrix=count.fit_transform(finaldata['bag_of_words'])

#making a cosine similarity matrix
cosine_matrix=cosine_similarity(count_matrix,count_matrix)
cosine_matrix

import pickle
from sklearn.externals import joblib
filename='movie_recommender.pkl'
joblib.dump(cosine_matrix,filename)
