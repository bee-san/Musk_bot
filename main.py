import os
from markovbot import MarkovBot


with open("tokens.txt", "r") as f:
    f_read = f.readline()
    access_token = "952160751157960704-ek5scwczzdQKgO9MRrDZbAAQV4L3ZAv" # f_read.split(" ")[2][0:-1]
    access_token_secret = "o3cygwweV3uXvY3MIg1aNGq761gCcX6yUWY4hIZkPvU0h"
    cons_key = "36wM5DmrtL3Rb0kqbZ3DJkcYD"
    cons_secret = "a3udTGncmjkf08xH8NnVGQni6CNzp3WpU8yjHuOtFeUcxonpyg"

# Initialise a MarkovBot instance
tweetbot = MarkovBot()

# Get the current directory's path
dirname = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the book
book = os.path.join(dirname, 'ElonMuskTxt.txt')
# Make your bot read the book!
tweetbot.read(book)

my_first_text = tweetbot.generate_text(25, seedword=['space', 'Tesla'])
print("tweetbot says:")
print(my_first_text)

tweetbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)

from time import sleep
while True:
    tweetbot.twitter_tweeting_start(days=0, hours=0, minutes=30, keywords=['SpaceX', 'Tesla', 'Mars', 'Solar', 'Do more', '120 hour work week', 'I am not an alien', 'launch'], prefix=None, suffix="#ElonMusk")
    sleep(30)