#!/usr/bin/env python3.6
# import getpass
from user import User

def create_user(first_name , last_name):
    '''
    Function to create new user
    '''
    new_user = User(first_name , last_name)
    return new_user

def save_users(user):
    '''
    function to save user
    '''
    user.save_user()
print("\n")
print("                                  ██████╗  █████╗ ███████╗███████╗    ██╗      ██████╗  ██████╗██╗  ██╗███████╗██████╗ ")
print("                                  ██╔══██╗██╔══██╗██╔════╝██╔════╝    ██║     ██╔═══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗")
print("                                  ██████╔╝███████║███████╗███████╗    ██║     ██║   ██║██║     █████╔╝ █████╗  ██████╔╝")
print("                                  ██╔═══╝ ██╔══██║╚════██║╚════██║    ██║     ██║   ██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗")
print("                                  ██║     ██║  ██║███████║███████║    ███████╗╚██████╔╝╚██████╗██║  ██╗███████╗██║  ██║")
print("                                  ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝    ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝")
print("                                 =====================================================================================\n")                                                                
print("                                     ╦ ╦┌─┐┬  ┌─┐┌─┐┌┬┐┌─┐  ┌┬┐┌─┐  ╔═╗┌─┐┌─┐  ┌─┐┌─┐┌─┐┌─┐  ┬  ┌─┐┌─┐┬┌─┌─┐┬─┐┬┬")
print("                                     ║║║├┤ │  │  │ ││││├┤    │ │ │  ║ ╦├┤ ├┤───├─┘├─┤└─┐└─┐  │  │ ││  ├┴┐├┤ ├┬┘││")
print("                                     ╚╩╝└─┘┴─┘└─┘└─┘┴ ┴└─┘   ┴ └─┘  ╚═╝└─┘└─┘  ┴  ┴ ┴└─┘└─┘  ┴─┘└─┘└─┘┴ ┴└─┘┴└─oo\n")
print("         _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+__+__+_+_+_+_+_+_+ ") 
print('\n')                                  
# pswd = getpass.getpass('Password:')
def main():
    
    print('                                                            HELLO , WELCOME TO PASS-LOCKER!. ')
    print('                                                            =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=')
    print('\n')
    print('                                         This app will have access to your passwords. Would you like to proceed? [y/n]')
    print('***********************************                                                                                          ********************************************')
    first_choice = input().lower()
    valid = { "y": True,
             "n": False}
    print('                                  *                                                                                          *')
    print('                                  *                                                                                          *')
    print('                                  *                                                                                          *')
    print('                                  *                                                                                          *')
    if first_choice == 'y':
        print('                                         [1].Login                            [2].Sign-up')
        log_sign = input()
        # valid = {
        #     1:True,
        #     2.False
        # }
        if log_sign == '2':
            print('                                  *                                                                                          *')
            print('                                  *                                                                                          *')
            print('                                  *                                                                                          *')
            print('                                  *                                                                                          *')
            print('                                         First name ....')
            f_name = input().lower()
            print('                                  *                                                                                          *')
            print('                                  *                                                                                          *')
            print('                                  *                                                                                          *')
            print('                                  *                                                                                          *')
            print("                                         Last name .....")
            l_name = input().lower()

            save_users(create_user(f_name,l_name)) #Create and save new user
            # print ('\n')
            print('                                  *                                                                                          *')
            print('                                  *                                                                                          *')
            print('                                  *                                                                                          *')
            print('                                  *                                                                                          *')
            print(f"                                        New user {f_name} {l_name} created")
            print('\n')
            print('                                  *                                                                                           *')
            print('                                  *                                                                                           *')
            print('                                  *                                                                                           *')
            print('                                  *                                                                                           *')
            print('                                                                              LOGIN')
            print('                                                                             *======*')
            print ('\n')
            print('                                  *                                                                                           *')
            print('                                  *                                                                                           *')
            # print('                                  *')
            # print('                                  *')
            print('                                         First name ....')
            f_name = input().lower()
            print("                                         Last name .....")
            l_name = input().lower()
            print('                                  *                                                                                           *')
            print('                                  *                                                                                           *')
            print(f'                                         Logged in as {f_name} {l_name} ')
    elif first_choice == 'n':
        print('                                                                         Bye')
    else:
        print('                                         Invalid choice, Choose between (y = yes) and (n = no)')
    print('                                  *                                                                                           *')
    print('                                  *                                                                                           *')
    print('                                  *                                                                                           *')
    print('                                  *                                                                                           *')
    

if __name__ == '__main__':

    main()
                            