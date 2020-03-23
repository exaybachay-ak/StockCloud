#!/usr/bin/python

### --------------------------------->>> Imports <<<---------------------------------   ###
import praw
import os
import pdb
import re
import random
import time
import datetime
import sys
import ftplib
# Imports for wordcloud
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

### --------------------------------->>> Gather data <<<---------------------------------   ###

### --> Setting bot and subreddit info
reddit = praw.Reddit(user_agent='your_UA_text',
                    client_id='your_client_id', client_secret='your_secret',
                    username='your_username', password='your_password')

### --> Stock patterns - e.g. SPY, $SPY, TSLA or $TSLA
pattern1 = re.compile(r'\$[a-zA-Z][a-zA-Z][a-zA-Z]\b')
pattern2 = re.compile(r'\$[a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z]\b')
pattern3 = re.compile(r'\$[a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z]\b')

pattern4 = re.compile(r'^[a-zA-Z][a-zA-Z][a-zA-Z]\b')
pattern5 = re.compile(r'^[a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z]\b')
pattern6 = re.compile(r'^[a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z]\b')

pattern7 = re.compile(r'\s[a-zA-Z][a-zA-Z][a-zA-Z]\b')
pattern8 = re.compile(r'\s[a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z]\b')
pattern9 = re.compile(r'\s[a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z]\b')

stocks = []

# Ask the user to enter their desired sort type and limit
sorttype = input("What type of sort do you want (hot, new, top, or rising):\n")

while True:
    try:
        sortlimit = int(input("What amount of data do you want back (enter a number, up to 100 posts):\n"))
        if sortlimit < 1 or sortlimit > 101:
            raise ValueError 
        break
    except:
        print("Invalid selection.  The number must be between 1 and 100.")

### --> Get submissions from WSB hot to parse for stock names
if sorttype == "Hot" or sorttype == "hot":
    for submission in reddit.subreddit('wallstreetbets').hot(limit=sortlimit):
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            match1 = re.match(pattern1, comment.body)
            match2 = re.match(pattern2, comment.body)
            match3 = re.match(pattern3, comment.body)
            match4 = re.match(pattern4, comment.body)
            match5 = re.match(pattern5, comment.body)
            match6 = re.match(pattern6, comment.body)
            match7 = re.match(pattern7, comment.body)
            match8 = re.match(pattern8, comment.body)
            match9 = re.match(pattern9, comment.body)
            if(match1):
                stocks.append(match1.group(0))
            elif(match2):
                stocks.append(match2.group(0))
            elif(match3):
                stocks.append(match3.group(0))
            elif(match4):
                stocks.append(match4.group(0))
            elif(match5):
                stocks.append(match5.group(0))
            elif(match6):
                stocks.append(match6.group(0))
            elif(match7):
                stocks.append(match7.group(0))
            elif(match8):
                stocks.append(match8.group(0))
            elif(match9):
                stocks.append(match9.group(0))
            else:
                pass

### --> Get submissions from WSB hot to parse for stock names
elif sorttype == "New" or sorttype == "new":
    for submission in reddit.subreddit('wallstreetbets').new(limit=sortlimit):
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            match1 = re.match(pattern1, comment.body)
            match2 = re.match(pattern2, comment.body)
            match3 = re.match(pattern3, comment.body)
            match4 = re.match(pattern4, comment.body)
            match5 = re.match(pattern5, comment.body)
            match6 = re.match(pattern6, comment.body)
            match7 = re.match(pattern7, comment.body)
            match8 = re.match(pattern8, comment.body)
            match9 = re.match(pattern9, comment.body)
            if(match1):
                stocks.append(match1.group(0))
            elif(match2):
                stocks.append(match2.group(0))
            elif(match3):
                stocks.append(match3.group(0))
            elif(match4):
                stocks.append(match4.group(0))
            elif(match5):
                stocks.append(match5.group(0))
            elif(match6):
                stocks.append(match6.group(0))
            elif(match7):
                stocks.append(match7.group(0))
            elif(match8):
                stocks.append(match8.group(0))
            elif(match9):
                stocks.append(match9.group(0))
            else:
                pass

### --> Get submissions from WSB hot to parse for stock names
if sorttype == "Top" or sorttype == "top":
    for submission in reddit.subreddit('wallstreetbets').top(limit=sortlimit):
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            match1 = re.match(pattern1, comment.body)
            match2 = re.match(pattern2, comment.body)
            match3 = re.match(pattern3, comment.body)
            match4 = re.match(pattern4, comment.body)
            match5 = re.match(pattern5, comment.body)
            match6 = re.match(pattern6, comment.body)
            match7 = re.match(pattern7, comment.body)
            match8 = re.match(pattern8, comment.body)
            match9 = re.match(pattern9, comment.body)
            if(match1):
                stocks.append(match1.group(0))
            elif(match2):
                stocks.append(match2.group(0))
            elif(match3):
                stocks.append(match3.group(0))
            elif(match4):
                stocks.append(match4.group(0))
            elif(match5):
                stocks.append(match5.group(0))
            elif(match6):
                stocks.append(match6.group(0))
            elif(match7):
                stocks.append(match7.group(0))
            elif(match8):
                stocks.append(match8.group(0))
            elif(match9):
                stocks.append(match9.group(0))
            else:
                pass


