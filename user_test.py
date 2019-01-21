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

    #******************************tearDown method******************************************************

                            #tearDown here

    #*******************************Create user test******************************************************

    def test_init(self):
        '''
        Test to see if users are instanciated properties
        '''
        self.assertEqual(self.new_user.first_name , 'Gerald')
        self.assertEqual(self.new_user.last_name , 'Muchuki')

    #******************************save user test**********************************************************

    def test_save_user(self):
        '''
        Test to see if users are saved in the user_list
        '''
        self.new_user.save_user() #saving new user
        self.assertEqual(len(User.user_list) , 1)

if __name__ == '__main__':
    unittest.main()