from __future__ import division
import sys
import json
import re
from collections import Counter

termCount = Counter()

def wordCount(tweet_file):
	global totalCount
	for tweet in tweet_file:
		jsonTweet = json.loads(tweet);
		if 'entities' in jsonTweet and jsonTweet['entities'] != None:
			if 'hashtags' in jsonTweet['entities']:
				if jsonTweet['entities']['hashtags'] != None:
					for hashTag in jsonTweet['entities']['hashtags']:
						hashTagText = hashTag['text']
						if hashTagText != '':
							termCount[hashTagText.lower()] += 1

def formattedValue(value):
		return "%.1f" %(value)

def termFrequency():
	for key, value in termCount.most_common(10):
		if key != '':
			print key.encode('utf-8') + ' ' + str(formattedValue(value))
	
def main():
	tweet_file = open(sys.argv[1])
	wordCount(tweet_file)
	termFrequency()

if __name__ == '__main__':
    main()
