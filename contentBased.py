import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


df= pd.read_csv("final.csv" )
df=df[df["soup"].notna()]

count= CountVectorizer(stop_words="english")
count_matrix= count.fit_transform(df["soup"])

cosins_sim= cosine_similarity(count_matrix)

df=df.reset_index()
indices=pd.Series(df.index,index=df["title_x"])

def getrecommendations(title):
  idx=indices[title]
  sim_score=list(enumerate(cosins_sim[idx]))
  sim_score=sorted(sim_score, key=lambda x:x[1],reverse=True)
  # print(sim_score)
  moviesname=sim_score[1:11]
  moviesindices=[i[0] for i in moviesname]
  return df[["title_x","movieposter","release_date","runtime","overview","vote_average"]].iloc[moviesindices].values.tolist()
  
