from passwordl import User, Credentials



def create_user(firstname, lastname, username, password):
    """
    this function creates new user
    """
    new_user = User(firstname, lastname, username, password)
    return new_user

def save_user(user):
    """
    Saves user
    """
    user.save_user()

def delete_user(user):
    """
    removes user
    """
    user.remove_user()


def displays_user():
    """
    This function displays users
    """
    User.show_user()


def check_user(username, password):
    """
    Check if user is in the user list
    """
    check_user = Credentials.check_user(username, password)
    return check_user

    
def generate_password():
    """
    Function to enable password generation
    """
    generate_password = Credentials.generatePassword()
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



def main():
    print('')
    print('Hello. Welcome to password locker! Enter username.')
    username = input()
    print(f"Hello {username}. " )
    while True:
        
        
        print("\n")
        print("What would you like to do? \nnu = New User, du = Display User, ")

        short_code = input().lower()


        if short_code == 'nu':
            print ("New User")
            print("-"*10)


            print("First name ...")
            firstname = input()

            print("lastname ...")
            lastname = input()

            print("username ...")
            username = input()

            print("Password ...")
            password = input()


            save_user(create_user(firstname, lastname, username, password))
            print('\n')



        elif short_code == 'du':
                if displays_user() == None:
                    print("This account does not exist")
                    print('\n')

                   

                else:
                    print("Find a list of users")
                    print('\n')

                    for user in displays_user():
                        print(f"{user.firstname}{user.lastname}{user.username}")
                        print('\n')


                           


        elif short_code == '':
                print("Nice time")

                        
            





if __name__ == '__main__':
    main()




