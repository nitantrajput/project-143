from itertools import groupby
from storage import all_movies,non_liked_movies,didnot_match_movies,liked_movies
from demgraphic import output
from contentBased import getrecommendations
from flask import Flask, jsonify,request

app= Flask(__name__)

@app.route("/get-movies")
def get_movies():
    moviedata={
     "title":all_movies[0][19],
     "movieposter":all_movies[0][27],
     "duration":all_movies[0][15] or "N/A",
     "overview":all_movies[0][9],
     "releaseDate":all_movies[0][13] or "N/A",
     "rating":all_movies[0][20],
    }
    return jsonify({
        "data":moviedata,
        "status":"success"
    }),200

@app.route("/likedmovies",methods=["POST"])
def likedmovies():
   movie=all_movies[0]
   liked_movies.append(movie)
   all_movies.pop(0)
   return jsonify({
    "status":"success"
    }), 200



@app.route("/nonlikedmovies",methods=["POST"])
def nonliked_movies():
    movie=all_movies[0]
    non_liked_movies.append(movie)
    all_movies.pop(0)
    return jsonify({
         "status":"success"
    }), 200


@app.route("/didNotWatch",methods=["POST"])
def didNot_Match():
    movie=all_movies[0]
    didnot_match_movies.append(movie)
    all_movies.pop(0)
    return jsonify({
         "status":"success"
    }), 200

@app.route("/popularMovies")
def popular_movies():
    movie_data=[]
    for i in output:
        d={
           "title":i[0],
           "movieposter":i[1],
            "duration":i[3] or "N/A",
            "overview":i[4],
            "releaseDate":i[2] or "N/A",
            "rating":i[5],  
        }
        movie_data.append(d)
    return jsonify({
        "data":movie_data,
        "status":"success"
    }),200


@app.route("/recommendations")
def get_recommendations():
    all_recommend_movies=[]
    for i in liked_movies:
        output=getrecommendations(i[19])
        for j in output:
            all_recommend_movies.append(j)
    import itertools
    all_recommend_movies.sort()
    all_recommend_movies= list( all_recommend_movies for all_recommend_movies,_ in itertools.groupby(all_recommend_movies))
    # print(all_recommend_movies)
    movie_data=[]
    for k in all_recommend_movies:
        d={
            "title":k[0],
            "movieposter":k[1],
            "duration":k[2] or "N/A",
            "overview":k[3],
            "releaseDate":k[4] or "N/A",
            "rating":k[5],  
        }
        movie_data.append(d)
    return  jsonify({
        "data":movie_data,
        "status":"success"
    }), 200

if __name__ == ("__main__"):
    app.run(debug=True,port=5000,host="localhost")