# Flask library
from flask import Flask, request, jsonify
import csv

with open("movies.csv") as f:
    reader= csv.reader(f)
    data= list(reader)
    # print(len(data))
    # print(data)
    all_movies=data[1:]
    headers=data[0]
  

headers.append("movieposter")
print(len(headers))


with open("movie_links.csv",encoding="utf8") as f:
    reader= csv.reader(f)
    data=list(reader)
    # print(len(data))
    allMovies_link=data[1:]
    headers2= data[0]
    # print(len(headers2))
    # print(all_movies)

with open("final.csv","a+",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(headers)


for i in all_movies:
    poster=any(i[8] in j for j in allMovies_link)
    #print(poster)
    if poster:
        for j in allMovies_link:
            if i[8] == j[0]:
                i.append(j[1])
                if len(i) == 28:
                    with open("final.csv","a+",newline="") as f:
                        writer= csv.writer(f)
                        writer.writerow(i)





   


