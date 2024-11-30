import requests
from lxml.etree import HTML
from requests import HTTPError


class Article:
    def __init__(self, source):
        self.source = source

    def get_articles(self):
        response = requests.get(self.source)

        if response.status_code == 200:
            text = response.text    # str
            tree = HTML(text)
            articles = tree.xpath("//div[contains(@class, 'col-span-12 lg:col-span')]")
            return articles
        else:
            raise HTTPError(f"Page is unreachable: {response.status_code}")

    def get_subject(self):
        articles_list = [self.get_articles()]
        subject_list = []

        for article in articles_list[0]:
            subject = article.xpath(".//h2/a/text()")[0].strip()
            subject_list.append(subject)

        return subject_list

    def get_article_url(self):
        articles_list = [self.get_articles()]
        url_list = []

        for link in articles_list[0]:
            url = link.xpath(".//a/@href")[0]
            url_list.append(url)

        return url_list
