
import random
import string
import pyperclip
from sqlalchemy import false

class User:
    """
    class user generates new instances for the details of the user
    """
    user_list = []


    def __init__(self, firstname, lastname, username, password):
        """
        This defines properties to be included for the user
        """

        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password

    
    def save_user(self):
        """
        this method saves users objects into the user_list
        """

        User.user_list.append(self)

    def delete_user(self):
        """
        removes users from the user_list
        """

        User.user_list.remove(self)


    @classmethod
    def show_users(cls):
        """
        method that displays users_list
        """
        return cls.user_list


    @classmethod
    def check_user(cls, username):
        """
        method that checks if user is in user_list
        """

        for user in cls.user_list:
            if user.username == username:
                return user

    
    @classmethod
    def user_exist(cls, username):
        """
        Checks if user exists in user_list
        """

        for user in cls.user_list:
            if user.username == username:
                return True
            
            else:
                return False




                return false





class Credentials:
    """
    This class defines properties of the credentials objects
    """
    cred_list = []

    def __init__(self, acc_name,acc_username, acc_password):

        self.acc_name = acc_name
        self.acc_password = acc_password
        self.acc_username= acc_username

    
    def save_account(self):
        """
        this saves credentials into cred_list
        """

        Credentials.cred_list.append(self)



    def delete_account(self):
        """
        deletes credentials in the cred_list
        """

        Credentials.cred_list.remove(self)        
    
    
    
    def display_credentials(self):

        """
        this displays credentials

        """
        return Credentials.cred_list


    def create_new_credentials(self):
        """
        Creates new account credentials
        """
        return 


    

    
    @classmethod
    def existing_account(cls, name):
        """
        checks if the account exists in cred_list

        """

        for account in cls.cred_list:
            if account.acc_name == name:
                return True
            else:
                return False

    
    @classmethod
    def find_by_account(cls,acc_name):
        """
        method that matches name with the account name
        """

        for account in cls.cred_list:
            if account.acc_name == acc_name:
                return account

    @classmethod
    def display_accounts(cls):

        """
        method that shows the list of accounts available
        """

        for account in cls.cred_list:
            return cls.cred_list



    @classmethod
    def display_credentials(cls):
        """
        method that returns the cred_list
        """
        return cls.cred_list


    @classmethod
    def check_credentials(cls, acc_name):
        """
        method that takes in an acc_name and return name match in acc_name
        """
        for credentials in cls.cred_list:
            if credentials.acc_name == acc_name:
                return credentials


     
    def generate_password(ln):
        '''
        generate random password for strings, numbers and integers
        '''
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890=?!#/@~$*"
        password = " "
        for i in range(ln):
            password += chars[random.randint(0, len(chars) - 1)]
        return password



   


    






    