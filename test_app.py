import unittest
from my_own_api import app  

class TestFlaskAPI(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True  

    def test_get_quotes_by_philosopher(self):
        response = self.app.get('/quotes/philosopher/nietzsche')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)  

    def test_get_quotes_nonexistent_philosopher(self):
        response = self.app.get('/quotes/philosopher/unknown')
        self.assertEqual(response.status_code, 404)
        self.assertIn('error', response.json)

    def test_post_add_new_quote(self):
        new_quote = {"quote": "He who has a why to live can bear almost any how."}
        response = self.app.post('/quotes/philosopher/nietzsche', json=new_quote)
        print("Response JSON:", response.json)
        print("Response Status Code:", response.status_code)
        self.assertEqual(response.status_code, 201)
        self.assertIn('quote_entry', response.json)
        self.assertEqual(response.json['quote_entry']['quote'], new_quote['quote'])

    def test_post_add_invalid_quote(self):
        invalid_quote = {"quote": " "}
        response = self.app.post('/quotes/philosopher/nietzsche', json=invalid_quote)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

    def test_post_add_duplicate_quote(self):
        quote = {"quote": "This is a unique quote."}
        response = self.app.post('/quotes/philosopher/nietzsche', json=quote)

        duplicate_response = self.app.post('/quotes/philosopher/nietzsche', json=quote)
        self.assertEqual(duplicate_response.status_code, 400) 
        self.assertIn('error', duplicate_response.json)
        self.assertEqual(duplicate_response.json['error'], "This quote already exists for the philosopher")

if __name__ == '__main__':
    unittest.main()
