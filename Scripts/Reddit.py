import praw
import csv
import os
from dotenv import load_dotenv

load_dotenv("Python_credentials.env")

#Reddit API Credentials 
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
)

#Check if authentication works
print(f"Authenticated as: {reddit.user.me()}")

#Searche mechanism for Reddit
subreddit = reddit.subreddit("all")  
search_query = "healthcare OR hospital OR medicine OR doctor OR patient OR treatment OR insurance"


#Fetch healthcare-related posts
posts = []
for submission in subreddit.search(search_query, limit=200):
    posts.append([submission.title, submission.score, submission.url])

#Save to CSV
csv_filename = "reddit_healthcare_posts.csv"  
with open(csv_filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Score", "URL"])  
    writer.writerows(posts)

print(f"✅ Saved {len(posts)} healthcare posts to {csv_filename}")
