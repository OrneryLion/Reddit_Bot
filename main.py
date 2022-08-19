import praw
from keys import client_id, secret, username, password

reddit = praw.Reddit(client_id=client_id,
                     client_secret=secret,
                     user_agent='Aaron',
                     username=username,
                     password=password)

subreddit = reddit.subreddit('wallstreetbets')

top_subreddit = subreddit.new(limit=25)

for submission in top_subreddit:
    title = submission.title
    print(title)
