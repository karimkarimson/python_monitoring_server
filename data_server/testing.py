import unittest
from flask import Flask
from flask_testing import TestCase
from unittest.mock import patch, MagicMock
from server import app

class MyTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    @patch('subprocess.run')
    def test_latency_check_start_success(self, mock_subprocess):
        mock_subprocess.return_value = MagicMock(returncode=0, stdout=b'', stderr=b'')
        response = self.client.get("/service/latency_check/start")
        self.assert200(response)
        self.assertIn('true', response.json['success'])
        self.assertIn('', response.json['message'])

    @patch('subprocess.run')
    def test_latency_check_start_failure(self, mock_subprocess):
        mock_subprocess.return_value = MagicMock(returncode=1, stdout=b'', stderr=b'error')
        response = self.client.get("/service/latency_check/start")
        self.assert200(response)
        self.assertIn('false', response.json['success'])
        self.assertIn('error', response.json['message'])

if __name__ == '__main__':
    unittest.main()