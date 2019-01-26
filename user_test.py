import unittest
from user import User

#*******************************Test user class begins here*************************************************

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

    def tearDown(self):
        '''tear down method to clean up after every test
        '''
        User.user_list = [] #Returns an empty user list after every test
    

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

    #*********************************Save multiple users test**************************************************

    def test_save_multiple_users(self):
        '''
        Test to see if multiple users can be saved
        '''
        self.new_user.save_user()
        dummy_user = User('Trevor' , 'Jayson') #new dummy user
        dummy_user.save_user()
        self.assertEqual(len(User.user_list) , 2)


    #**********************************Delete user test************************************************************

    def test_delete_user(self):
        '''
        Test to see if we can delete a user from user list
        '''
        self.new_user.save_user()
        dummy_user = User('Trevor' , 'Jayson')
        dummy_user.save_user()
        self.new_user.delete_user() #Deleting a user from the user list
        self.assertEqual(len(User.user_list) , 1)

    #************************************Display all users***********************************************************

    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''
        self.assertEqual(User.display_users() , User.user_list)
if __name__ == '__main__':
    unittest.main()

#*****************************************TetstCredentials class begins here*********************************************************

class TestCredentials(unittest.TestCase):
    '''
    testcase class to define the test case behaviour of the credentials class 

    Args:
        unittest.TestCredentials: TestCredentials class that helps in creating test cases
    '''
    #*********************************setUp method********************************************************

    def setUp(self):
        '''
        setUp test to run before each test case of the TestCredentials class
        '''
        self.new_credentials = credentials('Facebook' , 'Gerald12345')

    #**********************************tearDown method**************************************************

    def tearDown(self):
        '''tear down method to clean up after every test of the credentials class
        '''
        Credentials.credentials_list = [] #Returns an empty credentials list after every test



    #***********************************Create account (Credentials) test***************************

    # def test_init_credentials(self):
    #     '''
    #     Test to see if accounts are instanciated properties
    #     '''
    #     self.assertEqual(self.new_credentials.account_name , 'Instagram')
    #     self.assertEqual(self.new_user.password , 'Gerald12345')
