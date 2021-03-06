import unittest
import os
import json

from app.views import create_app
from app.models import User

class StackOverflow_endpoint_Users(unittest.TestCase):
    """This class represent application users."""

    def setUp(self):
        """Define test variables and initialize."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.users = {'name': 'James Bond', 'email': 'jamesbond@gmail.com', 'password': 'james'}

    def test_registering_new_user(self):
        """Test user sign_up."""
        response = self.client.post(
            '/api/v1/auth/signup', data=json.dumps(self.users), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_user_login(self):
        """Test user login."""
        response = self.client.post(
            '/api/v1/auth/login', data=json.dumps(self.users), content_type='application/json')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
