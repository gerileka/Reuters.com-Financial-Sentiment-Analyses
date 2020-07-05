#!/usr/bin/env python
# coding: utf-8

# In[75]:


from Link_function import get_links

import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[89]:


def get_data(pages):
    
    news_url = get_links(pages)
    
    date_list = []
    title_list = []
    text_list = []
    html_list = []

    for url in news_url:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        article_date = soup.find('div', class_='ArticleHeader_date').get_text().split('/')[0]
        article_title = soup.find('h1', class_='ArticleHeader_headline').get_text()
        article_text = soup.find('div', class_='StandardArticleBody_body').get_text()
        article_html = soup

        date_list.append(article_date)
        title_list.append(article_title)
        text_list.append(article_text)
        html_list.append(article_html)

    dict_df = {'Title': title_list, 'Date': date_list, 'URL': news_url,'Text': text_list,'HTML_content': html_list}  
    df_data = pd.DataFrame(dict_df) 
    
    df_data.to_excel('../data/content.xlsx',index=False)
    
    return df_data
    

