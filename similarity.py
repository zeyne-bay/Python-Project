#!/usr/bin/env python
# coding: utf-8

# In[8]:


from math import*
from load_data import*
#calculate euclidean distance
def euclidean_distance(x,y):
    total = 0
    for a in x:
        for b in y:
            if(a==b):
                d=pow(x[a]-y[b],2)
                total+=d        
    return sqrt(total) 
#calculate manhattan distance
def manhattan_distance(x,y):
    total = 0
    for a in x:
        for b in y:
            if(a==b):
                d=abs(x[a]-y[b])
                total+=d
    return total
#calculate cosine similarity    
def cosine_similarity(x,y):
    numerator = 0
    powa=0
    powb=0
    for a in x:
        for b in y:
            if(a==b):
                powa+=pow(x[a],2)
                powb+=pow(y[b],2)
                d=x[a]*y[b]
                numerator+=d
                denominator=round(sqrt(powa),3)*round(sqrt(powb),3)
    return round(numerator/float(denominator),3)
#calculate jaccard similarity     
def jaccard_similarity(x,y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality/float(union_cardinality)
#calculate pearson similarity
def pearson_similarity(x,y):
    i = 0
    dev_x=[]
    dev_y=[]
    totalx = 0
    totaly = 0
    for a in x:
        for b in y:
            if a==b:
                totalx += x[a]
                totaly += y[b]
                i+=1
    mean_x = totalx/i
    mean_y = totaly/i
    total_dev = 0
    total_dev_x = 0
    total_dev_y = 0
    for a in x:
        for b in y:
            if a==b:
                total_dev += (x[a] - mean_x)*(y[b] - mean_y)
                total_dev_x += pow(x[a] - mean_x,2)
                total_dev_y += pow(y[b] - mean_y,2)
    return total_dev/sqrt(total_dev_x*total_dev_y)
#calculate mean
def mean(x):
    return sum(a for a in x)/len(x)
#finding similarity between two users
def user_similarity(mtrc,fuser,suser):
    a=get_user_preference()
    mtrc=mtrc.lower() 
    if mtrc=="euclidean":
        return euclidean_distance(a[fuser],a[suser])
    elif mtrc=="manhattan":
        return manhattan_distance(a[fuser],a[suser])
    elif mtrc=="cosine":
        return cosine_similarity(a[fuser],a[suser])
    elif mtrc=="jaccard":
        return jaccard_similarity(a[fuser],a[suser])
    elif mtrc=="pearson":
        return pearson_similarity(a[fuser],a[suser])
    else:
        print("incorrect Data!")
        main()
#finding similarity between two movies        
def movie_similarity(mtrc,fmovie,smovie):
    m=get_movie()
    mtrc=mtrc.lower()
    x=m[fmovie]['genres']
    y=m[smovie]['genres']
    if mtrc=="euclidean":
        return sqrt(sum(pow(a-b,2) for a,b in zip(x,y)))
    elif mtrc=="manhattan":
        return sum(abs(a-b) for a,b in zip(x,y)) 
    elif mtrc=="cosine":
        sqrt_x=round(sqrt(sum([a*a for a in x])),3)
        sqrt_y=round(sqrt(sum([a*a for a in y])),3)
        num = sum(a*b for a,b in zip(x,y))
        denom = sqrt_x*sqrt_y
        return round(num/float(denom),3)
    elif mtrc=="jaccard":
        intersect = len(set.intersection(*[set(x), set(y)]))
        uni = len(set.union(*[set(x), set(y)]))
        return intersect/float(uni)
    elif mtrc=="pearson":
        total_dev = sum((a-mean(x))*(b-mean(y)) for a,b in zip(x,y))
        total_dev_x = sum(pow(a - mean(x),2) for a in x)
        total_dev_y = sum(pow(b - mean(y),2) for b in y)
        return total_dev/sqrt(total_dev_x*total_dev_y)
    else:
        print("incorrect Data!")
        main()
 
    

                                                                 
                                                                     


# In[ ]:




