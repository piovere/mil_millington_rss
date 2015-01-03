"""The main module

supported by a file in the same directory called "config.py" with twitter api keys
"""

import config
import twitter
import PyRSS2Gen as RSS
import datetime

auth = twitter.OAuth(token=config.access_token, 
	                 token_secret=config.token_secret,
	                 consumer_secret=config.consumer_secret,
	                 consumer_key=config.consumer_key)

t = twitter.Twitter(auth=auth)

my_tweets = t.statuses.user_timeline(screen_name="MilMillington")

for key in my_tweets[0].keys():
	print key

# Code to detect links and add HTML markup
# Pulled from http://stackoverflow.com/questions/1071191/detect-urls-in-a-string-and-wrap-with-a-href-tag
# def url_sub(tweet):
# 	URL_REGEX = re.compile(r'''((?:mailto:|ftp://|http://|https://)[^ <>'"{}|\\^`[\]]*)''')
# 	return URL_REGEX.sub(r'<a href="\1">\1</a>')

print "\n"
print url_sub(my_tweets[0]['text'])

rssitems = []

for tweet in my_tweets:
    rssitems.append(
               RSS.RSSItem(
                           title=tweet['text']
                           link=tweet[tweet['entities']['urls'][0]['expanded_url']]
                           description=tweet['text']
                           guid=RSS.Guid(tweet['entities']['urls'][0]['expanded_url'])
                           pubDate=tweet['created_at'] # need to convert this into datetime
                           )
               )

rss = RSS.RSS2(
               title="Mil's Mail announcements",
               link="https://twitter.com/MilMillington",
               description="An announcement feed to try and keep track of when "
                           "Mil Millington writes what used to be emails",
               lastBuildDate=datetime.datetime.utcnow(),

               items=rssitems
              )

rss.write_xml(open("milsmail.rss", "w"))
