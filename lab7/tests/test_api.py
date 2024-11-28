import unittest
from lab7.classes.api_config import APIConfig

class TestAPIConfig(unittest.TestCase):
    def test_singleton_instance(self):
        config1 = APIConfig()
        config2 = APIConfig()
        self.assertIs(config1, config2)

    def test_base_url(self):
        config = APIConfig()
        self.assertEqual(config.base_url, "https://jsonplaceholder.typicode.com")

if __name__ == '__main__':
    unittest.main()
