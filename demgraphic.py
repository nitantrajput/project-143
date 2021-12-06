import pandas as pd
import numpy as np
print(1)
df= pd.read_csv("final.csv")
print(2)
C= df["vote_average"].mean()
m=df["vote_count"].quantile(0.9)

qmovies=df.copy().loc[df["vote_count"]>=m]
def weightRating(x,m=m,C=C):
  v=x["vote_count"]
  R= x["vote_average"]
  return (v/(v+m)*R)+(m/(v+m)*C)
qmovies["score"]=qmovies.apply(weightRating,axis=1)
qmovies=qmovies.sort_values("score",ascending=False)

output=qmovies[["title_x","movieposter","release_date","runtime","overview","vote_average"]].values.tolist()
print(output)
