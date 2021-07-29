import statistics as stats
import preprocessor as prep
from textblob import TextBlob
from typing import List
from scraper import Scraper

def get_tweets(keyword: str) -> List[str]:
    scraper = Scraper(keyword)
    all_tweets = scraper.tweets
    return all_tweets

def clean_tweets(all_tweets: List[str]) -> List[str]:
    tweets_clean = []
    for tweet in all_tweets:
        tweets_clean.append(prep.clean(tweet))
    return tweets_clean

def get_sentiment(all_tweets: List[str]) -> List[str]:
    sentiment_scores = []
    for tweet in all_tweets:
        blob = TextBlob(tweet)
        sentiment_scores.append(blob.sentiment.polarity)
    return sentiment_scores

def avg_sentiment_score(keyword: str) -> int:
    tweets = get_tweets(keyword)
    tweets_clean = clean_tweets(tweets)
    sentiment_scores = get_sentiment(tweets_clean)
    avg_score = stats.mean(sentiment_scores)
    return avg_score

def compare_sentiment(first_thing, second_thing):
    first_score = avg_sentiment_score(first_thing)
    second_score = avg_sentiment_score(second_thing)
        
    if first_score > second_score:
        return first_thing
    elif first_score < second_score:
        return second_thing
    else: 
        return f'both {first_thing} and {second_thing}'