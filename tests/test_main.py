import unittest
from lukas_m_mod1_atsiskaitymas.main import crawl


class TestMain(unittest.TestCase):
    def setUp(self):
        self.source = 1
        self.return_format = 1


    def test_crawl_data_type_list(self):
        with self.assertRaises(TypeError):
            crawl(self.source, self.return_format)
