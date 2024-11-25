from lukas_m_mod1_atsiskaitymas.crawl import Article
from lukas_m_mod1_atsiskaitymas.save_data import *

def crawl(source, return_format="json", time_limit=60):
    if source == "lrytas":
        source_url = "https://www.lrytas.lt"
        get_article = Article(source_url)
        titles = get_article.get_subject()
        article_urls = get_article.get_article_url()
        if return_format == "csv":
            save_as_csv(source_url, titles, article_urls)
        elif return_format == "dict":
            create_dict(source_url, titles, article_urls)
        else:
            save_as_json(source_url, titles, article_urls)



if __name__=="__main__":
    crawl(source="lrytas", return_format="csv")
