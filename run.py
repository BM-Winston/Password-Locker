from user import User
from credentials import Credenitals

def create_user(firstname, lastname, username, password):
    """
    this function creates new user
    """
    new_user = User(firstname, lastname, username, password)
    return new_user

def save_user(self):
    """
    Saves user
    """
    user.save_user()

def delete_user(self):
    """
    removes user
    """
    user.remove_user()


def displays_user():
    """
    This function displays users
    """
    return User.displays_user()


def check_user(username, password):
    """
    Check if user is in the user list
    """
    check_user = Credenitals.check_user(username, password)
    return check_user

    
def generate_password():
    """
    Function to enable password generation
    """
    generate_password = Credenitals.generatePassword()
    return generate_password






def create_new_credentials(acc_name,acc_password):
    '''
	Function to create a new credential
	'''
    new_credentials = Credentials(acc_name,acc_password)
    return new_credentials

def save_credentials(credentials):
    """
    Function to save Credentials to the cred_list
    """
    credentials.save_credentials()

def find_credentials(acc_name):
    return Credentials.find_credentials(acc_name)

def check_existing_credentials(acc_name):
    return Credentials.credentials_exist(acc_name)


def delete_credentials(credentials):
    """
    Function to delete a Credentials from cred_list
    """
    credentials.delete_credentials()

def display_credentials():  
    """
    Displays all the saved credentials.
    """
    return Credentials.display_credentials()








