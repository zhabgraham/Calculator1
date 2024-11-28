import unittest
from unittest.mock import patch, Mock
from lab7.classes.data_repository import DataRepository

class TestDataRepository(unittest.TestCase):
    @patch("lab7.classes.data_repository.requests.get")
    def test_get_data_success(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = [{"id": 1, "name": "Test User"}]
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        repo = DataRepository("users")
        data = repo.get_data()
        self.assertEqual(data, [{"id": 1, "name": "Test User"}])
        mock_get.assert_called_once_with("https://jsonplaceholder.typicode.com/users")

    @patch("lab7.classes.data_repository.requests.get")
    def test_get_data_failure(self, mock_get):
        mock_get.side_effect = Exception("Error fetching data")

        repo = DataRepository("users")
        with self.assertRaises(Exception) as context:
            repo.get_data()
        self.assertIn("Error fetching data", str(context.exception))

if __name__ == '__main__':
    unittest.main()
