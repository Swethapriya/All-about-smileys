import json
import pandas as pd
import matplotlib.pyplot as plt
import re

def clean(text):
	text = ' '.join(list(filter(lambda x:x[0:4]!='http', text.split())))
	text = ' '.join(list(filter(lambda x:x[0:3]!='&gt', text.split())))
	return text

HAPPY = open("happy_tweets.txt","r")
SAD = open("sad_tweets.txt","r")
ANGRY = open("angry_tweets.txt","r")
FEAR = open("fear_tweets.txt","r")
SURPRISE = open("surprise_tweets.txt","r")
DISGUST = open("disgust_tweets.txt","r")

for line in HAPPY:
    try:
        clean_tweet = clean(line)
        print(clean_tweet)
    except:
        continue
