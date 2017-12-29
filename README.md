# bitcoin-warren-buffett

### https://twitter.com/bitbotvestor

This twitter bot makes comments and predictions about Bitcoin just as well as your amateur cryptocurrency enthusiast.

(Which may or may not be accurate)

The script takes the top comments from a controversial post on */r/Bitcoin* and tweets one every 30 minutes. These comments typically are from edgy yet amateur and highly optimistic redditors, which make them great content to reflect on the bubble Bitcoin is in at the moment (created Dec 2017).

The two motivations behind this project were:

1. Learning how to interact with website APIs using Python
2. Making fun of "crypto enthusiasts" while learning a little on the side

## What I did

To make this python script, I used the tweepy package to post on Twitter and praw to read from */r/Bitcoin* on Reddit.

I used the set data structure to hold every message tweeted so far, so the script checks if the message has been tweeted before. If it had, then it iterates to the next controversial post.
