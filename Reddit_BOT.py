import praw
import requests
import config
import time
from database import setup_database,save_comment_id,is_comment_replied
import random

def bot_login():
    print("Logging in...")
    r = praw.Reddit(username=config.username,
                    password=config.password,
                    client_id=config.client_id,
                    client_secret=config.client_secret,
                    user_agent="ShitPoster616`s shitposter responder v0.1")
    print("Logged in")
    return r


def get_random_meme():
    url = "https://meme-api.com/gimme"
    response = requests.get(url).json()
    return response["url"] if "url" in response else None


def run_bot(r):
    print("Bot started")
    user="odinsergione"
    for comment in r.subreddit("popular").comments(limit=25):
        if not is_comment_replied(comment.id)  and not comment.author == r.user.me():#if the comment.id is not in my sets of id i memorized and to not reply to myself
            print("Shitposter: " + comment.body)
            comment_url = f"https://www.reddit.com{comment.permalink}"
            print(f"Comment URL: {comment_url}")

            meme_url = get_random_meme()
            if meme_url:
                try:
                    comment.reply(f"[Here’s a meme for you!]({meme_url})")
                    print(f"Replied with: {meme_url}")
                    save_comment_id(comment.id)
                    time.sleep(random.randint(10,30))#pause the bot for 10 sec policy of reddit
                    #test the code by commenting the above code and delete the coment to below code
                    # r.redditor(user).message("Test MEME",f"Here`s a test meme: {meme_url}")
                    #print(f"Sent test meme to {user}: {meme_url}")
                except Exception as e:
                    print(f"Failed to fetch meme: {e}")
    print("Bot finished and sleeping for 24 hours")
    time.sleep(86400)

#logging the bot a single time
setup_database()
r = bot_login()
replied_comments = set()# memorize the comments i already comment
while True:
    try:
        run_bot(r)
    except Exception as e:
        print(f"Bot encountered an error: {e}")
        time.sleep(300)#if bot got blocked wait 5 min
