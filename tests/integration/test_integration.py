import unittest
from repo1.functions import process_output

class TestIntegration(unittest.TestCase):
    def test_process_output(self):
        input_value = 10
        expected_output = 25  # (10 * 2) + 5
        self.assertEqual(process_output(input_value), expected_output)

if __name__ == "__main__":
    unittest.main()
