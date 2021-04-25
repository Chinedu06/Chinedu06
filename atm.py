# functionnalities
# "I should have register and login here"
# Welcome to V bank
#   Date & Time
# Do you have an account
# 1; YES 2. NO
# if YES Log In
#     For Log In:
#             Collect user name
#             Collect user account number
#              (validate account number)
#              Collect user password
#               (validate user password)
#               Validate user details
#                 Print:
#                     Welcome User
#                Return:
#                       Bank Operations

# If no Register
#      For registration:
#             collect user email address
#             collect Username,
#              Collect User password
#             Generate Account number
#             Log in user with generated account number
#               and password
#              (validate user password and account number)
#                 Print:
#                     Welcome User
#                   Return:
#                  Bank Operations 
#     Bank Operations
#           Deposit
#          Withdraw
#           Complaint
          
#      What is needed
#           Register




import random
import datetime

database = {
    4102793121: ['Okereke', 'Godswill', 'godswill@zuri.task', '1234']
}

def init():
    print('Welcome to V bank')

    now = datetime.datetime.now()
    print (now.strftime('%Y-%M-%d  %H:%M:%S'))

    
    have_account = int(input('Do you have an account with us? \n 1 (YES) 2 (NO) \n'))

    if (have_account == 1):

        login()
    elif (have_account == 2):

        print(register())
    else:
        print('Sorry, you have selected an invalid option')
        init()

def login():
    print('Welcome back \n Login ')

    account_number_from_user = input('Whats your account number? \n')
    is_valid_account_number = account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = input('Whats your password? \n')

        for accountNumber, UserDetails in database.items():
            if accountNumber == int(account_number_from_user):
                if (UserDetails[3] == password):
                    bankoperation(UserDetails)

        
    else:
        print('Invalid account number')
        login()

def register():
    print('Register')

    email = input('Whats is your email address? \n')
    first_name = input('What is your first name? \n')
    last_namr = input('What is your last name? \n')
    password = input('Create your password \n')

    accountNumber = generateaccountnumber()

    print('Your account has been created succesfully!!')
    print('Your account number is: %d' % accountNumber)
    print('Make sure you keep it safe')

    login()
    bankoperation(register)

def generateaccountnumber():
    return random.randrange(1111111111, 9999999999)


def account_number_validation(account_number):
    if account_number:

        if len(str(account_number)) == 10:

            try:
                int(account_number)
                return True
            except ValueError:
                print('Invalid account number, account number should be 10 digits')
                return False
            except TypeError:
                print('Invalid account type')
                return False
        
        else:
            print('Account number can not be more than 10 digits')
            return False
    
    else:
        print('Account number is a required field')
            
def bankoperation(user):
    print('Welcome %s %s' % (user[0], user[1]))

    SelectedOption = int(input('What would you like to do? 1 (Cash Deposit) 2 (Cash withdrawal) 3 (Complaint) 4 (Exit) \n '))

    if (SelectedOption == 1):
        DepositOperation(user)

    elif (SelectedOption == 2):
        WithdrawalOperation(user)

    elif (SelectedOption == 3):
        Complaint(user)

    elif (SelectedOption == 4):
        exit()

    else:

        print('Invalid option selected')
        bankoperation(user)

def DepositOperation(user):
    int(input('How much will you like to deposit? \n'))
    print('Deposit Succesfull\n')

def WithdrawalOperation(user):
    int(input('How much would you like to withdraw \n'))
    print('Withdrawal Succesfull \n Please take your cash')

def Complaint(user):
    (input('What issue will you like to report \n'))
    print('Thank you for contacting us')



def bankoperation(register):
    print('Welcome %s %s')

    SelectedOption = int(input('What would you like to do? 1 (Cash Deposit) 2 (Cash withdrawal) 3 (Complaint) 4 (Exit) \n '))

    if (SelectedOption == 1):
        DepositOperation(register)

    elif (SelectedOption == 2):
        WithdrawalOperation(register)

    elif (SelectedOption == 3):
        Complaint(register)

    elif (SelectedOption == 4):
        exit()

    else:

        print('Invalid option selected')
        bankoperation(register)

def DepositOperation(register):
    int(input('How much will you like to deposit? \n'))
    print('Deposit Succesfull\n')

def WithdrawalOperation(register):
    int(input('How much would you like to withdraw \n'))
    print('Withdrawal Succesfull \n Please take your cash')

def Complaint(register):
    (input('What issue will you like to report \n'))
    print('Thank you for contacting us')

init()