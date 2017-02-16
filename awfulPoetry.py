# file awfulpoetry2.py
# now allows user to print up to 10 random sentences
# Alexander Mas

import random

# create each list of words
articles = ["the", "a", "another"]
subjects = ["cat", "dog", "man", "woman"]
verbs = ["sang", "ran", "jumped", "hoped", "laughed"]
adverbs = ["loudly", "quietly", "well", "badly"]

# function to get input from user
def get_int(msg, default):
    while True:
        try:
            line = input(msg)
            if not line and default is not None:
                return default
            i = int(line)
            if not 1 <= i <= 10:
                print("must be between ", 1, " and ", 10, "\n")
            else: return i
        except ValueError as err:
            print(err)

# get number of sentences from user; defaults to 5
numSentences = get_int("number of sentences: ", 5)

# create sentences
i = 0
while i < numSentences:
    # randomly select a word from each list
    article = random.choice(articles)
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    adverb = random.choice(adverbs)

    # randomly select a sentence structure to create and print
    sentenceToPrint = ""
    sentenceSelector = random.randint(0, 1)
    if sentenceSelector == 0:
        sentence = [article, subject, verb, adverb]
        for j in sentence:
            sentenceToPrint += j + " "
    else:
        sentence = [article, subject, verb]
        for k in sentence:
            sentenceToPrint += k + " "
    print(sentenceToPrint)

    i += 1
