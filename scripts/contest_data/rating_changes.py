import requests
import time
import os
import pandas as pd

official_contests = requests.get("https://codeforces.com/api/contest.list?gym=false").json()

for contest in official_contests["result"]:

    time.sleep(3)

    id = contest["id"]
    rating_changes = requests.get(f"https://codeforces.com/api/contest.ratingChanges?contestId={id}").json()

    if rating_changes["status"] == "FAILED":
        print(f"Contest {id} has failed with error: {rating_changes['comment']}")
        continue

    rating_changes = rating_changes["result"]

    #We only care about: name, rank, oldRating, newRating

    data = []

    for competitor in rating_changes:
        handle = competitor["handle"]
        old_rating = competitor["oldRating"]
        new_rating = competitor["newRating"]
        print(handle + " " + str(old_rating) + " " + str(new_rating))

        data.append([handle, old_rating, new_rating])

    df = pd.DataFrame(data, columns = ['Handle', 'oldRating', 'newRating'])
    df.to_csv(f"../../contest_data/rating_changes/{id}.csv")
