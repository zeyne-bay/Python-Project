#!/usr/bin/env python
# coding: utf-8

# In[1]:


def get_user_preference():
    #set the empty dictionaries
    user_preference={}
    movies={}
    # sort the file line by line
    for line in open('u.item'):
        # split the file and set to variables
        (movie_id, movie_title)=line.split('|')[0:2]
        # set the dictionary so id is the index and title is related to the index
        movies[movie_id]=movie_title
    # sort the file line by line
    for line in open('u.data'):
        # split file and set to variables
        (user_id, movie_id, rate)=line.split('\t')[0:3]
        # set the nested dictionary
        user_preference.setdefault(user_id, {})
        # define the nested dictionary
        user_preference[user_id][movies[movie_id]]=float(rate)
    # call the dictionary
    return user_preference 
def get_movie():
    # set the empty dictionaries
    movie_genres_and_watchers={}
    users={}
    genres={}
    # sort the file line by line
    for line in open('u.data'):
        # split file and set to variables
        (user_id, movie_id)=line.split('\t')[0:2]
        # set the dictionary
        users[movie_id]=user_id
    # sort the file line by line
    for line in open('u.item'):
        # split file and set to variables
        (movie_id, movie_title)=line.split('|')[0:2]
        genres = line.split('|')[5:26]
        # set the nested dictionary
        movie_genres_and_watchers.setdefault(movie_title, {})
        # define the nested dictionary
        movie_genres_and_watchers[movie_title]['genres']= [float(i) for i in genres]
        movie_genres_and_watchers.setdefault(movie_title, {})
        movie_genres_and_watchers[movie_title]['users']= users[movie_id] 
    # call the dictionary
    return movie_genres_and_watchers


# In[ ]:




