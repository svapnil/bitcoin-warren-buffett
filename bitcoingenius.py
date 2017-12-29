
import tweepy, praw, time, sys #tweepy for twitter, PRAW for reddi

from userauthinfo import ACCOUNTPRIVATEINFO #class that stores private info to use APIs

#corresponding information from your Twitter application:
auth = tweepy.OAuthHandler(ACCOUNTPRIVATEINFO.TWITTER_CONSUMER_KEY, ACCOUNTPRIVATEINFO.TWITTER_CONSUMER_SECRET)
auth.set_access_token(ACCOUNTPRIVATEINFO.TWITTER_ACCESS_KEY, ACCOUNTPRIVATEINFO.TWITTER_ACCESS_SECRET)
api = tweepy.API(auth)
#twitter bot is ready for action

#make reddit instance
reddit = praw.Reddit(client_id= ACCOUNTPRIVATEINFO.REDDIT_CLIENT_ID,
                     client_secret= ACCOUNTPRIVATEINFO.REDDIT_CLIENT_SECRET,
                     user_agent= ACCOUNTPRIVATEINFO.REDDIT_USER_AGENT)

usedComments = set()
count = 0

#loop for the code in the Script
while(True):
    for submission in reddit.subreddit('bitcoin').controversial('day'):

        firstComment = submission.comments[0].body
        if firstComment in usedComments or len(firstComment) > 280:
            continue
        else:
            api.update_status(firstComment)
            print(firstComment)
            usedComments.add(firstComment)
            break


    time.sleep(1800)#Tweet every 30 minutes

    count = count + 1

    #api.update_status() code to update status
