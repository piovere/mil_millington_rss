"""The main module

supported by a file in the same directory called "config.py" with twitter api keys
"""

import config
import twitter
import PyRSS2Gen

auth = twitter.OAuth(token=config.access_token, 
	                 token_secret=config.token_secret,
	                 consumer_secret=config.consumer_secret,
	                 consumer_key=config.consumer_key)

t = twitter.Twitter(auth=auth)

my_tweets = t.statuses.user_timeline(screen_name="MilMillington")

for key in my_tweets[0].keys():
	print key

print "\n"
print my_tweets[0]['text']

# Adding a comment, just playing around
