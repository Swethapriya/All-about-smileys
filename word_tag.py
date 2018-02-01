import json
import pandas as pd
import matplotlib.pyplot as plt
import re
import nltk
import operator


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

HAPPY.seek(0)
hap_num = 0
hap_pred = {"happy": 0,"sad": 0, "fear":0,"angry":0,"disgust":0,"surprise":0}
for line in HAPPY:
	if(line.count("#happy")==0):
		continue
	try:
		clean_tweet = clean(line)
		#print(clean_tweet)
		tokens = nltk.word_tokenize(clean_tweet)
		tags = nltk.pos_tag(tokens)
		happy_q = 1
		sad_q = 1
		fear_q = 1
		anger_q = 1
		disgust_q = 1
		surprise_q = 1
		for i in tags:
			if(re.match('^[\w]+$', i[0]) is not None and ("_" not in i[0])):
				if(i[1] not in ('IN', 'RB', 'PRP$', 'PRP', 'CC', 'DT', 'PDT', 'TO', 'CD')):
					key = i[0]
					if(key in happy_words.keys()):
						happy_q += happy_words[key]
					if(key in sad_words.keys()):
						sad_q += sad_words[key]
					if(key in fear_words.keys()):
						fear_q += fear_words[key]
					if(key in angry_words.keys()):
						anger_q += angry_words[key]
					if(key in disgust_words.keys()):
						disgust_q += disgust_words[key]
					if(key in surprise_words.keys()):
						surprise_q += surprise_words[key]
		emotion_q = {"happy":happy_q,"sad":sad_q,"fear":fear_q,"angry":anger_q,"disgust": disgust_q,"surprise": surprise_q}
		hap_pred[max(emotion_q, key=emotion_q.get)] += 1
		hap_num += 1
	except:
		continue
print("\nhappy:",)
print("Number of happy tweets used for training:", hap_num)
print("prediction:")
print(hap_pred,"\n")

SAD.seek(0)
sad_num = 0
sad_pred = {"happy": 0,"sad": 0, "fear":0,"angry":0,"disgust":0,"surprise":0}
for line in SAD:
	if(line.count("#sad")==0):
		continue
	try:
		clean_tweet = clean(line)
		#print(clean_tweet)
		tokens = nltk.word_tokenize(clean_tweet)
		tags = nltk.pos_tag(tokens)
		happy_q = 1
		sad_q = 1
		fear_q = 1
		anger_q = 1
		disgust_q = 1
		surprise_q = 1
		for i in tags:
			if(re.match('^[\w]+$', i[0]) is not None and ("_" not in i[0])):
				if(i[1] not in ('IN', 'RB', 'PRP$', 'PRP', 'CC', 'DT', 'PDT', 'TO', 'CD')):
					key = i[0]
					if(key in happy_words.keys()):
						happy_q += happy_words[key]
					if(key in sad_words.keys()):
						sad_q += sad_words[key]
					if(key in fear_words.keys()):
						fear_q += fear_words[key]
					if(key in angry_words.keys()):
						anger_q += angry_words[key]
					if(key in disgust_words.keys()):
						disgust_q += disgust_words[key]
					if(key in surprise_words.keys()):
						surprise_q += surprise_words[key]
		emotion_q = {"happy":happy_q,"sad":sad_q,"fear":fear_q,"angry":anger_q,"disgust": disgust_q,"surprise": surprise_q}
		sad_pred[max(emotion_q, key=emotion_q.get)] += 1
		sad_num += 1
	except:
		continue
print("\nsad:",)
print("Number of sad tweets used for training:", sad_num)
print("prediction:")
print(sad_pred,"\n")

FEAR.seek(0)
fea_num = 0
fea_pred = {"happy": 0,"sad": 0, "fear":0,"angry":0,"disgust":0,"surprise":0}
for line in FEAR:
	if(line.count("#fear")==0):
		continue
	try:
		clean_tweet = clean(line)
		#print(clean_tweet)
		tokens = nltk.word_tokenize(clean_tweet)
		tags = nltk.pos_tag(tokens)
		happy_q = 1
		sad_q = 1
		fear_q = 1
		anger_q = 1
		disgust_q = 1
		surprise_q = 1
		for i in tags:
			if(re.match('^[\w]+$', i[0]) is not None and ("_" not in i[0])):
				if(i[1] not in ('IN', 'RB', 'PRP$', 'PRP', 'CC', 'DT', 'PDT', 'TO', 'CD')):
					key = i[0]
					if(key in happy_words.keys()):
						happy_q += happy_words[key]
					if(key in sad_words.keys()):
						sad_q += sad_words[key]
					if(key in fear_words.keys()):
						fear_q += fear_words[key]
					if(key in angry_words.keys()):
						anger_q += angry_words[key]
					if(key in disgust_words.keys()):
						disgust_q += disgust_words[key]
					if(key in surprise_words.keys()):
						surprise_q += surprise_words[key]
		emotion_q = {"happy":happy_q,"sad":sad_q,"fear":fear_q,"angry":anger_q,"disgust": disgust_q,"surprise": surprise_q}
		fea_pred[max(emotion_q, key=emotion_q.get)] += 1
		fea_num += 1
	except:
		continue
print("\nfear:",)
print("Number of fear tweets used for training:", fea_num)
print("prediction:")
print(fea_pred,"\n")

