import os
from markovbot import MarkovBot


with open("tokens.txt", "r") as f:
    f_read = f.readline()
    print(f_read)
    access_token = f_read.split(" ")[2][0:-1]
    print(access_token)
    access_token_secret = f_read[1].split(" ")[1]
    cons_key = f_read[2].split(" ")[1]
    cons_secret = f_read[3].split(" ")[1]

print(access_token)
print(access_token_secret)
print(cons_key)
print(cons_secret)

# Initialise a MarkovBot instance
tweetbot = MarkovBot()

# Get the current directory's path
dirname = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the book
book = os.path.join(dirname, 'ElonMuskTxt.txt')
# Make your bot read the book!
tweetbot.read(book)