import requests
import time
import os
import pandas as pd

users = {}
lf = 0
for file in os.listdir("../../contest_data/rating_changes/"):
    
    lf = file
    temp_df = pd.read_csv("../../contest_data/rating_changes/" + file)
    
    for ind, row in temp_df.iterrows():
        if temp_df["Handle"][ind] in users:   
            users[temp_df["Handle"][ind]].pop()
            users[temp_df["Handle"][ind]].append(temp_df["oldRating"][ind])
            users[temp_df["Handle"][ind]].append(temp_df["newRating"][ind])
        else:
            users[temp_df["Handle"][ind]] = [temp_df["oldRating"][ind]]
            users[temp_df["Handle"][ind]].append(temp_df["oldRating"][ind])

mlen = 10
bad = []
for k in users:
    if(len(users[k]) <= mlen):
        bad.append(k)
for b in bad:
    users.pop(b)
for k in users:
    users[k] = [users[k]]

savedf = pd.DataFrame(users)
savedf.to_csv(f"../../contest_data/user_time_series.csv")