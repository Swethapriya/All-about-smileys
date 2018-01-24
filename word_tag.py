import json
import pandas as pd
import matplotlib.pyplot as plt
import re
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def clean(text):
	# text = ' '.join(list(filter(lambda x:x[0:4]!='http', text.split())))
	text = ' '.join(list(filter(lambda x:x[0:3]!='&gt', text.split())))
	return text

#HAPPY = open("happy_tweets.txt","r")
SAD = open("sad_tweets.txt","r")
ANGRY = open("angry_tweets.txt","r")
FEAR = open("fear_tweets.txt","r"	)
SURPRISE = open("surprise_tweets.txt","r")
DISGUST = open("disgust_tweets.txt","r")

HAPPY = ["happy belated birthday eddie from all at competence matters!",
"actually no, its acknowledging that a huge chunk of the mainstream media are activists, not journalists. happy to discuss",
"i have never been more happy to miss a flight then last monday: met my brother randomly https://t.co/qyqp8zy8",
"happy birthday() #110",
"i'm so happy for you; well done! ^^",
"slip your tongue between my thighs and write me a story with a happy ending.",
"happy 22nd birthday https://t.co/ffx5usvf5e",
"happy new year all! read our much anticipated edition 5 of the extra mile! https://t.co/uf8fzs8o9j",
"happy birthday pal. all the best.",
"happy birthday tanda mo na"]
for line in HAPPY:
    try:
        clean_tweet = clean(line)
        print(clean_tweet)
        tokens = nltk.word_tokenize(clean_tweet)
        print(tokens)
        tags = nltk.pos_tag(tokens)
        print(tags)
    except:
        continue
