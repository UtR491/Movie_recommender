#!/usr/bin/env python
# coding: utf-8
In this part of the project we will make a Book recommender using Machine Learning Algorithms
# In[4]:


#importing the datasets
#the first one contains the metadata
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import seaborn as sns
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np
df=pd.read_csv(r'C:\Users\HP\Desktop\books.csv')
df=df.dropna(axis='rows',subset=['original_title']).reset_index(drop=True)
df


# In[7]:


#relevant columns are taken
df=df[['original_title','authors','book_id','image_url','original_publication_year','average_rating','ratings_count']]
df


# In[8]:


#sorting based on book_id
df=df.sort_values(by='book_id',ascending=True).reset_index(drop=True)
df


# In[9]:


#the second dataset contains the book_id of the books the user has recommended
to_read=pd.read_csv(r'C:\Users\HP\Desktop\to_read.csv')
to_read
#these are some books that the user has marked to read


# In[10]:


#the most important dataset which contains the ratings each book has received by the users
ratings=pd.read_csv(r'C:\Users\HP\Desktop\ratings.csv')
ratings
#the ratingss are out of 5

We will proceed to erase those duplicated ratings(if any) from the rating table: for those user-book pairs that have more than 1 rating we will then keep only one record, indicating the average of the given ratings.
# In[117]:


# The following table will show which pair of user-book have more than 1 rating in the dataset: 

userRatesPerBookCount = ratings.groupby(['user_id', 'book_id'], as_index = False).count().sort_values('rating', ascending = False)
userRatesPerBookCount.head(15)


# In[118]:


# Let's check if this is true:

ratings[(ratings.user_id == 3204) & (ratings.book_id == 8946)]


# In[119]:


# Here I calculate the rating mean per user and book, so that I can later replace the mean to the rating value
# and get rid of the duplicates rows

userRatesPerBookMean = ratings.groupby(['user_id', 'book_id'], as_index = False).mean().round(0).sort_values('rating', ascending = False)
userRatesPerBookMean.head(15)


# In[120]:


# We create a table grouped by user and book pair, calculating mean and number of rating that a user has made for the
# same book

ratings['count'] = ratings['rating']

userRatesPerBook = ratings.groupby(['user_id', 'book_id'], as_index = False)                    .agg({'rating' : 'mean', 'count' : 'count'})                    .rename(columns = {'rating':'mean'})                    .sort_values('count', ascending = False)

ratings = ratings.drop(['count'], axis = 1)
            
userRatesPerBook['mean'] = userRatesPerBook['mean'].round(0)
userRatesPerBook


# In[121]:




ratings = pd.merge(ratings, userRatesPerBook, on = ['user_id', 'book_id'])
ratings.head()
ratings.sort_values('count', ascending = False).head(15)


# In[122]:


#dropping the duplicates

ratings = ratings.drop_duplicates(subset = ['book_id', 'user_id'], keep = 'first', inplace = False)                                  .sort_values('count', ascending = False)
ratings = ratings.drop(['rating', 'count'], axis = 1)
ratings


# In[123]:


ratings.describe()
#we have a total of approx 980K ratings with a mean of 3.8
#also 75% of the books are rated 5 which is the maximum rating


# In[124]:


get_ipython().run_line_magic('matplotlib', 'inline')
df['average_rating'].hist(bins=50)
#most book have an average rating in the range of 4-4.5


# In[125]:


sns.jointplot(x='average_rating', y='ratings_count', data=df)
#From the diagram it is clear that most movies 
#have few ratings. Movies with most ratings are those that are most famous.


# In[126]:


#ratings per user
ratings.columns = ['book_id', 'user_id', 'rating']
ratesPerUser = ratings[['user_id', 'rating']].groupby(['user_id'], as_index = False)                       .count()                       .rename(columns = {'rating' : 'totalRatings'})                      .sort_values('totalRatings', ascending = False)
ratesPerUser


# In[127]:


plt.rcParams['figure.figsize'] = [20, 6]
plt.hist(ratesPerUser['totalRatings'], bins = 50)
plt.xticks(np.arange(min(ratesPerUser['totalRatings']), max(ratesPerUser['totalRatings'])+1, 4.0))
plt.show()

The above plot shows that majority of the users have rated only 1-15 movies,in order to make our recommender accurate we will consider the users who havee rated atleast 20 of the 10K books


# In[128]:


ratings = pd.merge(ratings, ratesPerUser, on = ['user_id'])
ratings.sort_values('totalRatings', ascending = False).head(10)


# In[129]:


# Keeping only users with more than a 'minimum' of ratings
minimumRatings = ratings.totalRatings <= 20
np.sum(minimumRatings)


# In[130]:


ratings = ratings[-minimumRatings]
#total ratings 
#remaining users and books
print(str(len(ratings))+'\n'+str(len(ratings.user_id.unique()))+'\n'+str(len(ratings.book_id.unique())))

Doing the same process with books and removing books with less than 30 ratings
# In[131]:


