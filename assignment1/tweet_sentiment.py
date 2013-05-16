import sys
import json

scores = {}

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
		if 'text' in jsonTweet:
			tweetText = jsonTweet['text'];
			print str(getSentiment(tweetText))
		else:
			print '0'			

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	readScores(sent_file)
	calTweetSentiment(tweet_file)

if __name__ == '__main__':
    main()
