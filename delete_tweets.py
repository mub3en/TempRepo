import tweepy
import twitter_creds as tc
import json
from datetime import datetime, timedelta, timezone
import time

if __name__ == "__main__":
    auth = tweepy.OAuthHandler(tc.CONSUMER_KEY, tc.CONSUMER_SECRET_KEY)
    auth.set_access_token(tc.ACCESS_TOKEN, tc.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    days_to_keep = 365  # number of days of the data you are keeping.
    cutoff_date = datetime.now(timezone.utc) - timedelta(days=days_to_keep)

    print("Tweets from the beginning of your account (@" + api.verify_credentials().screen_name + ") to '" + str(
        cutoff_date) + "' will be deleted.\n")

    with open("./tweets_data/RAW_FILE_DOWNLOADED_THROUGH_TWIITER_DATA.js", "r") as fp:
        myjson = json.load(fp)

    count = 0
    isDone = 0
    for tweet in myjson:
        d = datetime.strptime(tweet['tweet']['created_at'], "%a %b %d %H:%M:%S %z %Y")
        if d < cutoff_date:
            try:
                api.destroy_status(tweet['tweet']['id_str'])
                print(tweet['tweet']['id_str'] + " : " + tweet['tweet']['full_text'] + " --- has been wiped from the face of this planet earth.\n")
                time.sleep(1 * 0.01)
                count += 1
            except tweepy.TweepError as e:
                print("Error on data: %s" % str(e))
                print(tweet['tweet']['id_str'] + " --- didn't purge.\n")
                isDone += 1
                continue

    print("Deleted: " + str(count))
    print("Already Deleted: " + str(isDone))
