#!/usr/bin/env python3.6
from user import User




def create_user(fstname,lstname,phone,email,password):
    '''
    Function that creates a new user
    '''
    new_user = User(fstname,lstname,phone,email,password)
    return new_user


def save_users(user):
    '''
    Function that saves a user
    '''
    user.save_user()


def dlt_user(user):
    '''
    Function for deleting a user
    '''
    user.dlt_user()


def fnd_user(number):
    '''
    Function that finds a user by number and returns the registered user
    '''
    return User. find_by_number(number)


def review_existing_users(number):
    '''
    Function that checks if a user exists with the added number and return a Boolean
    '''
    return User.user_exist(number)


def display_users():
    '''
    Function that returns every saved users
    '''
    return User.display_users()


def main():
    print("Hello Welcome to your user list. What is your name?")
    user_name = input()
    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : 5 - create a new user, 4 - display users, 3 -find a user, 2 -exit the Password locker ")

        short_code = input().lower()

        if short_code == '5':
            print("New User")
            print("-"*10)

            print ("First name ....")
            fst_name = input()

            print("Last name ...")
            lst_name = input()

            print("Phone number ...")
            phn_number = input()

            print("Email address ...")
            eml_address = input()

            print("Password ...")
            password = input()

            print("confirm password ...")
            passworda = input()


            save_users(create_user(fst_name,lst_name,phn_number,eml_address,password)) # create and save new user.
            print ('\n')
            print(f"New User {fst_name} {lst_name} created")
            print ('\n')

        elif short_code == '4':

            if display_users():
                print("Hello again!Here is a list of all your users")
                print('\n')

                for user in display_users():
                    print(f"{user.fst_name} {user.lst_name} .....{user.phone_number}")

                    print('\n')
            else:
                    print('user does not exist\n')
 
        elif short_code == '3':

            print("Enter the number you want to search for")

            search_number = input()
            if review_existing_users(search_number):
                search_user = fnd_user(search_number)
                print(f"{search_user.fst_name} {search_user.lst_name}")
                print('-' * 30)

                print(f"Phone number.......{search_user.phone_number}")
                print(f"Email address.......{search_user.eml}")
            else:
                print("sorry! user does not exist")

        elif short_code == "2":
            print("arrivederci .......")
            break
        else:
            print("Error. Please use the short codes")


if __name__ == '__main__':

    main()