import  unittest
from requests import HTTPError
from lukas_m_mod1_atsiskaitymas.crawl import Article
from unittest.mock import patch


class TestCrawl(unittest.TestCase):
    @patch("requests.get")

    # Testing if response code is 200 if not raise error
    def test_get_articles_response(self, mock_get):
        article = Article("www.example.com")
        mock_get.return_value.status_code = 404

        with self.assertRaises(HTTPError):
            article.get_articles()

    # ToDo Need to fix this
    @patch("requests.Response")
    def test_get_articles_data(self, mock_response):
        mock_response.return_value.text = 1
        data = Article("https://example.com")

    # Testing if return value is list
    def test_get_articles(self):
        data = Article("https://example.com")
        assert data.get_articles() == []

    def test_get_subject(self):
        data = Article("https://example.com")
        assert data.get_subject() == []

    def test_get_article_url(self):
        data = Article("https://example.com")
        assert data.get_article_url() == []


if __name__ == "__main__":
    unittest.main()