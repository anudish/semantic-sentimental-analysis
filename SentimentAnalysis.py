import csv

positiveDictionary = {}
negativeDictionary = {}

tweetList = []
with open('twitterData.txt') as tweetsfile:
    tweets = [x.strip() for x in tweetsfile.readlines()]
    for sentence in tweets:
        sentence = sentence.replace('\n', '')
        sentence = sentence.replace('\r', '')
        sentence = sentence.replace('Tweet:', '')
        tweetList.append(sentence)

positiveWordlist = []
with open('positiveWords.txt') as postiveFile:
    positiveWordlist = [positive.strip() for positive in postiveFile.readlines() ]

negativeWordlist = []
with open('negativeWords.txt',encoding="ISO-8859-1") as negativeFile:
    negativeWordlist = [negative.strip() for negative in negativeFile.readlines()]

wordsDictionary = []
with open('SentimentAnalysis.csv','w') as sentimentAnalysis:
    sentiment = csv.writer(sentimentAnalysis,lineterminator = '\n')
    sentiment.writerow(['Tweet', 'Message', 'Match', 'Polarity'])
    for i in range(len(tweetList)):
        wordBag = {}
        tweetWords = tweetList[i].split(" ")
        for word in range(len(tweetWords)):
            key = tweetWords[word]
            key = key.lower()
            if key in wordBag.keys():
                wordBag[key] = wordBag[key]+1
            else:
                wordBag[key] = 1
        wordsDictionary.append(wordBag)
        positiveWordCount = 0
        negativeWordCount = 0
        neutralCount = 0
        polarity = "neutral"
        matchList = ""
        positiveMatchlist = ""
        negativeMatchlist = ""

        for keyList in wordBag.keys():
        	if  keyList in positiveWordlist:
        		positiveWordCount = positiveWordCount + 1
        		if keyList in positiveDictionary.keys():
        			positiveDictionary[keyList] = positiveDictionary[keyList] + 1
        		else:
        			positiveDictionary[keyList] = 1
        		positiveMatchlist = positiveMatchlist + keyList + ","
        	elif keyList in negativeWordlist:
        		negativeWordCount = negativeWordCount + 1
        		if keyList in negativeDictionary.keys():
        			negativeDictionary[keyList] = negativeDictionary[keyList] + 1
        		else:
        			negativeDictionary[keyList] = 1
        		negativeMatchlist = negativeMatchlist + keyList + ","
        	else:
        		neutralCount = neutralCount + 1
        if(positiveWordCount>negativeWordCount):
        	polarity = 'positive'
        	matchList = positiveMatchlist
        elif(negativeWordCount>positiveWordCount):
        	polarity = 'negative'
        	matchList = negativeMatchlist
        else:
        	matchList = "NONE,"
        sentiment.writerow([i,tweetList[i],matchList[:-1],polarity])

with open('positiveTweets.csv','w+') as file:
	positiveFile = csv.writer(file,lineterminator='\n')
	positiveFile.writerow(['words','Count'])
	for keyList in positiveDictionary.keys():
		positiveFile.writerow([keyList, positiveDictionary[keyList]])
	
with open('negativeTweets.csv','w+') as file:
	negativeFile = csv.writer(file, lineterminator='\n')
	negativeFile.writerow(['words','Count'])
	for keyList in negativeDictionary.keys():
		negativeFile.writerow([keyList, negativeDictionary[keyList]])
