
import random
import string
import pyperclip

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





class Credentials:
    """
    This class defines properties of the credentials objects
    """
    cred_list = []

    def __init__(self, acc_name, acc_password):

        self.acc_name = acc_name
        self.acc_password = acc_password


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


    def save_acc(self):
        """
        this saves credentials into cred_list
        """

        Credentials.cred_list.save(self)

    def delete_acc(self):
        """
        deletes credentials in the cred_list
        """

        Credentials.cred_list.remove(self)

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



   


    






    