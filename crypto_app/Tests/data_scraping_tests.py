import unittest
from unittest.mock import patch, MagicMock
from utils.scraping_utils import scrape_data

class TestScrapeData(unittest.TestCase):

    @patch("scraping_utils.webdriver.Chrome")
    def test_scrape_data(self, mock_driver):
        # Mock the web driver instance and its methods
        mock_instance = mock_driver.return_value
        mock_instance.find_elements_by_class_name.return_value = [MagicMock()]
        mock_instance.page_source = "<html><body>Mocked HTML</body></html>"

        # Run the scraping function
        result = scrape_data()

        # Assertions
        self.assertIsInstance(result, list)
        self.assertTrue(mock_instance.quit.called)

if __name__ == "__main__":
    unittest.main()

























