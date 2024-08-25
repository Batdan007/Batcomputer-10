import unittest
from unittest.mock import mock_open, patch
from langchain.schema import Document
from load_code import load_single_code


class TestLoadSingleCode(unittest.TestCase):
    def test_load_single_code(self):
        file_path = "/path/to/code.py"
        code = "print('Hello, World!')"

        with patch("builtins.open", mock_open(read_data=code)) as mock_file:
            result = load_single_code(file_path)

            mock_file.assert_called_once_with(file_path, encoding="utf-8")
            self.assertIsInstance(result, Document)
            self.assertEqual(result.page_content, code)
            self.assertEqual(result.metadata["source"], file_path)
            self.assertEqual(result.metadata["encoding"], "utf-8")


if __name__ == "__main__":
    unittest.main()