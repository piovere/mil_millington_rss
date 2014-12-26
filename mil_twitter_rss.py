"""The main module

supported by a file in the same directory called "auth_keys.py" with twitter api keys
"""

import auth_keys
import twitter

auth = twitter.OAuth(token=auth_keys.access_token, 
	                 token_secret=auth_keys.token_secret,
	                 consumer_secret=auth_keys.consumer_secret,
	                 consumer_key=auth_keys.consumer_key)

t = twitter.Twitter(auth=auth)

my_tweets = t.statuses.user_timeline(screen_name="MilMillington")

for key in my_tweets[0].keys():
	print key

print "\n"
print my_tweets[0]['text']
