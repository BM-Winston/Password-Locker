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

        Useruser_list.remove(self)


    @classmethod
    def displays_users(cls):
        """
        method that displays users_list
        """
        return user_list


    @classmethod
    def check_user(cls, username):
        """
        method that checks if user is in user_list
        """

        for user in cls.user_list:
            if user.username == number:
                return user





class Credenitals:
    """
    This class defines properties of the credentials objects
    """
    cred_list = []

    def __init__(self, acc_name, acc_password):

        self.acc_name = acc_name
        self.acc_password = acc_password


    def save_acc(self):
        """
        this saves credentials into cred_list
        """

        Credenitals.cred_list.save(self)

    def delete_acc(self):
        """
        deletes credentials in the cred_list
        """

        Credenitals.cred_list.remove(self)

    @classmethod
    def display_credentials(cls):
        """
        method that returns the cred_list
        """
        return credentials.cred_list


    @classmethod
    def check_credentials(cls):
        """
        method that takes in an acc_name and return name match in acc_name
        """
        for credentials in cred_list:
            if credentials.acc_name == acc_name:
                return credentials


   


    






    