### --> Get submissions from WSB hot to parse for stock names
if sorttype == "Rising" or sorttype == "rising":
    for submission in reddit.subreddit('wallstreetbets').rising(limit=sortlimit):
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            match1 = re.match(pattern1, comment.body)
            match2 = re.match(pattern2, comment.body)
            match3 = re.match(pattern3, comment.body)
            match4 = re.match(pattern4, comment.body)
            match5 = re.match(pattern5, comment.body)
            match6 = re.match(pattern6, comment.body)
            match7 = re.match(pattern7, comment.body)
            match8 = re.match(pattern8, comment.body)
            match9 = re.match(pattern9, comment.body)
            if(match1):
                stocks.append(match1.group(0))
            elif(match2):
                stocks.append(match2.group(0))
            elif(match3):
                stocks.append(match3.group(0))
            elif(match4):
                stocks.append(match4.group(0))
            elif(match5):
                stocks.append(match5.group(0))
            elif(match6):
                stocks.append(match6.group(0))
            elif(match7):
                stocks.append(match7.group(0))
            elif(match8):
                stocks.append(match8.group(0))
            elif(match9):
                stocks.append(match9.group(0))
            else:
                pass

### --------------------------------->>> Download stocks <<<---------------------------------   ###

### --> Retrieve list of stocks from FTP
# https://gist.github.com/indraniel/02b16a2c3d0ff6518e0e025483791c59

# Set up parameters for FTP transaction
server = 'ftp.nasdaqtrader.com'
directory = 'SymbolDirectory'
file1 = 'nasdaqlisted.txt'
file2 = 'otherlisted.txt'

#Retrieve files
ftp = ftplib.FTP(server)
ftp.login()
ftp.cwd(directory)
ftp.retrbinary("RETR {}".format(file1), open(file1, 'wb').write)
ftp.retrbinary("RETR {}".format(file2), open(file2, 'wb').write)

# Combine the files into 1
file = open("alllisted.txt", "w+")
filenames = ['nasdaqlisted.txt', 'otherlisted.txt']

for fname in filenames:
    with open(fname) as infile:
        file.write(infile.read())

file.close()

### --> Strip out extra info so we only have stock symbols
with open('alllisted.txt', "r") as f:
    content = f.read()

new_content = re.sub(r'\|.*', ' ', content)

formattedstocks = open("allformatted.txt", "w+")
formattedstocks.write(new_content)
formattedstocks.close()

### --> Pull only legitimate stock symbols
realstocks = []

with open('allformatted.txt', 'r') as alf:
    line = alf.readline()
    cnt = 1
    while line:
        for s in stocks:
            match = re.search(s + '\s', line, re.IGNORECASE)
            if match:
                realstocks.append(s)
        line = alf.readline()
        cnt += 1

### --------------------------------->>> Calculate frequency <<<---------------------------------   ###

### ---> Tally up number of times a stock appears
stockcloud = {}

#Find words in array and add to dict, then increment for each occurrance
for r in realstocks:
    upper = '[A-Z][A-Z][A-Z]|[A-Z][A-Z][A-Z][A-Z]|[A-Z][A-Z][A-Z][A-Z][A-Z]'
    umatch = re.search(upper, r)
    if umatch:
        stockcloud[r] = stockcloud.get(r, 0) + 20
    else:
        stockcloud[r] = stockcloud.get(r, 0) + 1

#Sort the dict by most occurrances first
#Commenting this out - shouldn't need to sort if it's in a word cloud
sortedstockcloud = sorted(stockcloud.items(), key=lambda x: (x[1],x[0]), reverse=True)

### --------------------------------->>> Generate command-line visualization <<<---------------------------------   ###
index = ['Frequency']
index2 = [1]
df = pd.DataFrame(stockcloud, index=index)
df2 = pd.DataFrame(sortedstockcloud, columns=['Word','frequency'])

#Display the data
print(df)
print(df2)

### --------------------------------->>> Generate image visualization <<<---------------------------------   ###

stocknums = [lis[1] for lis in sortedstockcloud]
stocknames = [lis[0] for lis in sortedstockcloud]
stockscloud = []

#expand stocks into a cloud list
for idx, num in enumerate(stocknums):
   for i in range(0,int(num)):
      stockscloud.append(stocknames[idx])

listToStr = ' '.join([str(elem) for elem in stockscloud]) 

# read stock list and define wordcloud
df = pd.DataFrame(stocks)
stopwords = set(STOPWORDS)
wordcloud = WordCloud(collocations=False, width = 1200, height = 1200, background_color ='white', stopwords = stopwords, min_font_size = 10).generate(listToStr)

# plot the WordCloud image                        
fig = plt.figure(figsize = (8, 8), facecolor = None)
fig.canvas.set_window_title("Looking at WallStreetBets " + sorttype + " sort, with " + str(sortlimit) + " post\(s\)")
plt.imshow(wordcloud)
plt.axis("off") 
plt.tight_layout(pad = 0)

plt.show()
