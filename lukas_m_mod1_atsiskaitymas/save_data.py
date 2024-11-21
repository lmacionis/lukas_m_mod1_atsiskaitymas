from lukas_m_mod1_atsiskaitymas.crawl import article_url, title, source_url
import pandas as pd
import re

def save_as_csv():
    url_of_article = [source_url + item for item in article_url]

    dict_for_csv = {'Title': title, 'LINK': url_of_article}
    df = pd.DataFrame(dict_for_csv)         # data frame
    df.to_csv('data_as.csv')
    df.index += 1                           # In terminal shows that it starts from 1, but in libre it still starts from 0


def save_as_dict():
    data_dict = {}
    temp_key = "Subject 0"
    #url_of_article = [source_url + item for item in article_url]
    for number in range(len(title)):
        number += 1
        key1 = re.sub(r'\d', str(number), temp_key)

        key2 = "Title"
        key3 = "Link"
        for i in title:
            for j in [source_url + item for item in article_url]:
                data_dict[key1] = {key2: i, key3: j}

    return data_dict

print(save_as_dict())
