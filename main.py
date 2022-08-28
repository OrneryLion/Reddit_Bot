import praw
from keys import client_id, secret, username, password

reddit = praw.Reddit(client_id=client_id,
                     client_secret=secret,
                     user_agent='Aaron',
                     username=username,
                     password=password)

subreddit = reddit.subreddit('HarryPotter')

top_subreddit = subreddit.top(limit=25)

for submission in top_subreddit:
    title = submission.title
    url = submission.url



    print(title)
    print(url)
    for comment in submission.comments:
        print(comment.body)
        break
