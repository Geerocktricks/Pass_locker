#!/usr/bin/env python3.6
import getpass
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

def check_existing_users(first_name , last_name):
    '''
    function to check user exists
    '''
    return User.user_exist(first_name , last_name)


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

def main():
    
    print('                                                            HELLO , WELCOME TO PASS-LOCKER!. ')
    print('                                                            =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=')
    print('\n')
    print('                              This app will have access to your passwords. Would you like to proceed? [y = yes/n = no]')
    print('***************************                                                                                                          *************************************')
    first_choice = input().lower()
    valid = { "y": True,
             "n": False}
    print('                                  *                                                                                          *')
    print('                                  *                                                                                          *')
    print('                                  *                                                                                          *')
    print('                                  *                                                                                          *')
    if first_choice == 'y':
        print('                                                                     [1 = Agree].Sign-up')
        log_sign = input()
        # valid = {
        #     1:True,
        #     2.False
        # }
        if log_sign == '1':
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
            print('                                  *                                                                                          *')
            print('                                  *                                                                                          *')
            print('                                  *                                                                                          *')
            print('                                  *                                                                                          *')
            print('                                  *      password.......                                                                     *')
            pswd_a = getpass.getpass('Password:')
            print('                                         Confirm password......                                                              *')
            pswd_b = getpass.getpass('Password:')
            save_users(create_user(f_name,l_name)) #Create and save new user
            # print ('\n')
            print('                                  *                                                                                          *')
            print('                                  *                                                                                          *')
            print('                                  *                                                                                          *')
            print('                                  *                                                                                          *')
            if pswd_a == pswd_b:
                print(f"                                        New user {f_name} {l_name} created")
            else:
                print('                                         Passwords don\'t match                                                          *')
            print('                                  *                                                                                          *')
            print('                                  *                                                                                          *')
            print('                                  *                                                                                          *')
            print('                                  *                                                                                          *')
            print(f'                                                                          LOGIN                                              *')
            print('                                                                         *=========*')
            print('                                  *         Enter your first name to log in.......                                           *')
            name = input().lower()
            print('                                  *                                                                                          *')
            print('                                  *                                                                                          *')
            print('                                  *                                                                                          *')
            print('                                  *                                                                                          *')
            print('                                             Enter your password..........')
            pswd_c = getpass.getpass('Password:')
            if pswd_c == pswd_a and f_name == name:
                print(f'                                        Logged in as {f_name}')
            else:
                print('                                         user name or password incorrect')
                print('                                  *                                                                                          *')
                print('                                  *                                                                                          *')
                print('                                  *                                                                                          *')
                print('                                  *                                                                                          *')
            print('                                  *                                                                                          *')
            print('                                  *                                                                                          *')
            print('                                  *                                                                                          *')
            print('                                  *                                                                                          *')
            print('                                            [1 =] View existing acconts                             [2 =] Add new account        ')
            acnt = input()
            if acnt == '2':
                print('                                         Account name ..............')
                acnt_name = input()
                print('                                          Password..........')
                acnt_passA = getpass.getpass('Password:')
                print('                                         Confirm password.........')
                acnt_passB = getpass.getpass('Password:')
                if acnt_passA == acnt_passB:
                    print(f'                                       New {acnt_name} account created!')
                    print('                                      [a=] Display Existing accounts                        [b=] Exit')

        #     print('\n')
        #     print('                                  *                                                                                           *')
        #     print('                                  *                                                                                           *')
        #     print('                                  *                                                                                           *')
        #     print('                                  *                                                                                           *')
        #     print('                                                                              LOGIN')
        #     print('                                                                             *======*')
        #     print ('\n')
        #     print('                                  *                                                                                           *')
        #     print('                                  *                                                                                           *')
        #     # print('                                  *')
        #     # print('                                  *')
        #     print('                                         First name ....')
        #     f_name = input().lower()
        #     print("                                         Last name .....")
        #     l_name = input().lower()
        #     print('                                  *                                                                                           *')
        #     print('                                  *                                                                                           *')
        #     if create_user(f_name,l_name):
        #         print(f'                                         Logged in as {f_name} {l_name} ')
        #         print('\n')
        #         print('                                         View existing user accounts [y/n]')
        #         exist_account = input()
        #         valid = { "y": True,
        #                 "n": False}
        #         if exist_account == 'y':
        #             print('Available')
        # elif log_sign == '1':
        #     print('                                  *                                                                                          *')
        #     print('                                  *                                                                                          *')
        #     print('                                  *                                                                                          *')
        #     print('                                  *                                                                                          *')
        #     # print('                                         First name ....')
        #     # f_name = input().lower()
        #     # print('                                  *                                                                                          *')
        #     # print('                                  *                                                                                          *')
        #     # print('                                  *                                                                                          *')
        #     # print('                                  *                                                                                          *')
        #     # print("                                         Last name .....")
        #     # last_name = input().lower()
        #     # if last_name == 'muchuki':
        #     #     print(f"                                         You are logged in as {f_name} {last_name}") 
    elif first_choice == 'n':
        print('                                                                         Bye')
    
    # elif first_choice == 'q':

    else:
        print('                                         Invalid choice, Choose between (y = yes) and (n = no)')
    print('                                  *                                                                                           *')
    print('                                  *                                                                                           *')
    print('                                  *                                                                                           *')
    print('                                  *                                                                                           *')
    

if __name__ == '__main__':

    main()
                            