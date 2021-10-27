# user Mason Levely
# date: 10/11/2012
# Program: ATM Bank Transaction

'''
This program simulates an ATM Utilizing  If. Elif, & Else statements
Nesting If statements and refresh our comparison & Logical Operators
'''

print("Welcome to Cash-R-Us Bank\nLet's take a moment to set up your account. \n")

# Set up account by asking users for their first & last names using Variables
first_name = input("What is your first name: ")
last_name = input("What is your last name: ")

print("\nWelcome to Cash-R-Us",first_name,last_name + ", we will now set up a security pin on your account.\n")

# set up a PIN - Personal Identification Number
pin = input("please chose a 4 digit Personal Identification Number: ")

print("\nThank you",first_name + ", We see that you set your PIN to",pin)

print("\nWould you like to make a transaction through our Automated Teller Machine")
atm = input("Yes or No: ").lower()

if atm == "yes":
    print("\n**********************************************\n")

    # This part of the program will be asking users to complete a transaction through the atm
    print("Please insert your ATM card\n")
    print("Welcome to Cash-R-Us ATM",first_name,last_name,"\n")
    userPIN = input("What is your four digit PIN: ")

    if pin == userPIN:
        balance = 674
        print("\nYour balance: $" + str(balance))



    else:
        print("Sorry",first_name,last_name,"your PIN doesn't match our records")




else:
    print("\nHave a wonderful day",first_name,last_name + ", please come back and visit soon.")