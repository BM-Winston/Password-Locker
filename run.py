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


def shows_user():
    """
    This function displays users
    """
    return User.show_users()


def check_user(username, password):
    """
    Check if user is in the user list
    """
    check_user = Credentials.check_user(username, password)
    return User.check_user()

def create_account( acc_name,acc_username, acc_password ):
    """
    function that creates new account
    """
    new_account = Credentials( acc_name,acc_username, acc_password)
    return new_account
def save_account(account):
    """
    saves new account
    """
    account.save_account()

def delete_account(account):
    """
    Function to delete account
    """
    account.delete_account()

def existing_account(name):
    """
    function that returns a boolean if the account exists or not

    """
    return Credentials.find_by_account(name)

def find_account(acc_name):
    """
    finds account by account name
    """
    return Credentials.find_by_account(acc_name)

def display_accounts():
    """
    displays the account list
    """
    return Credentials.display_accounts()



    
def generate_password():
    """
    Function to enable password generation
    """
    generate_password = Credentials.generatePassword()
    return generate_password


def display_accounts():
    """
    Returns account list
    """
    return Credentials.display_accounts()






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
    # print('')
    print('Hello. Welcome to password locker! Enter username.')
    username = input()
    print(f"Hello {username}. " )
    while True:
        
        
        print("\n")
        print("What would you like to do? \ ca = create account,fa = find account, del =  delete, e = exit ,  ")

        short_code = input().lower()


        if short_code == 'ca':
            print ("New Account")
            print("-"*10)


            print("First name ...")
            acc_name = input()

            

            print("username ...")
            acc_username = input()

            print("Password ...")
            acc_password = input()

            print("New Account Created" )


            save_account(create_account( acc_name,acc_username, acc_password))
            print("New Account Updated")
            print('\n')



        # elif short_code == 'dc':
        #         if display_credentials() == None:
        #             print("This account does not exist")
        #             print('\n')

                   

        #         else:
        #             print("Find a list of credentials")
        #             print('\n')

        #             for user in display_credentials():
        #                 print(f"{user.firstname}{user.lastname}{user.username}")
        #                 print('\n')                               


        elif short_code == 'fa':
            while True:


                if display_accounts():
                    for account in display_accounts():
                        print(f"ACCOUNT NAME:{account.acc_name}")
                        print(f"PASSWORD:{account.acc_password}")

                else:

                    print("No accounts created")

                print("Go back to main menu y")
                option= input().lower()

                if option == "y":
                    break

                else:
                    print("Enter a valid option")




                    
            # if existing_account(option):
            #     print("Key In the username")
            #     option = input()
            # else:
            #     # search_account = find_account(option)
            #     print(f"{existing_account.acc_name} {existing_account.acc_username} {existing_account.acc_password}")
            #     print('-' * 20)        


        elif short_code == 'del':
            print("searchaccount by name")
            option1 = input()
            if existing_account(option1):
                searchaccount = find_account(option1)
                print("Account found")
                print(f"Account name: {searchaccount.acc_name}")
                print("Are you sure you want to delete this account y/n")
                option2 =input()
                if option2 == 'y':
                    delete_account(searchaccount)

                elif option2 == 'n':
                    continue
                else:
                    print("y/n")

            else:
                print("That account does not exist")

            # print("Enter the username of the account you want to delete")
            # option = input()
            # if existing_account(option):
                
            #     print(f"{option} e")
            #     print('\n')
            # else:
            #     print("Account  unavailable")
            #     print('\n')

        elif short_code == 'dc':
            print(' ')
            if display_credentials():
                print('Here is a list of all your credentials')
                print(' ')
                for credential in display_credentials():
                    print(f' Account Name: {credential.acc_name}, Username {credential.username} , Password: {credential.password}')
                print(' ')	
            else:
                print(' ')
                print("No credentials saved yet")
                print(' ')

        elif short_code == 'e':
            print("Thanks for using Password-Locker.Nice time .......")
            break

        else:
            print("Try short codes!")
                


        


                        
            





if __name__ == '__main__':
    main()




