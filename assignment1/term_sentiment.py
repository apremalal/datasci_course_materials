import sys
import json

scores = {}
new_scores = {}

def getSentiment(tweetText):
	sentiment = 0
	for word in tweetText.split():
		if word in scores:
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
			tweetText = jsonTweet['text'].lower();
			tweet_sentiment = getSentiment(tweetText)
			for word in tweetText.split():
				if word in scores:
					continue
				else:
					if word in new_scores:
						new_scores[word] += int(tweet_sentiment)
					else:
						new_scores[word] = int(tweet_sentiment)
def formattedValue(value):
		return "%.3f" %(value)

def printResults():
	for key,value in new_scores.iteritems():
		print key.encode('utf-8') + ' ' + str(formattedValue(value))

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	readScores(sent_file)
	calTweetSentiment(tweet_file)
	printResults()

if __name__ == '__main__':
    main()
