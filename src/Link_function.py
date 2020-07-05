#!/usr/bin/env python
# coding: utf-8

# In[2]:


def get_one_link(url):
    import requests
    from bs4 import BeautifulSoup
    
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    news_link = []
    column_href = soup.find('div', class_='news-headline-list')
    for link in column_href.find_all('a'):
        news_link.append('https://www.reuters.com'+link.get('href'))
    news_link = list(set(news_link))
    
    return news_link


def get_links(pages):
    
    import itertools
    
    news_url = []
    for p in range(1,pages+1):
        url = 'https://www.reuters.com/news/archive/bank-news?view=page&page='+str(p)+'&pageSize=10'
        print(url)
        news_url.append(get_one_link(url))
    news_url = list(set(list(itertools.chain(*news_url))))
    
    return news_url


# ### _Test_ 

# In[5]:


# url= 'https://www.reuters.com/news/archive/bank-news?view=page&page=1&pageSize=10'
# get_links(url)


# In[ ]:




