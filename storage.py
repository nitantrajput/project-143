import pandas as pd
import numpy as np
import csv
all_movies=[]

with open("final.csv") as f:
    reader= csv.reader(f)
    data= list(reader)
    all_movies=data[1:]

liked_movies=[]
non_liked_movies=[]
didnot_match_movies=[]