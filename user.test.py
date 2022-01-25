import unittest
import pyperclip #Importing the unittest module
from user import User #Importing the user class

class TestUser(unittest.TestCase) :
 
 
    '''
     Test class that defines test cases for the user class behaviours.
      
     Args:
           unittest.TestCase:TestCase class that helps in creating the test cases
    '''     



    def setUp(self):
        '''
        set up method to run before each test cases
        '''
        self.new_user = User("Kalondu","boss","0724655025","kalondu@b.com","222")# add user object

    def tearDown(self):

        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.fst_name,"Kalondu")
        self.assertEqual(self.new_user.lst_name,"boss")
        self.assertEqual(self.new_user.phone_number,"0724655025")
        self.assertEqual(self.new_user.eml,"kalondu@b.com")
        self.assertEqual(self.new_user.password,"222")

#.
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user user_list
        '''
        self.new_user.save_user()#saving the new user
        self.assertEqual(len(User.user_list),1)

     #another test case
    def test_save_multiple_user(self):

        '''
        test_save_multiple_user to check if we can save multiple user ojects to our user_list
        '''

        self.new_user.save_user()
        test_user=User("Test","user","0724655025","test@user.com","222")# new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)


    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user user_list
        '''
        self.new_user.save_user()
        test_user = User("Test","user","0740462323","test@user.com","222")#new user
        test_user.save_user()


        self.assertEqual(len(User.user_list),2)


    def test_find_user_by_number(self):
        '''
        test to check if we can find a user by phone number and display information
        '''

        self.new_user.save_user()
        test_user = User("Test","user","0740462323","test@user.com","222")#new user
        test_user.save_user()

        find_user = User.find_by_number("0740462323")


        self.assertEqual(find_user.eml,test_user.eml)


    def test_user_exists(self):
        '''
        test to check if we can return a Boolean if we cannot find the user. 
        '''

        self.new_user.save_user()
        test_user = User("Test","user","0740462323","test@user.com","222")# new user
        test_user.save_user()

        user_exist = User.user_exist("0740462323")

        self.assertTrue(user_exist)


    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_users(),User.user_list)

if __name__=='__main__':
     unittest.main()

