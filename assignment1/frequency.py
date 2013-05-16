from __future__ import division
import sys
import json
import re
from collections import Counter

termCount = Counter()
totalCount = 0

def wordCount(tweet_file):
	global totalCount
	for tweet in tweet_file:
		jsonTweet = json.loads(tweet);
		if 'text' in jsonTweet:
			tweetText = jsonTweet['text'];
			for word in tweetText.lower().split():#re.split('\W+',tweetText.lower()):
				if word != '':
					termCount[word] += 1
					totalCount += 1

def formattedFrequency(value):
		return "%.8f" %(value/totalCount)

def termFrequency():
	for key, value in termCount.items():
		if key != '':
			print (key.encode('utf-8') + ' ' + str(formattedFrequency(value))) # ' '+str(key)+' '+str(totalCount)+
	

def main():
	tweet_file = open(sys.argv[1])
	wordCount(tweet_file)
	termFrequency()

if __name__ == '__main__':
    main()
