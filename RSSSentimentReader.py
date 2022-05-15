import feedparser
import pandas as pd
import SentoUtilities
from nltk.corpus import stopwords
from textblob import TextBlob

#Defining a function to process text for sentiment analysis, Removing punctuation and common stop words.
def preprocess(phrase):
    stop_words = stopwords.words('english')
    processedphrase = phrase
    processedphrase = processedphrase.replace('[^\w\s]', '')
    processedphrase = " ".join(word for word in processedphrase.split() if word not in stop_words)
    processedphrase = " ".join(Word(word).lemmatize() for word in processedphrase.split())
    return(processedphrase)

#Defining RSS reader process as a function
def getFeeds(url):
    #Most RSS feeds have an "entries" object which contains each articles payload
    feed = feedparser.parse(url)['entries']
   #print(feed[0].keys())

    #Specify columns for the upcoming dataframe
    columns = ['Datetime','Source','News','CleanedText','Sentiment','Polarity']
    payload = []

    #For each object in the recovered feed, Fetch the main article and preprocess the text to suit sentiment analysis
    for news in feed:
       #print(news['published'])
        #print((str(news).split('<p>', 6)[5]) + (str(news).split('<p>', 6)[6]))
        cleanedNews = Preprocess((str(news).split('<p>', 6)[5]) + (str(news).split('<p>', 6)[6]))

        sentiPayload = TextBlob(cleanedNews)
        NewsSentiment = sentiPayload.sentiment

        payload.append([news['published'], news['author'], (str(news).split('<p>', 6)[5]), cleanedNews, NewsSentiment[0], NewsSentiment[1]])# + (str(news).split('<p>', 6)[6])

    df = pd.DataFrame(payload, columns=columns)

    df.to_csv('Data/news.csv')

#I was fetching the feed from the below site, Lines 19, 30 and 35 may require altering depending upon your particular RSS feeds objects, Uncomment line 20 to view the full object and identify required variables.    
getFeeds("https://coinjournal.net/news/feed/")
