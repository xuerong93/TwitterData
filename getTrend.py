import tweepy
import csv
import json
from tweepy import OAuthHandler

consumer_key = "CxLgokbrmaYExYebaA0zzyq5I"
consumer_secret = "0jnAqy0hmSYRrsgIPUfejsSpUtu0O1S4NiYLoyea8pUEmdRNlp"
access_key = "3740077215-4Bl8iYfQ8jlCvejfNr4xtigUGPsP7LrhIKp4BTO"
access_secret = "dd5lm69onbokv9RQfulYpiLT1jWXeNvqNpTte7qIvaq4i"

#printing all the tweets to the standard output
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

#list = open('trend.csv','a')

#print the trends all over the world
trends1 = api.trends_place(1)
# # trends1 is a list with only one element in it, which is a 
# # dict which we'll put in data.
# data = trends1[0] 
# # grab the trends
# trends = data['trends']
# # grab the name from each trend
# names = [trend['name'] for trend in trends]
# # put all the names together with a ' ' separating them
# #trendsName = ' '.join(names)
# #print(trendsName)
# Name = set(names)
# print Name

hashtags = [trend['name'] for trend in trends1[0]['trends'] if trend['name'].startswith('#')]
for hashtag in hashtags:
		print(hashtag.encode("utf-8"))
		
		
#print the trends in UK:23424975 #23424977 for united states #china 23424781
results = api.trends_place(id = 23424977) 
print "USA Trends"
with open('trend.txt', 'w+') as f:
	for location in results:
		for trend in location["trends"]:
			f.write(str(trend["name"])+'\n')
			print " - %s" % trend["name"]