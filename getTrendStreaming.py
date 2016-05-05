#just change f = open('store.txt','a')in line 16 and stream.filter(track=["#CamsPumaFace"]) in line 36 with the topic name and run the python file
import tweepy
import json
from tweepy import OAuthHandler
import csv

# consumer_key = "fjE4LONflAggpE7QCuQ8zmYzN"
# consumer_secret = "QmOS2ldKRn3TyIs1pQGjavpEmea5D8xh0pxqv12XwflYw4l94D"
# access_key = "3968827636-QX1tbtHcIppfuuFHdupkDoUrYIr2hve6MKVOz8D"
# access_secret = "7P1SVcVNYYg3XSSXcEnW1VC6Y3l2MM5ncof3UvvulisUc"
#SherryHuli Sreaming 1
consumer_key = "n5c3FzoWXPvaXEEyx3FbEQ58g"
consumer_secret = "0HDsUb2xkYCIbJmTXvY4iWQoHoFOi37Oola0BiKMJldP1mzl9F"
access_key = "784262882-cZUG21NSRBl1mbGnFMNICcfhzqIUcD1T8mBD0Gx1"
access_secret = "3VVSe5FTdlzOZm2T0AmtTId077MN7jriFmQb3r1CH6Gyr"

#printing all the tweets to the standard output
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
 
trend_hashtag = "AskKourtney"

class StdOutListener(tweepy.streaming.StreamListener):
    #''' Handles data received from the stream. '''
    def on_status(self, status):
        #print status.__dict__
        #print status.created_at
        with open('%s_trend.csv' % trend_hashtag,'a') as trend:
            writer = csv.writer(trend)
            writer.writerow([str(status.created_at),"lang: "+str(status.lang)])
            #writer.writerow([str(status)])
        pass
        return True
        
    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening
 
    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening
    
if __name__ == '__main__': 
    listener = StdOutListener()
    stream = tweepy.streaming.Stream(auth, listener)
    stream.filter(track= ["#"+trend_hashtag])
    #f.close()
#locations=[-122.75,36.8,-121.75,37.8],
