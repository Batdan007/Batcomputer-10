import unittest
from unittest.mock import patch
from load_llm import check_together_api_key

class TestCheckTogetherApiKey(unittest.TestCase):
    @patch("builtins.input", return_value="your_together_api_key")
    @patch("builtins.open")
    def test_check_together_api_key(self, mock_open, mock_input):
        check_together_api_key()

        mock_open.assert_called_once_with(".env", "a")
        mock_open.return_value.write.assert_called_once_with(
            '\nTOGETHER_API_KEY="your_together_api_key"'
        )
        mock_input.assert_called_once_with("Enter your OpenAI API key: ")

if __name__ == "__main__":
    unittest.main()

class TestCheckTogetherApiKey(unittest.TestCase):
    @patch("builtins.input", side_effect=["your_together_api_key", "your_openai_api_key"])
    @patch("builtins.open")
    def test_check_together_api_key(self, mock_open, mock_input):
        check_together_api_key()

        mock_open.assert_called_once_with(".env", "a")
        mock_open.return_value.write.assert_called_once_with(
            '\nTOGETHER_API_KEY="your_together_api_key"'
        )
        mock_input.assert_called_once_with("Enter your OpenAI API key: ")