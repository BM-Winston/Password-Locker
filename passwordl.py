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

        Use.user_list.remove(self)


class Credenitals:
    """
    This class defines properties of the credentials objects
    """
    cred_list = []

    def __init__(self, acc_name, acc_password):

        self.acc_name = acc_name
        self.acc_password = acc_password


    def save-cred(self):
        """
        this saves credentials into cred_list
        """

        Credenitals.cred_list.save(self)

    






    