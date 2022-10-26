import requests
import time
import os
import pandas as pd

users = {}
lf = 0

official_contests = requests.get("https://codeforces.com/api/contest.list?gym=false").json()

for contest in reversed(official_contests["result"]):
    
    lf = contest["id"]
    try:
        temp_df = pd.read_csv("../../contest_data/rating_changes/" + str(contest["id"]) + ".csv")
    except:
        print(f"Unable to read file {lf}.csv")
        continue
    for ind, row in temp_df.iterrows():
        if temp_df["Handle"][ind] in users:   
            users[temp_df["Handle"][ind]].pop()
            users[temp_df["Handle"][ind]].append(temp_df["oldRating"][ind])
            users[temp_df["Handle"][ind]].append(temp_df["newRating"][ind])
        else:
            users[temp_df["Handle"][ind]] = [temp_df["oldRating"][ind]]
            users[temp_df["Handle"][ind]].append(temp_df["oldRating"][ind])
    print(f"Successfully read file {lf}.csv")

for k in users:
    users[k] = [users[k]]

savedf = pd.DataFrame(users)
savedf.to_csv(f"../../contest_data/user_time_series.csv")
