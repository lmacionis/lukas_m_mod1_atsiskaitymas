import unittest
from requests import HTTPError
from lukas_m_mod1_atsiskaitymas.crawl import Article
from unittest.mock import patch


class TestCrawl(unittest.TestCase):
    def setUp(self):
        self.data = Article("https://www.example.com")


    @patch("requests.get")
    def test_get_articles_response(self, mock_get):
        mock_get.return_value.status_code = 400

        with self.assertRaises(HTTPError):
            self.data.get_articles()


    @patch("requests.get")
    def test_get_articles_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = "Lorem Ipsum"

        try:
            self.data.get_articles()
        except Exception as error:
            raise TypeError({error})


    def test_get_articles(self):
        assert self.data.get_articles() == []


    def test_get_subject(self):
        assert self.data.get_subject() == []


    def test_get_article_url(self):
        assert self.data.get_article_url() == []


if __name__ == "__main__":
    unittest.main()