import unittest
from cd import app

class TestApp(unittest.TestCase):
    
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        
    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, world!')
        
    def test_cow(self):
        response = self.app.get('/cow')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'MOoooOo!')

if __name__ == '__main__':
    unittest.main()

