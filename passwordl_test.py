import unittest
from passwordl import User, Credentials


class TestUser(unittest.TestCase):
    """
    create a subclass that defines test cases
    """


    def setup(self):
        """
        first test
        """
        self new_user = User("Winston, abcdefgh")


    def test_init():
        """
        test to check if object is initialized correctly
        """

        self.asserEqual(self.new_user.username, "Winston")
        self.asserEqual(sel.new_user.password,"abcdefgh")


    def test_save_user(self):
        """
        test_save_user test case to test if the user object is saved into
         the user_list
        """
        self.new_user.save_user
        self.asserEqual(len(User.user_list)1)


    def tearDown(self):
        """
        method that cleans after each test is run
        """
        User.user_list = []


class TestCredentials(unittest.TestCase)


    


    

    


    


