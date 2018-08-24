import unittest
import json
import os


from app.views import create_app
from app.__init__ import create_app

class TestStackOverflow_endpoint_answers(unittest.TestCase):
    """This class represents stackoverflow-lite endpoint test case"""
    
    def setUp(self):
        """Define the test variables and initialize the application."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.answers = {'id':1,'ask':'What is the difference between django and flask','language':'python', 'date_posted': '7th May 2017'}
    
    def test_viewing_answers(self):
        """Test user can view all answers."""
        response = self.client.get(
            '/api/v1/questions/answers', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_viewing_a_single_answer(self):
        """Test user can view a single answer."""
        response = self.client.get(
            '/api/v1/questions/1', data=json.dumps(self.answers), content_type='application/json')
        self.assertEqual(response.status_code, 200)


   
         
'''
    def test_posting_answer__to_specific_questions(self):
        """test user can post a answer/s to a specific question (POST request)"""
        response = self.client.post(
            '/api/v1/1/answers', data=json.dumps(self.answers), content_type='application/json')
        self.assertEqual(response.status_code, 201)      
'''

if __name__ == "__main__":
    unittest.main()        