ANGRY.seek(0)
ang_num = 0
ang_pred = {"happy": 0,"sad": 0, "fear":0,"angry":0,"disgust":0,"surprise":0}
for line in ANGRY:
	if(line.count("#angry")==0):
		continue
	try:
		clean_tweet = clean(line)
		#print(clean_tweet)
		tokens = nltk.word_tokenize(clean_tweet)
		tags = nltk.pos_tag(tokens)
		happy_q = 1
		sad_q = 1
		fear_q = 1
		anger_q = 1
		disgust_q = 1
		surprise_q = 1
		for i in tags:
			if(re.match('^[\w]+$', i[0]) is not None and ("_" not in i[0])):
				if(i[1] not in ('IN', 'RB', 'PRP$', 'PRP', 'CC', 'DT', 'PDT', 'TO', 'CD')):
					key = i[0]
					if(key in happy_words.keys()):
						happy_q += happy_words[key]
					if(key in sad_words.keys()):
						sad_q += sad_words[key]
					if(key in fear_words.keys()):
						fear_q += fear_words[key]
					if(key in angry_words.keys()):
						anger_q += angry_words[key]
					if(key in disgust_words.keys()):
						disgust_q += disgust_words[key]
					if(key in surprise_words.keys()):
						surprise_q += surprise_words[key]
		emotion_q = {"happy":happy_q,"sad":sad_q,"fear":fear_q,"angry":anger_q,"disgust": disgust_q,"surprise": surprise_q}
		ang_pred[max(emotion_q, key=emotion_q.get)] += 1
		ang_num += 1
	except:
		continue
print("\nangry:",)
print("Number of angry tweets used for training:", ang_num)
print("prediction:")
print(ang_pred,"\n")

DISGUST.seek(0)
dis_num = 0
dis_pred = {"happy": 0,"sad": 0, "fear":0,"angry":0,"disgust":0,"surprise":0}
for line in DISGUST:
	if(line.count("#disgust")==0):
		continue
	try:
		clean_tweet = clean(line)
		#print(clean_tweet)
		tokens = nltk.word_tokenize(clean_tweet)
		tags = nltk.pos_tag(tokens)
		happy_q = 1
		sad_q = 1
		fear_q = 1
		anger_q = 1
		disgust_q = 1
		surprise_q = 1
		for i in tags:
			if(re.match('^[\w]+$', i[0]) is not None and ("_" not in i[0])):
				if(i[1] not in ('IN', 'RB', 'PRP$', 'PRP', 'CC', 'DT', 'PDT', 'TO', 'CD')):
					key = i[0]
					if(key in happy_words.keys()):
						happy_q += happy_words[key]
					if(key in sad_words.keys()):
						sad_q += sad_words[key]
					if(key in fear_words.keys()):
						fear_q += fear_words[key]
					if(key in angry_words.keys()):
						anger_q += angry_words[key]
					if(key in disgust_words.keys()):
						disgust_q += disgust_words[key]
					if(key in surprise_words.keys()):
						surprise_q += surprise_words[key]
		emotion_q = {"happy":happy_q,"sad":sad_q,"fear":fear_q,"angry":anger_q,"disgust": disgust_q,"surprise": surprise_q}
		dis_pred[max(emotion_q, key=emotion_q.get)] += 1
		dis_num += 1
	except:
		continue
print("\ndisgust:",)
print("Number of dusgust tweets used for training:", dis_num)
print("prediction:")
print(dis_pred,"\n")

SURPRISE.seek(0)
sur_num = 0
sur_pred = {"happy": 0,"sad": 0, "fear":0,"angry":0,"disgust":0,"surprise":0}
for line in SURPRISE:
	if(line.count("#surprise")==0):
		continue
	try:
		clean_tweet = clean(line)
		#print(clean_tweet)
		tokens = nltk.word_tokenize(clean_tweet)
		tags = nltk.pos_tag(tokens)
		happy_q = 1
		sad_q = 1
		fear_q = 1
		anger_q = 1
		disgust_q = 1
		surprise_q = 1
		for i in tags:
			if(re.match('^[\w]+$', i[0]) is not None and ("_" not in i[0])):
				if(i[1] not in ('IN', 'RB', 'PRP$', 'PRP', 'CC', 'DT', 'PDT', 'TO', 'CD')):
					key = i[0]
					if(key in happy_words.keys()):
						happy_q += happy_words[key]
					if(key in sad_words.keys()):
						sad_q += sad_words[key]
					if(key in fear_words.keys()):
						fear_q += fear_words[key]
					if(key in angry_words.keys()):
						anger_q += angry_words[key]
					if(key in disgust_words.keys()):
						disgust_q += disgust_words[key]
					if(key in surprise_words.keys()):
						surprise_q += surprise_words[key]
		emotion_q = {"happy":happy_q,"sad":sad_q,"fear":fear_q,"angry":anger_q,"disgust": disgust_q,"surprise": surprise_q}
		sur_pred[max(emotion_q, key=emotion_q.get)] += 1
		sur_num += 1
	except:
		continue
print("\nsurprise:",)
print("Number of surprise tweets used for training:", sur_num)
print("prediction:")
print(sur_pred,"\n")

# print("/n/n HAPPY")
# for x in happy_words:
# 	if(happy_words[x] > 9):
# 		print(x,':',happy_words[x])


# print("/n/n SAD")
# for x in happy_words:
# 	if(happy_words[x] > 9):
# 		print(x,':',happy_words[x])


# print("/n/n FEAR")
# for x in happy_words:
# 	if(happy_words[x] > 9):
# 		print(x,':',happy_words[x])

# print("/n/n SURPRISE")
# for x in happy_words:
# 	if(happy_words[x] > 9):
# 		print(x,':',happy_words[x])

# print("/n/n ANGRY")
# for x in happy_words:
# 	if(happy_words[x] > 9):
# 		print(x,':',happy_words[x])

# print("/n/n DISGUST")
# for x in happy_words:
# 	if(happy_words[x] > 9):
# 		print(x,':',happy_words[x])
