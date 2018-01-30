import json
import pandas as pd
import matplotlib.pyplot as plt
import re
import nltk


nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

happy_words = {}
sad_words = {}
angry_words = {}
fear_words = {}
surprise_words = {}
disgust_words = {}

def clean(text):
	words = text.split()
	for i in range(0,len(words)):
		if(words[i][0:4] == "http"):
			words[i] = "url"
	text = ' '.join(words)
	text = ' '.join(list(filter(lambda x:x[0:3]!='&gt', text.split())))
	text = ' '.join(list(filter(lambda x:x[0:3]!='^^', text.split())))
	return text

HAPPY = open("happy_tweets.txt","r")
SAD = open("sad_tweets.txt","r")
ANGRY = open("angry_tweets.txt","r")
FEAR = open("fear_tweets.txt","r"	)
SURPRISE = open("surprise_tweets.txt","r")
DISGUST = open("disgust_tweets.txt","r")

for line in HAPPY:
	if(line.count("#happy")==0):
		continue
	try:
		clean_tweet = clean(line)
		#print(clean_tweet)
		tokens = nltk.word_tokenize(clean_tweet)
		tags = nltk.pos_tag(tokens)

		for i in tags:
			if(re.match('^[\w]+$', i[0]) is not None and ("_" not in i[0])):
				if(i[1] not in ('IN', 'RB', 'PRP$', 'PRP', 'CC', 'DT', 'PDT', 'TO', 'CD')):
					happy_key = i[0]
					if(happy_key in happy_words.keys()):
						happy_words[happy_key] += 1
					else:
						happy_words[happy_key] = 1
	except:
		continue

for line in SAD:
	if(line.count("#sad")==0):
		continue
	try:
		clean_tweet = clean(line)
		#print(clean_tweet)
		tokens = nltk.word_tokenize(clean_tweet)
		tags = nltk.pos_tag(tokens)

		for i in tags:
			if(re.match('^[\w]+$', i[0]) is not None and ("_" not in i[0])):
				if(i[1] not in ('IN', 'RB', 'PRP$', 'PRP', 'CC', 'DT', 'PDT', 'TO', 'CD')):
					sad_key = i[0]
					if(sad_key in sad_words.keys()):
						sad_words[sad_key] += 1
					else:
						sad_words[sad_key] = 1
	except:
		continue

for line in ANGRY:
	if(line.count("#angry")==0):
		continue
	try:
		clean_tweet = clean(line)
		#print(clean_tweet)
		tokens = nltk.word_tokenize(clean_tweet)
		tags = nltk.pos_tag(tokens)

		for i in tags:
			if(re.match('^[\w]+$', i[0]) is not None and ("_" not in i[0])):
				if(i[1] not in ('IN', 'RB', 'PRP$', 'PRP', 'CC', 'DT', 'PDT', 'TO', 'CD')):
					angry_key = i[0]
					if(angry_key in angry_words.keys()):
						angry_words[angry_key] += 1
					else:
						angry_words[angry_key] = 1
	except:
		continue

for line in FEAR:
	if(line.count("#fear")==0):
		continue
	try:
		clean_tweet = clean(line)
		#print(clean_tweet)
		tokens = nltk.word_tokenize(clean_tweet)
		tags = nltk.pos_tag(tokens)

		for i in tags:
			if(re.match('^[\w]+$', i[0]) is not None and ("_" not in i[0])):
				if(i[1] not in ('IN', 'RB', 'PRP$', 'PRP', 'CC', 'DT', 'PDT', 'TO', 'CD')):
					fear_key = i[0]
					if(fear_key in fear_words.keys()):
						fear_words[fear_key] += 1
					else:
						fear_words[fear_key] = 1
	except:
		continue

for line in SURPRISE:
	if(line.count("#surprise")==0):
		continue
	try:
		clean_tweet = clean(line)
		#print(clean_tweet)
		tokens = nltk.word_tokenize(clean_tweet)
		tags = nltk.pos_tag(tokens)

		for i in tags:
			if(re.match('^[\w]+$', i[0]) is not None and ("_" not in i[0])):
				if(i[1] not in ('IN', 'RB', 'PRP$', 'PRP', 'CC', 'DT', 'PDT', 'TO', 'CD')):
					surprise_key = i[0]
					if(surprise_key in surprise_words.keys()):
						surprise_words[surprise_key] += 1
					else:
						surprise_words[surprise_key] = 1
	except:
		continue

for line in DISGUST:
	if(line.count("#disgust")==0):
		continue
	try:
		clean_tweet = clean(line)
		#print(clean_tweet)
		tokens = nltk.word_tokenize(clean_tweet)
		tags = nltk.pos_tag(tokens)

		for i in tags:
			if(re.match('^[\w]+$', i[0]) is not None and ("_" not in i[0])):
				if(i[1] not in ('IN', 'RB', 'PRP$', 'PRP', 'CC', 'DT', 'PDT', 'TO', 'CD')):
					disgust_key = i[0]
					if(disgust_key in disgust_words.keys()):
						disgust_words[disgust_key] += 1
					else:
						disgust_words[disgust_key] = 1
	except:
		continue

print("/n/n HAPPY")
for x in happy_words:
	if(happy_words[x] > 9):
		print(x,':',happy_words[x])


print("/n/n SAD")
for x in happy_words:
	if(happy_words[x] > 9):
		print(x,':',happy_words[x])


print("/n/n FEAR")
for x in happy_words:
	if(happy_words[x] > 9):
		print(x,':',happy_words[x])

print("/n/n SURPRISE")
for x in happy_words:
	if(happy_words[x] > 9):
		print(x,':',happy_words[x])

print("/n/n ANGRY")
for x in happy_words:
	if(happy_words[x] > 9):
		print(x,':',happy_words[x])

print("/n/n DISGUST")
for x in happy_words:
	if(happy_words[x] > 9):
		print(x,':',happy_words[x])
