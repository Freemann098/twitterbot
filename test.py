from twython import Twython
import random

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

messages = [
        "Have a good day",
        "You can do it",
        "I love you",
        "You smell wondeful",
        "Even though you smell bad, you look great",
        "Atleast you tried!",
        "You really are a good person, beleive me",
        
]

message = random.choice(messages)
twitter.update_status(status=message)
print("Tweeted: {}".format(message))
