import pandas as pd
import re
import json

def save_as_csv(source_url, titles, article_urls):
    url_of_article = [source_url + item for item in article_urls]
    dict_for_csv = {"Title": titles, "LINK": url_of_article}
    df = pd.DataFrame(dict_for_csv)         # data frame
    df.index += 1
    df.to_csv("data_as.csv")


def create_dict(source_url, titles, article_urls):
    data_dict = {}  # dict
    temp_key = "Subject 1"  # str
    url_of_articles = [source_url + item for item in article_urls]  # list

    for num, (title, article_url) in enumerate(zip(titles, url_of_articles)):
        num += 1
        key1 = re.sub(r'\d', str(num), temp_key)
        data_dict[key1] = {"Title": title, "Link": article_url}

    return data_dict


def save_as_json(source_url, titles, article_urls):
    data_dict = create_dict(source_url, titles, article_urls)
    with open("dict_data.json", "w") as file:
        json.dump(data_dict, file)
