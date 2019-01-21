import unittest
from user import User

class TestUser(unittest .TestCase):
    '''
    Tets case that defines test cases for the user class
    behaviours
    
    Args:
        unittest.TestUser: TestUser class that helps in creating test cases
    '''

    #******************************SetUp method**************************************************

    def setUp(self):
        '''
        set up method to run before each test cases
        '''
        self.new_user = User('Gerald' , 'Muchuki')
