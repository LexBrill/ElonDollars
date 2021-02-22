import csv
import re

def lines_that_equal(line_to_match, fp):
    return [line for line in fp if line.rstrip("\n") == line_to_match]

net_sentiment = 0

regex = re.compile('[,\.!?]')
tweet = "i love etsy"
tweet = regex.sub('', tweet).lower()
print(tweet)


stock_words = []

tweet_list = tweet.split()
print(tweet_list)
    
positive_words = open("positive-words.txt", "r")
negative_words = open("negative-words.txt", "r")


for word in tweet_list:
    is_stock_word = False
    if len(word) >= 3:
        # print(word)
        f = open('nasdaq_screener_1613975622995.csv', 'rt')
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            if word in row[0].lower() or word in row[1].lower():
                # print(word)
                is_stock_word = True
                stock_words.append(row[0])
                print(word + " " + row[0] + " " + row[1])
    if not is_stock_word:
        positive_list = lines_that_equal(word, positive_words)
        negative_list = lines_that_equal(word, negative_words)
        if len(positive_list) != 0:
            net_sentiment += 1
        if len(negative_list) != 0:
            net_sentiment -= 1

if net_sentiment == 0:
    print("Neutral sentiment")
elif net_sentiment > 0:
    print("Positive sentiment")
else:
    print("Negative sentiment")

if len(stock_words) == 0:
    print("No stocks involved")
else:
    # print(stock_words[0])
    for stock in stock_words:
        print(stock)