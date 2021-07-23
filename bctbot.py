import tweepy
import time
import random

auth = tweepy.OAuthHandler('token','token')
auth.set_access_token('token-token','token')
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()
b = 'b*ceta dx '

for tweet in api.home_timeline():
    try:
        with open('palavras.txt') as f:
            lines = f.readlines()
            pal = random.choice(lines)
            while (len(pal)<3 and pal!='cu'):
                pal = random.choice(lines)
            else:
                frase = b+pal
        
        api.update_status(frase)
        print('Tweetou')
        time.sleep(7200)

    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