ratesPerBook = ratings[['book_id', 'rating']].groupby(['book_id'], as_index = False)                       .count()                       .rename(columns = {'rating' : 'receivedRatings'})                       .sort_values('receivedRatings', ascending = False)

ratesPerBook.tail()


# In[132]:


plt.rcParams['figure.figsize'] = [20, 6]
plt.hist(ratesPerBook['receivedRatings'], bins = 50)
plt.xticks(np.arange(min(ratesPerBook['receivedRatings']), max(ratesPerBook['receivedRatings'])+1, 4.0))
plt.show()


# In[133]:


ratings = pd.merge(ratings, ratesPerBook, on = ['book_id'])


# In[134]:


# Keeping only books with more than a 'minimum' of ratings received

minimumReceived = ratings.receivedRatings < 30
np.sum(minimumReceived)


# In[135]:


ratings = ratings[-minimumReceived]

print(str(len(ratings))+'\n'+str(len(ratings.user_id.unique()))+'\n'+str(len(ratings.book_id.unique())))

Showing the top N recommended movies based on rating
# In[137]:


#showingTitles = pd.merge(ratings, df[['book_id', 'authors', 'original_title']], how = 'left', left_on = ['book_id'], right_on = ['book_id'])
#showingTitles = showingTitles.groupby(['book_id'], as_index = False) #\
                      
#showingTitles.sort_values('rating', ascending = False).head(10)


# # 1) CONTENT BASED FILTERING(TAG BASED)
The tags dataset contains format-free definition, which include a vast variety of tags. Most of them are not saying much of the book itself and its contect or characteristics (e.g. 'to-read', 'favourite', 'book-I-own', 'made-me-cry', etc). For this reason I have decide to include only the tags that are representative of the book 'genre' according to Goodreads itself: the tags used in fact are scraped from their genre section and contain a vast variety of tags. The others have been filtered out.
# In[12]:


tags=pd.read_csv(r'C:\Users\HP\Desktop\tags.csv')
booktags=pd.read_csv(r'C:\Users\HP\Desktop\book_tags.csv')


# In[13]:


showingTag = pd.merge(booktags, tags, on = 'tag_id')
showingTag=showingTag[['book_id','tag_id','tag_name']]
showingTag.sort_values('book_id').head(25)


# In[14]:


#sorting the most used tags
mostUsedTags = showingTag.groupby(['tag_name'], as_index = False)                       .agg({'book_id' : 'count'})                       .rename(columns = {'book_id' : 'number'})                       .sort_values('number', ascending = False)
mostUsedTags.head(10)


# In[15]:


genres=pd.read_csv(r'C:\Users\HP\Desktop\genres.csv')
genres


# In[17]:


genreList = genres['tag_name'].tolist()
genreTags = tags.loc[tags['tag_name'].isin(genreList)]
len(genreTags)
#832 tags are the most common genre tags


# In[18]:


genreTags.head()


# In[19]:


mostCommonTags = pd.merge(booktags, genreTags, on = ['tag_id'])
stringedTags = mostCommonTags.groupby('book_id')['tag_name'].apply(lambda x: "%s" % ' '.join(x)).reset_index()
stringedTags


# In[20]:


book=pd.merge(df,stringedTags,on=['book_id'])
book


# In[21]:


#removing spaces & ','  from authors names
book['authors'] = book['authors'].astype('str').apply(lambda x: str.lower(x.replace(" ", "")))
book['authors'] = book['authors'].astype('str').apply(lambda x: str.lower(x.replace(",", " ")))
book


# In[22]:


Title=book['original_title']
finaldata=pd.DataFrame(Title)
finaldata['Title']=finaldata['original_title']
finaldata=finaldata.drop('original_title',axis=1)
#bag of words
finaldata['bag_of_words']=book['authors']+' '+book['tag_name']
#Converting the text to lowercase to avoid duplication and removing '|'
finaldata['bag_of_words']=finaldata['bag_of_words'].str.lower()
finaldata=finaldata.fillna(' ')
finaldata
#now our dataset is ready for modelLing


# In[23]:


#generating the count matrix
count=CountVectorizer()
count_matrix=count.fit_transform(finaldata['bag_of_words'])

#making a cosine similarity matrix
cosine_matrix=cosine_similarity(count_matrix,count_matrix)
cosine_matrix

Now I will create a function that takes the movie title as input and gives the top 10 similar movies and their features as output
# In[24]:


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
    important_features=['original_title','average_rating','authors','image_url','original_publication_year']
    for i in top_10_index:
        for feature in important_features:
       
          recommendations[feature].append(book.xs(i)[feature])
        rec=pd.DataFrame(recommendations)   
    return rec 

#for dictionary return delete the last 2 lines and use -->return recommendations
  
        
    
    
    


# In[28]:


recommend('Wait for It')


# In[30]:


import pickle
from sklearn.externals import joblib
filename='book_recommender.pkl'
joblib.dump(cosine_matrix,filename)

