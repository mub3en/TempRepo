# Twitter Timeline Cleaner

This Python script allows you to delete old tweets from your Twitter timeline based on a specified cutoff date.

## Prerequisites

Before using this script, make sure you have the following prerequisites:

- Python 3.x installed on your machine
- The `tweepy` library installed. You can install it using `pip install tweepy`

## Setup

1. Clone this repository to your local machine.
2. Create a new Twitter application and obtain your Twitter API credentials. You can follow the official Twitter documentation to create an application and generate the necessary API keys and access tokens.
4. Open the `twitter_creds.py` file and replace the placeholders with your actual Twitter API credentials.

## Usage

1. Place the JSON file containing your tweet data in the `tweetdata` folder within the cloned repository. Make sure the file is named `tweet_MAINAccount.js`.
2. Open a terminal or command prompt and navigate to the cloned repository's directory.
3. Run the following command to execute the script:
4. The script will prompt you with the number of tweets that will be deleted based on the specified cutoff date.
5. Confirm the deletion by entering 'Y' or 'y' when prompted. The script will then start deleting the tweets one by one.
6. Once the process is complete, the script will display the number of tweets deleted and any errors encountered during the process.

## Configuration

You can customize the behavior of the script by modifying the following variables in the `delete_tweets.py` file:

- `days_to_keep`: Specifies the number of days of data you want to keep in your timeline. Tweets older than this number of days will be deleted.

## Notes

- Be cautious when using this script, as it permanently deletes tweets from your Twitter timeline.
- Twitter API has rate limits for accessing and deleting tweets. The script is designed to handle rate limits, but if you have a large number of tweets to delete, it may take some time to complete the process.

