import json
import pandas as pd
import matplotlib.pyplot as plt
import re

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text.decode('utf-8'))
    if match:
        return text
    return ""

tweets_data_path = 'sample_tweets.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")

for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

# for i in tweets_data:
# 	print(i['text'].encode("utf-8"))

# x = map(lambda tweet: tweet['lang'].encode("utf-8"), tweets_data)
# print(list(x))

tweets = pd.DataFrame()
tweets['text'] = pd.Series(list(map(lambda tweet: tweet['text'].encode("utf-8"), tweets_data))).values
tweets['lang'] = pd.Series(list(map(lambda tweet: tweet['lang'].encode("utf-8"), tweets_data))).values
tweets['country'] = pd.Series(list(map(lambda tweet: tweet['place']['country'].encode("utf-8") if tweet['place'] != None else None, tweets_data))).values

tweets['happy'] = tweets['text'].apply(lambda tweet: word_in_text('happy', tweet))
tweets['sad'] = tweets['text'].apply(lambda tweet: word_in_text('sad', tweet), tweets_data)
tweets['angry'] = tweets['text'].apply(lambda tweet: word_in_text('angry', tweet), tweets_data)
tweets['surprise'] = tweets['text'].apply(lambda tweet: word_in_text('surprise', tweet), tweets_data)
tweets['disgust'] = tweets['text'].apply(lambda tweet: word_in_text('disgust', tweet), tweets_data)
tweets['fear'] = tweets['text'].apply(lambda tweet: word_in_text('fear', tweet), tweets_data)