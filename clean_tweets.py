import json
import pandas as pd
import matplotlib.pyplot as plt
import re


def clean(text):
	if(text[0:3].decode("utf-8") == "rt "):
		text = text[3:]
	text = text.decode("utf-8").encode("ascii", errors="ignore").decode()
	text = ' '.join(list(filter(lambda x:x[0]!='@', text.split())))
	return text

def word_in_text(word, text):
	word = word.lower()
	text = text.lower()
	text = clean(text)
	match = re.search(word, text)
	if match:
		return text
	return ""

HAPPY = open("happy_tweets.txt","a")
SAD = open("sad_tweets.txt","a")
ANGRY = open("angry_tweets.txt","a")
FEAR = open("fear_tweets.txt","a")
SURPRISE = open("surprise_tweets.txt","a")
DISGUST = open("disgust_tweets.txt","a")

tweets_data_path = 'tweets.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")

for line in tweets_file:
    try:
        tweet = json.loads(line)
        clean_tweet = tweet['text'].encode("utf-8")
        h = word_in_text('happy',clean_tweet)
        sa = word_in_text('sad',clean_tweet)
        su = word_in_text('surprise',clean_tweet)
        a = word_in_text('angry',clean_tweet)
        d = word_in_text('disgust',clean_tweet)
        f = word_in_text('fear',clean_tweet)
        if(h != ""):
        	HAPPY.write(h)
        	HAPPY.write("\n")
        if(sa != ""):
        	SAD.write(sa)
        	SAD.write("\n")
        if(su != ""):
        	SURPRISE.write(su)
        	SURPRISE.write("\n")
        if(a != ""):
        	ANGRY.write(a)
        	ANGRY.write("\n")
        if(d != ""):
        	DISGUST.write(d)
        	DISGUST.write("\n")
        if(f != ""):
        	FEAR.write(f)
        	FEAR.write("\n")
    except:
        continue

# for i in tweets_data:
# 	print(i['text'].encode("utf-8"))

# x = map(lambda tweet: tweet['lang'].encode("utf-8"), tweets_data)
# print(list(x))

# tweets = pd.DataFrame()
# tweets['text'] = pd.Series(list(map(lambda tweet: tweet['text'].encode("utf-8"), tweets_data))).values
# tweets['lang'] = pd.Series(list(map(lambda tweet: tweet['lang'].encode("utf-8"), tweets_data))).values
# tweets['country'] = pd.Series(list(map(lambda tweet: tweet['place']['country'].encode("utf-8") if tweet['place'] != None else None, tweets_data))).values

# tweets['happy'] = tweets['text'].apply(lambda tweet: word_in_text('happy', tweet))
# tweets['sad'] = tweets['text'].apply(lambda tweet: word_in_text('sad', tweet))
# tweets['angry'] = tweets['text'].apply(lambda tweet: word_in_text('angry', tweet))
# tweets['surprise'] = tweets['text'].apply(lambda tweet: word_in_text('surprise', tweet))
# tweets['disgust'] = tweets['text'].apply(lambda tweet: word_in_text('disgust', tweet))
# tweets['fear'] = tweets['text'].apply(lambda tweet: word_in_text('fear', tweet))

# for i in tweets['happy']:
# 	HAPPY.write(i)

# for i in tweets['sad']:
# 	SAD.write(i)

# for i in tweets['fear']:
# 	FEAR.write(i)

# for i in tweets['surprise']:
# 	SURPRISE.write(i)

# for i in tweets['disgust']:
# 	DISGUST.write(i)

# for i in tweets['angry']:
# 	ANGRY.write(i)

HAPPY.close()
SURPRISE.close()
SAD.close()
FEAR.close()
ANGRY.close()
DISGUST.close()