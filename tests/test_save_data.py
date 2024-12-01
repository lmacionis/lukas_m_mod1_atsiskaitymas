import unittest
from lukas_m_mod1_atsiskaitymas.save_data import save_as_json, save_as_csv
from unittest.mock import  patch, mock_open


class TestSaveData(unittest.TestCase):
    def setUp(self):
        self.source_url = "www.example.com"
        self.titles = ["Lorem Ipsum"]
        self.url_of_articles = ["www.y.com"]


    @patch("builtins.open", new_callable=mock_open)
    def test_save_as_csv(self, mock_file_open):
        save_as_csv(self.source_url, self.titles, self.url_of_articles)
        mock_file_open.assert_called_once_with("data_as.csv", "w", encoding='utf-8', errors='strict', newline='')


    @patch("builtins.open", new_callable=mock_open)
    def test_save_as_json(self, mock_file_open):
        save_as_json(self.source_url, self.titles, self.url_of_articles)
        mock_file_open.assert_called_once_with("dict_data.json", "w")


if __name__ == '__main__':
    unittest.main()