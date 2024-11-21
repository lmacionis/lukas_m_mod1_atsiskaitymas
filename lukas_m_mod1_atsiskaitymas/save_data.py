from lukas_m_mod1_atsiskaitymas.crawl import article_url, title, source_url
import pandas as pd


def save_as_csv():
    url_of_article = [source_url + item for item in article_url]

    dict_for_csv = {'Title': title, 'LINK': url_of_article}
    df = pd.DataFrame(dict_for_csv)         # data frame
    df.to_csv('data_as.csv')
    df.index += 1

save_as_csv()
