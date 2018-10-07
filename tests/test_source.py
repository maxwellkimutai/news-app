import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method thatt will run before every Test
        '''
        self.new_source = Source('Test id','Test name','Test description','Test categoty','Test language')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))
