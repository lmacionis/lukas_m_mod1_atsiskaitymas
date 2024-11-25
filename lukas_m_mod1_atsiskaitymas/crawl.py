from requests  import get
from lxml.etree import HTML


class Article:
    def __init__(self, source):
        self.source = source

    def get_articles(self):
        response = get(self.source)
        text = response.text
        tree = HTML(text)
        articles = tree.xpath("//div[contains(@class, 'col-span-12 lg:col-span')]")
        return articles

    def get_subject(self):
        time_limit = 60
        subject_list = []
        for article in self.get_articles():
            subject = article.xpath(".//h2/a/text()")[0].strip()
            subject_list.append(subject)
        return subject_list

    def get_article_url(self, url=None):
        url_list = []
        for link in self.get_articles():
            url = link.xpath(".//a/@href")[0]
            url_list.append(url)
        return url_list
