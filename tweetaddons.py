#this class will function as a way of extending the tweet with add ons that increase
#the comedic value of the reddit comment ex. censoring profane comments, adding hashtags
class TweetAddOns:
    @staticmethod
    def censorTweet(tweet):
        swearWords = ["fuck","shit","damn","retard","bitch","fag","pussy","cunt","rape","tard","penis","titty"]
        for swear in swearWords:
            if swear in tweet.lower():
                tweet = tweet.replace(swear[1:],(len(swear)-1)*'*')
        return tweet

    @staticmethod
    def addHashtags(tweet):

        hashtagDictionary = {" bitcoin ":" #bitcoin",
                             " btc ":" #bitcoin",
                             " ethereum ":" #ethereum",
                             " etc ":" #ethereum",
                             " crypto":" #cryptocurrency",
                             "cryptocurrency":" #cryptocurrency",
                             "invest":" #investments",
                             " cash":" #money",
                             "bitcoin cash":" #BCHbetterthanBTC",
                             "bch": " #BitcoinCash",
                             "hodl": " #HODL",
                             "lambo": " #LamboSoon"}
        #adding relevant hashtags to the tweet
        for keyword in hashtagDictionary:
            if (keyword in tweet.lower()) and (len(hashtagDictionary[keyword]) + len(tweet) <= 280) and (hashtagDictionary[keyword] not in tweet):
                tweet += hashtagDictionary[keyword]
        return tweet
