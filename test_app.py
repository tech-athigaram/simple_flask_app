import unittest
import json
from app import app, users

class BasicTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        # Reset users list before each test
        users.clear()
        users.extend([
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"}
        ])

    def test_get_users(self):
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['name'], 'Alice')
        self.assertEqual(data[1]['name'], 'Bob')

    def test_add_user(self):
        new_user = {"name": "Charlie"}
        response = self.app.post('/users', data=json.dumps(new_user), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['name'], 'Charlie')
        self.assertEqual(data['id'], 3)
        # Check if user was added
        response = self.app.get('/users')
        data = response.get_json()
        self.assertEqual(len(data), 3)

    def test_get_user_by_id_found(self):
        response = self.app.get('/users/1')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['name'], 'Alice')

    def test_get_user_by_id_not_found(self):
        response = self.app.get('/users/999')
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()
# We recommend installing an extension to run python tests.
