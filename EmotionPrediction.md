Brainstorm:

The idea is to collect the adjectives, adverbs, verbs, Interjections in the given text. All of these parts of speech are tagged with one/more of the basic emotions prior. We add up the score of the each emotion and use this data to determine the dominant emotion/emotional distribution(emotional footprint) of the text/song.

Sub problems:
1) Procuring the dictionary of adjectives/adverbs/verbs/Interjections
2) Tagging each of them with the basic emotions.
3) Test on various data samples from songs, emails, tweets, novel passages etc.,
4) Furthur improvement 

Prob 1&2:

Using twitter and hashtags of the basic emotions happy,anger,fear,disgust,surprise,sadness and their variations(?) and pos tagging for the procurement of the dictionary. And we use the hashtags used as the tags to the words.

Details and modifications:

Extracting words from tweets:

Since we have extracted the tweets with standalone emotion words happy,sad,.. and not just those in which these occur with hashtags(like #happy, #sad..), we might have to use different approaches for these two kind of tweets.

Common Approach:
Common nouns like "birthday", "new year", "death", "scam" also provide a lot of information about the emotions and are not to be discarded. It's proper nouns that are to be discarded. And this filtering of common nouns from proper nouns can be done using TF-IDF parameter.
remove &gt
Other Hashtags with actual words are important
We are including retweets which means, the same tweet might be considered a large number of times. This is fine in a way that a tweet with more retweets is grammatically correct. However, the downside is that the presence of the word happy doesn't necessarily mean a happy tweet and the retweets add more weight to such a false happy tweet. Also, the retweets extracted are not exhaustive, making the calculation unreliable.
Tagging is done for unigrams, bigrams and trigrams
Grams in hastagged(by emotions) tweets get double the weight as compared to the ones that aren't 

With Hashtag:


Without Hashtag:

