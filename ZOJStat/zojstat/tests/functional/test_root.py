from nose.tools import assert_true
from zojstat.tests import TestController

class TestRootController(TestController):
    """Tests for the method in the root controller."""

    def test_index(self):
        """The front page is working properly"""
        response = self.app.get('/')
        msg = 'SQUUUU'
        # You can look for specific strings:
        assert_true(msg in response)
        
    def test_query(self):
        """Query Page"""
        response = self.app.get('/query?user=cciv79')
        response = self.app.get('/query?user=vabc3')
