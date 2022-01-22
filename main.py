import json
import os

def login_signinPage():

    os.system('cls')
    print(' -----------------------------LinkedIn----------------------------- ')
    number = int(input('Menu :\n(1) Sign in\n(2) Login\nEnter a number : '))

    if number == 1:
        return sign_in()
    elif number == 2:
        return login()
    else:
        print('Error!!!', 'Invalid input', sep='\n')
        return login_signinPage()

def sign_in():

    os.system('cls')
    print(' -----------------------------Sign in----------------------------- ')
    name = input('Name : ')
    password = input('password : ')

    for user in users:
        if user['name'] == name and user['password'] == password:
            return userPage()
    print('Error!!!', 'No user was found with this information. Please Login.', sep='\n')
    return login_signinPage()

def login():

    os.system('cls')
    print(' -----------------------------Login----------------------------- ')
    name = input('Name : ')
    password = input('password : ')
    date = input('Date of Birth : (Hint : yyyy/mm/dd)')
    university = input('University : ')
    field = input('Field : ')
    workplace = input('Workplace : ')
    specialties = list(input('Specialties : (Hint : spread them by space)').split(' '))

    users.append({'id':str(int(users[-1]['id']) + 1), 'name': name, 'password': password,'dateOfBirth': date, 'universityLocation': university, 'field': field, 'workplace': workplace, 'specialties': specialties, 'connectionId': []})

    userPage()

def userPage():
    return 0

def findSuggestion():
    return 0


if __name__ == '__main__':

    # read from json file and save it in users
    file = open('users.json')
    users = json.load(file)
    file.close()

    login_signinPage()





