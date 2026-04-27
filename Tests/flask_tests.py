'''
A starter file for testing a Flask app
Run with:
python -m unittest flask_tests.py
'''

from flask_lab_app import *
import unittest

class TestSOMETHING(unittest.TestCase):
    def test_route(self):
        #sets up a special test app
        self.app = app.test_client() 
        #test app returns TestResponse object
        response = self.app.get('/', follow_redirects=True) 
        #TestResponse has webpage in .data
        self.assertEqual(b'hello, this is the homepage', response.data) 