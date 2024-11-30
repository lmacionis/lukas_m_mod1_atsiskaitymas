import  unittest
from requests import HTTPError

from lukas_m_mod1_atsiskaitymas.crawl import Article
from unittest.mock import patch

class TestCrawl(unittest.TestCase):
    @patch("requests.get")

    def test_get_articles(self, mock_get):
        article = Article("www.example.com")
        mock_get.return_value.status_code = 400

        with self.assertRaises(HTTPError):
            article.get_articles()


if __name__ == "__main__":
    unittest.main()