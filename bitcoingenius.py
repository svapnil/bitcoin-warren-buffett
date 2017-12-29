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

#load recent already posted tweets into set
postedStatuses = tweepy.Cursor(api.user_timeline).items(100)
for status in postedStatuses:
    usedComments.add(status.text[:100])



#there is a problem where tweepy status.text will output a concatonated version of the target
#which is an issue for the set that holds individual tweets. To fix, i will only add the first
#100 characters of each tweet to the set to make sure i can properly identify duplicates

count = 0

#loop for the code in the Script
while(True):
    for submission in reddit.subreddit('bitcoin').controversial('day'):

        try:
            firstComment = submission.comments[0].body
        except IndexError as ie:
            print(submission.title + ' doesnt have a comment - skipping')
            continue

        if firstComment[:100] in usedComments or len(firstComment) > 280:
            continue
        else:

            try:
                api.update_status(firstComment)
                print(firstComment)
            except Exception as e:
                print('An exception occured when tweeting: ' + firstComment)
                print('Moving on..')
                continue

            usedComments.add(firstComment[:100])
            break

    time.sleep(1800)#Tweet every 30 minutes

    count = count + 1

    #api.update_status() code to update status
