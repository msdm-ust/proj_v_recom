import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

df1 = pd.read_csv('dev/20200313_integration_ver1/data/tmdb_5000_credits.csv')
df2 = pd.read_csv('dev/20200313_integration_ver1/data/tmdb_5000_movies.csv')
df3 = pd.read_table('dev/20200313_integration_ver1/data/success.txt',header=None)
df3 = np.array(df3[0])

df1.columns = ['id','title','cast','crew']
df2 = df2.merge(df1,on='id')
# df2 = df2.merge(df3[['id','cover']],on='id')

C = df2['vote_average'].mean()   # mean vote across the whole report
m = df2['vote_count'].quantile(0.9)  # minimum votes required to be listed in the chart
q_movies = df2.copy().loc[df2['vote_count'] >= m]

def weighted_rating(x,m=m,C=C):
    v = x['vote_count']
    R = x['vote_average']
    return (v/(v+m)*R)+(m/(m+v)*C)

q_movies['score'] = q_movies.apply(weighted_rating,axis = 1)
q_movies = q_movies.sort_values('score',ascending=False)
data_df = q_movies[['title_x','vote_count','vote_average','score']]
data_df.columns = ['title','vote_count','vote_average','score']

# Define a TF-IDF Vectorizer Object. Remove all stop words such as
# 'the' 'a'
tfidf = TfidfVectorizer(stop_words='english')
# deal with NA data
df2['overview'] = df2['overview'].fillna('')
tfidf_matrix = tfidf.fit_transform(df2['overview'])


cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(df2.index,index=df2['title_x']).drop_duplicates()


def get_recommendations(title, cosine_sim=cosine_sim,K=9):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:K+1]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]
    # Return the top 10 most similar movies

    res = df2['title_x'].iloc[movie_indices]
    data = []
    for index in res.index:
        movie = {}
        movie['rating'] = df2['vote_average'].iloc[index]
        movie['name'] = res[index]
       #movie['tagline'] = df2['tagline'].iloc[index]
       #movie['url'] = 'https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1583478382&di=784188562baefbb8cf353a75e22481bb&src=http://image14.m1905.cn/uploadfile/2016/0704/20160704045741804962.jpg'
        if int(df2['id'].iloc[index]) in df3:
            movie['url'] = 'img/pictures/%s.jpg' %(str(df2['id'].iloc[index]))
        else:
            movie['url'] = 'img/pictures/0.jpg'
        print(movie['name'], movie['url'])
        data.append(movie)
    return data


def get_random_movies(K = 10):
    # 选择前100的movies渲染首页
    samples = df2.sample(n=K)
    data = []
    for row in samples.itertuples():
        movie = {}
        movie['id'] = getattr(row,'id')
        movie['rating'] = getattr(row,'vote_average')
        movie['name'] = getattr(row,'title_x')
        #movie['tagline'] = getattr(row,'tagline')
        #movie['url'] = 'https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1583478382&di=784188562baefbb8cf353a75e22481bb&src=http://image14.m1905.cn/uploadfile/2016/0704/20160704045741804962.jpg'
        #movie['url'] = getattr(row,'cover')
        if int(movie['id']) in df3:
            movie['url'] = 'img/pictures/%s.jpg' % (str(movie['id']))
        else:
            movie['url'] = 'img/pictures/0.jpg'
        data.append(movie)
    return data


