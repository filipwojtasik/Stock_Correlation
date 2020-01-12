import yfinance as yf
import numpy as np
import os
import requests
from newsapi import NewsApiClient



newsapi = NewsApiClient(api_key='97daaf4147dc4277a56b4fb2106d4bcc')
q='amazon'

if not os.path.exists(q):
    os.makedirs(q)
if not os.path.exists(q+'fin'):
    os.makedirs(q+'fin')

for i in range(30):
    if i<3:
        d=i-15
        all_articles = newsapi.get_everything(q=q,
                                              from_param=f'2019-10-{i+28}',
                                              to=f'2019-10-{i+28}',
                                              language='en',
                                              sort_by='popularity'
                                              ,page_size=100,
                                              #sources='bbc-news,the-verge,australian-financial-review,bloomberg,business-insider,business-insider-uk,financial-post,fortune,the-wall-street-journal,wired,the-verge,the-new-york-times,techradar,techcrunch'
                                              )

    if i>2 and i <12:
        d = i - 2
        all_articles = newsapi.get_everything(q=q,
                                              from_param=f'2019-11-0{d}',
                                              to=f'2019-11-0{d}',
                                              language='en',
                                              sort_by='popularity'
                                              , page_size=100,
                                              #sources='bbc-news,the-verge,australian-financial-review,bloomberg,business-insider,business-insider-uk,financial-post,fortune,the-wall-street-journal,wired,the-verge,the-new-york-times,techradar,techcrunch'
                                              )
    if i>11:
        d = i - 2
        all_articles = newsapi.get_everything(q=q,
                                              from_param=f'2019-11-{d}',
                                              to=f'2019-11-{d}',
                                              language='en',
                                              sort_by='popularity'
                                              , page_size=100,
                                              #sources='bbc-news,the-verge,australian-financial-review,bloomberg,business-insider,business-insider-uk,financial-post,fortune,the-wall-street-journal,wired,the-verge,the-new-york-times,techradar,techcrunch'
                                              )


    title=[]
    ind=[]
    title2=[]

    #with open('apple.json', 'r') as json_file:
    #        line = json.load(json_file)

    line=all_articles
    '''
    g = open(f"{q}/{i}{q}.txt", "wb")

    for i in range(int(100)):
        try:
            title.append(line['articles'][i]['title'])
            if title[i] != None:
                strr=title[i]+'\n'
                g.write(strr.encode('utf8'))
        except:
            break

    g.close()
    
    g = open(f"{q}art/{i}{q}art.txt", "wb")

    for i in range(int(100)):
        try:
            title2.append(line['articles'][i]['description'])
            if title2[i] != None:
                strr = title2[i] + '\n'
                g.write(strr.encode('utf8'))
        except:
            break

    g.close()
    '''
    g = open(f"{q}fin/{i}{q}fin.txt", "wb")

    for i in range(int(100)):
        try:
            title2.append(line['articles'][i]['title'])
            if title2[i] != None:
                strr = title2[i] + '\n'
                g.write(strr.encode('utf8'))
        except:
            break

    g.close()
