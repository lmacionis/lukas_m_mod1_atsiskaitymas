from lukas_m_mod1_atsiskaitymas.crawl import article_urls, titles, source_url
import pandas as pd
import re
import pprint
import json

def save_as_csv():
    url_of_article = [source_url + item for item in article_urls]

    dict_for_csv = {'Title': titles, 'LINK': url_of_article}
    df = pd.DataFrame(dict_for_csv)         # data frame
    df.to_csv('data_as.csv')
    df.index += 1                           # In terminal shows that it starts from 1, but in libre it still starts from 0


def create_dict():
    data_dict = {}
    temp_key = "Subject 0"
    url_of_articles = [source_url + item for item in article_urls]

    for num, (title, article_url) in enumerate(zip(titles, url_of_articles)):
        num += 1
        key1 = re.sub(r'\d', str(num), temp_key)
        data_dict[key1] = {"Title": title, "Link": article_url}

# Leaving for reference purposes, this creates nested dict with same last article and last url
#    for number in range(len(titles)):
#        number += 1
#        key1 = re.sub(r'\d', str(number), temp_key)
#
#        key2 = "Title"
#        key3 = "Link"
#
#        for title in titles:
#            for article_url in [source_url + item for item in article_urls]:
#                data_dict[key1] = {key2: title, key3: article_url}
    return data_dict


def save_as_json():
    with open("dict_data.json", "w") as file:
        json.dump(create_dict(), file)

save_as_json()
