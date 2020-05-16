#!/usr/bin/env python
# coding: utf-8
In this part of the project we will make use of Natural Language Processing-a Machine Learning algorithm-and recommend the user movies similar to the one given as the input

# In[1]:


#the dataset we are using contains 5000 imdb movies of different genres,time periods and plots.
import pandas as pd
import numpy as np
from collections import defaultdict
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
df=pd.read_csv(r'https://query.data.world/s/qvc3lchzrpjbvcqegp3ababm7yzut5')
df
#importing the dataset

In this step we will perform data cleaning using different attribute available in pandas
# In[17]:


#dropping the columns we dont need
#dropping the movies with no plots and director's name because these,I believe are these are the two most
#important features to determine the similarity between movies
df=df.dropna(axis='rows',subset=['plot_keywords','director_name','movie_title']).reset_index(drop=True)
df=df[['director_name','actor_2_name','genres','actor_1_name','movie_title','actor_3_name','plot_keywords','movie_imdb_link','imdb_score']]


# In[18]:


df


# In[19]:


#merging the actor names into one and dropping the rest
df['actors']=df['actor_1_name']+'|'+df['actor_2_name']+'|'+df['actor_3_name']


# In[20]:


df=df.drop(['actor_1_name','actor_2_name','actor_3_name'],axis=1)
df


# In[21]:


#changing the order of the columns
#this step is not necessary,I just did it because I liked it in this order 
order=[2,5,1,0,3,6,4]
df=df[df.columns[order]]
df


# In[22]:


df=df.sort_values(by='imdb_score',ascending=False).reset_index(drop=True)
df
#sorting data based on descending imdb scores,highest first


# In[23]:


#nobody wants low rated imdb movies so removing movies with imdb<6
df=df.drop(df[df['imdb_score']<6].index)
df
#we started with 5000 movies and now we are left with 3413


# In[121]:


#removing spaces from actor and directors names to avoid misconception
#suppose we have Robert Duvall and Robert De Niro 
#Since their first names match our model will consider a similarity even if there isn't
df['director_name']=df['director_name'].str.replace(" ","")
df['actors']=df['actors'].str.replace(" ","")
df['movie_titles']=df['movie_title'].str.replace("\xa0","")
df
#now unless and untill the full name doesn't match our model will not consider them same

In this step I will create a new dataframe for vectorization:With the movie title and another column called bag of words
This contains the plot keywords,actor's and director's name and the genre of the movie all combined into one column which will be used for evaluating the score of the movies
# In[33]:



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

Next Step:MODELLING
# In[26]:


#generating the count matrix
count=CountVectorizer()
count_matrix=count.fit_transform(finaldata['bag_of_words'])

#making a cosine similarity matrix
cosine_matrix=cosine_similarity(count_matrix,count_matrix)
cosine_matrix

Now I will create a function that takes the movie title as input and gives the top 10 similar movies and their features as output
# In[133]:


#first i will create a pandas series of all the movie titles to access the
#movies using indices of the series in the function

indices=pd.Series(finaldata['Title'])
indices=indices.str.replace("\xa0","")
#now we define the function which takes the movie title as input
        
def recommend(title,cosine_matrix=cosine_matrix):
    #initializing empty dictionary
    recommendations=defaultdict(list)
    #getting the index of the movie that matches the title
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
        rec=pd.DataFrame(recommendations)   
    return rec 

#for dictionary return delete the last 2 lines and use -->return recommendations
  
        
    
    
    


# In[134]:


recommend('The Godfather')

