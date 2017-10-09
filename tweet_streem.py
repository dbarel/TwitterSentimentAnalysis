from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from textblob import TextBlob
import datetime
import sys


def give_keywords():
    try:
        with open('configuration.txt') as config:
            for line in config:
                if line.startswith('PERSON.KEYWORDS ='):
                    keys = line.split('|')
                    keys[0] = keys[0][18:]
                    return keys[1:]
            else:
                return
    except FileNotFoundError:
        sys.exit('configuration.txt file was not found, program will close')


class Listener(StreamListener):
    def on_data(self, data):
        try:
            tweet = json.loads(data)
            print(tweet['text'])
            analysis = TextBlob(tweet['text']).sentiment
            if analysis.polarity > 0.1:
                sentiment = ',1\n'
            elif analysis.polarity < -0.1:
                sentiment = ',-1\n'
            else:
                sentiment = ',0\n'
            print(str(analysis.polarity), str(analysis.subjectivity))
            # date = tweet['created_at'][4:19] + tweet['created_at'][-5:] #time format may change by the OS.
            # converting datetime to flot, less readable but much fester to calculate time delta with it.
            date = str((datetime.datetime.utcnow() - datetime.datetime(2017, 1, 1)).total_seconds())
            with open('chart_this\\sentiment.csv', 'a', newline='') as f:
                f.write(date + sentiment)
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            return True

    def on_error(self, status_code):
        print(status_code)


if __name__ == '__main__':

    consumer_key = "aMTLPIi8R3z0nokw5orML2dHn"
    consumer_secret = "bEM77bewDizStiCQYIsYpYg1glJW8NcGOOO8gem7t3HhC8pw60"
    consumer_token = "40377526-hvC6R1SCn3hAt01MjdIrc8RfTOR7BgeIrxAh1I20R"
    token_secret = "vIsm795sY48wZs0IS5ZAlzNBes5BzeiUZDu2B98tscT7I"

    with open('chart_this\\sentiment.csv', 'w', newline='') as file:
        file.write('')

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(consumer_token, token_secret)
    twitterStream = Stream(auth, Listener())
    key_word = give_keywords()

    if key_word:
        twitterStream.filter(track=key_word, languages=['en'])
    else:
        sys.exit('no line star with PERSON.KEYWORDS = in configuration, program will close')
