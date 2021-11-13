## install relevant libraries

# !pip install -q bert-extractive-summarizer
# !pip install -q neuralcoref
# !pip install -q transformers
# !pip3 install -q news-please
# !pip3 install -q cchardet
# !pip install -q keybert
# !pip install -q beautifulsoup4

## import necesary libraries

from colab import *
import requests
from bs4 import BeautifulSoup
import re
import urllib.parse
from urllib.parse import urlparse
from newsplease import NewsPlease
from keybert import KeyBERT
from transformers import pipeline

"""**Tweet**"""

tweet = "Pakistan PM Imran Khan tests positive for Covid19 48 hours after getting the Chinese Sinopharm vaccine shot. Under observation."
print(tweet)

"""# **Step 1**: Extracting keywords from the tweet"""

from keybert import KeyBERT
model = KeyBERT('distilbert-base-nli-mean-tokens')

keywords = model.extract_keywords(tweet, keyphrase_ngram_range=(1,1))
keywords = [i[0] for i in keywords]
keywords = "+".join(keywords)

print(keywords)

"""# **Step 2**: Extracting relevant news articles wrt keywords"""

url = "https://www.google.com/search?q=" + keywords + "&tbm=nws"
url

import requests
from bs4 import BeautifulSoup
import re
import urllib.parse
from urllib.parse import urlparse
def googleSearch(url):
    g_clean = [ ] 
    
    try:
        html = requests.get(url)
        if html.status_code==200:
            soup = BeautifulSoup(html.text, 'lxml')
            a = soup.find_all('a') #// a is a list
            for i in a:
                k = i.get('href')
                try:
                    m = re.search("(?P<url>https?://[^\s]+)", k)
                    n = m.group(0)
                    rul = n.split('&')[0]
                    domain = urlparse(rul)
                    if (re.search('google.com', domain.netloc)):
                        continue
                    else:
                        g_clean.append(rul)
                except:
                    continue
    except Exception as ex:
        print(str(ex))
    finally:
        return g_clean

news_urls = googleSearch(url)

len(news_urls), news_urls[:3]



"""**Scraping the news from these urls**"""

from newsplease import NewsPlease

news_content = []


for url in news_urls:
    try:
        article = NewsPlease.from_url(url)
        title = article.title
        description = article.description
        main_text = article.maintext

        content = str(title) + " " + str(description) + " " + str(main_text)
        news_content.append(content)
    except:
        continue
    
    if (len(news_content) >= 5):
        break

news_content

"""# **Step 3**: Summarizing from these news_content"""

from transformers import pipeline

summarizer = pipeline("summarization")

summarized_news = []

for i in news_content:
    try:
      summary = summarizer(i, max_length=250, min_length=30, do_sample=False)
      summarized_news.append(summary[0]['summary_text'])
    except:
      summarized_news.append("")

# now summarizing all the summaries

combined_summary = summarizer(" ".join(summarized_news), max_length=250, min_length=30, do_sample=False)
combined_summary = combined_summary[0]['summary_text']

combined_summary





"""---
# **Combining everything together in 1 function**
"""

model = KeyBERT('distilbert-base-nli-mean-tokens')
summarizer = pipeline("summarization")

# defining helper functions

def return_keywords(tweet):
    keywords = model.extract_keywords(tweet, keyphrase_ngram_range=(1,1))
    keywords = [i[0] for i in keywords]
    keywords = "+".join(keywords)

    return keywords


def get_news_urls(keywords):
    url = "https://www.google.com/search?q=" + keywords # + "&tbm=nws"
    g_clean = [ ] 
    
    try:
        html = requests.get(url)
        if html.status_code==200:
            soup = BeautifulSoup(html.text, 'lxml')
            a = soup.find_all('a') #// a is a list
            for i in a:
                try:
                    m = re.search(r'/url[?]q=(.*?)&amp', str(i)).group(1)
                    if m not in g_clean:
                        g_clean.append(m)
                except:
                    continue
    except Exception as ex:
        print(str(ex))
    finally:
        return g_clean

def get_news_content(news_urls, top_n = 5):
    news_content = []

    for url in news_urls:
        try:
            article = NewsPlease.from_url(url)
            title = article.title
            description = article.description
            main_text = article.maintext

            content = str(title) + " " + str(description) + " " + str(main_text)
            news_content.append(content)
            print(url)
        except:
            continue
        
        if (len(news_content) >= top_n):
            break
    
    return news_content

def get_summarized_news(news_content):
    summarized_news = []

    for i in news_content:
        try:
          summary = summarizer(i, max_length=250, min_length=30, do_sample=False)
          summarized_news.append(summary[0]['summary_text'])
        except:
          summarized_news.append("")
    
    # now summarizing all the summaries
    combined_summary = summarizer(" ".join(summarized_news), max_length=250, min_length=30, do_sample=False)
    combined_summary = combined_summary[0]['summary_text']

    return combined_summary

def get_summary(tweet):
    # Step 1: Extract keywords
    keywords = "+".join(list(map(str, tweet.split(" "))))
    # Step 2: get_news_urls
    news_urls = get_news_urls(keywords)
    # Step 3: get_news_content
    news_content = get_news_content(news_urls, top_n = 4)
    # Step 4 (final step): get_summarized_news
    summary = get_summarized_news(news_content) 
    return summary

# get latest fake news from https://www.altnews.in/

tweet = "It is mandatory to apply masks in all police station areas of Uttar Pradesh from 9 am to 30 days tomorrow. A person who will be caught without a mask should remain in temporary jail for 10 hours. Put on masks for two yards, of yourself and family with a corona-like illness Save."
summary = get_summary(tweet)
print("-------------")
print(tweet)
print("-------------")
print(summary)

"""# Experiment"""
# Step 1: Extract keywords
keywords = "+".join(list(map(str, tweet.split(" "))))
# Step 2: get_news_urls
news_urls = get_news_urls(keywords)

print(keywords)

print(news_urls)

url = "https://www.google.com/search?q=" + keywords + "&tbm=nws"
html = requests.get(url)
soup = BeautifulSoup(html.text, 'lxml')
a = soup.find_all('a') #// a is a list

print(a)
print(a[20])

for i in a:
  try:
    print(re.search(r'/url[?]q=(.*?)&amp', str(i)).group(1))
  except:
    continue