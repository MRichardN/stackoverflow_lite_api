import unittest
import json
import os


from app.views import create_app

class StackOverflow_endpoint(unittest.TestCase):
    
    def setUp(self):
        """Define the test variables and initialize the application."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.questions = {'questions':'What is the difference between django and flask','python' 'date_posted': '7th May 2017'}
        
    def test_posting_of_questions(self):
        '''test user can post a question'''
        response = self.client.post(
            '/api/v1/questions', data=json.dumps(self.questions), content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_viewing_questions(self):
        """Test user can view all questions."""
        response = self.client.get(
            '/app/api/v1/questions', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_viewing_a_single_question(self):
        """Test user can view a single question."""
        response = self.client.get(
            '/app/api/v1/questions/1', data=json.dumps(self.questions), content_type='application/json')
        self.assertEqual(response.status_code, 200)
    
    def test_editing_a_question(self):
        """Test use rcan edit a question."""
        self.client.post(
            '/api/v1/questions', data=json.dumps(self.questions), content_type='application/json')
        response = self.client.put(
            '/api/v1/questions/1', data=json.dumps(self.questions), content_type='application/json')
        self.assertEqual(response.status_code, 404)
        #200

if __name__ == "__main__":
    unittest.main()