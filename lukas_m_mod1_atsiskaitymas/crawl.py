from requests  import get
from lxml.etree import HTML


class Article:
    def __init__(self, source):
        self.source = source

    def get_subject(self):
        time_limit = 60
        formats =['.csv', '.txt', ".json"]
        response = get(self.source)
        text = response.text
        tree = HTML(text)
        articles = tree.xpath("//div[contains(@class, 'col-span-12 lg:col-span-4')]")
        subject_list = []
        for article in articles:
            subject = article.xpath(".//h2/a/text()")[0].strip()
            subject_list.append(subject)
        return subject_list


article1 = Article("https://www.lrytas.lt/")
print(article1.get_subject())
