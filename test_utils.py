# repo1/test_utils.py
import unittest
from utils import process_data

class TestUtils(unittest.TestCase):
    def test_process_data(self):
        self.assertEqual(process_data("test"), "Processed: test")

if __name__ == '__main__':
    unittest.main()
