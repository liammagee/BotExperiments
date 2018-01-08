import tweepy
from time import sleep
import numpy as np
import random


# Import our Twitter credentials from credentials.py
from credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

my_file=open('shandy.txt','r')
file_lines=my_file.readlines()
my_file.close()

line = file_lines[random.randrange(len(file_lines))]
print(line)
api.update_status(line)
# Create a for loop to iterate over file_lines
# for line in file_lines:
#     api.update_status(line)
 