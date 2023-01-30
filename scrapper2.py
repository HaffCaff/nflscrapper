# Read-only instance
import praw as praw
import pandas as pd
from IPython.display import display
from praw.models import MoreComments
import numpy as np
import matplotlib.pyplot as plt

reddit_read_only = praw.Reddit(client_id="",  # your client id
                               client_secret="",  # your client secret
                               user_agent="")  # your user agent
# URL of the post
url = "https://www.reddit.com/r/nfl/comments/10olgzg/game_thread_cincinnati_bengals_124_at_kansas_city/"

# Creating a submission object
submission = reddit_read_only.submission(url=url)

post_comments = []
words = []
u_words = []
counts = []
keywords = ["chiefs","kc", "bengals", "mahomes", "penalty", "burrow", "mixon", "kelce", "boyd", "MSV", "injuries","higgins","chase"]

for comment in submission.comments:
    if type(comment) == MoreComments:
        continue

    post_comments.append(comment.body)

for comment in post_comments:
    res = comment.lower().split()
    for i in res:
        words.append(i)

words.sort()
u_words = set(words)

for i in u_words:
    counts.append(words.count(i))

res = dict(zip(u_words, counts))

# print({k: v for k, v in sorted(res.items(), key=lambda item: item[1])})

finres = {}

for word in keywords:
    if word in res.keys():
        finres[word] = res[word]

print(finres)

names = list(finres.keys())
values = list(finres.values())

plt.bar(range(len(finres)), values, tick_label=names)
plt.title("Reddit Comments Buzzwords")
plt.show()
