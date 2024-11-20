import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_process(self):
        response = self.app.post('/process', json={"input": 10})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"result": 20})

if __name__ == "__main__":
    unittest.main()
