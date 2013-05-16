import sys
import json
from collections import Counter

scores = {}
happyScore = Counter()
stateList = []

def getHappiestState():
	return happyScore.most_common(1)[0]

def getSentiment(tweetText):
	sentiment = 0
	for word in tweetText.split():
		if word.lower() in scores:
			sentiment += scores[word.lower()]
	return sentiment

def readScores(sent_file):
	for line in sent_file:
		term, score  = line.split("\t") 
		scores[term] = int(score)  

def calTweetSentiment(tweet_file):
	for tweet in tweet_file:
		jsonTweet = json.loads(tweet);
		if 'place' in jsonTweet and jsonTweet['place'] != None:
			if 'country_code' in jsonTweet['place']:
				if jsonTweet['place']['country_code'].lower() == 'us':
					if 'full_name' in jsonTweet['place']:
						if 'text' in jsonTweet:
							tweetText = jsonTweet['text'];
							happyScore[jsonTweet['place']['full_name'].lower()] += getSentiment(tweetText.lower())

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	readScores(sent_file)
	calTweetSentiment(tweet_file)
	print getHappiestState()[0][-2:]

if __name__ == '__main__':
    main()
