import twint, os, nest_asyncio
import pandas as pd
from typing import List

def scrape_tweets(keyword, lang='en'):
    """
    Args:
        keyword (str): keyword to look for
        lang (str, optional): language string. Defaults to 'en'.
    Returns:
        pandas.DataFrame: dataframe containing information about the tweets
    """
    nest_asyncio.apply()
    df = pd.DataFrame()
    prev_size = -1
    size = len(df)  
    c = twint.Config()
    if os.path.isfile("resume.csv"):
        os.remove("resume.csv")
    c.Search = keyword
    c.Lang = lang 
    c.Limit = 100
    c.Pandas = True
    c.Pandas_au = True
    c.Hide_output = True
    c.Resume = "resume.csv" 
 
    while (prev_size != size):
        try:
            twint.run.Search(c)
            df = twint.storage.panda.Tweets_df
                
            prev_size = size
            size = len(df)
                
            if (prev_size != size):
                if len(df) > c.Limit:
                    df.drop(df.tail(len(df)-c.Limit).index,inplace=True)
                if os.path.isfile("resume.csv"):
                    os.remove("resume.csv")   
                return df
        except Exception as e:
            print('An error has occurred while scraping:', e)

class Scraper:

    def __init__(self, keyword) -> List[str]:
        self.data = scrape_tweets(keyword)
        self.tweets = self.data['tweet'].to_list()
        # self.[...]
        
        

