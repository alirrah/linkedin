import json
import os


def login_signinPage(users):

    os.system('cls')
    print(' -----------------------------LinkedIn----------------------------- ')
    number = int(
        input('Menu :\n(1) Sign in\n(2) Login\n(3) Quit\nEnter a number : '))
    return number


def sign_in(users):

    os.system('cls')
    print(' -----------------------------Sign in----------------------------- ')
    name = input('Name : ')
    password = input('password : ')

    for user in users:
        if user['name'] == name and user['password'] == password:
            print('You have signed in successfully')
            os.system('pause')
            return user
    return None


def login(users):

    os.system('cls')
    print(' -----------------------------Login----------------------------- ')
    name = input('Name : ')
    password = input('password : ')
    date = input('Date of Birth : (Hint : yyyy/mm/dd) ')
    university = input('University : ')
    field = input('Field : ')
    workplace = input('Workplace : ')
    specialties = list(
        input('Specialties : (Hint : spread them by space) ').split(' '))

    users.append({'id': str(int(users[-1]['id']) + 1), 'name': name, 'password': password, 'dateOfBirth': date,
                 'universityLocation': university, 'field': field, 'workplace': workplace, 'specialties': specialties, 'connectionId': []})
    print('Information successfully recorded')
    os.system('pause')
    return users[-1]


def userPage(users, user):

    while True:

        os.system('cls')
        print(' -----------------------------User Page----------------------------- ')
        print('Profile : \n\tName : ', user['name'], '\n\tDate of Birth : ', user['dateOfBirth'], '\n\tUniversity : ', user['universityLocation'],
              '\n\tField : ', user['field'], '\n\tWorkplace : ', user['workplace'], '\n\tSpecialties : ', user['specialties'])
        number = int(input(
            '\nMenu : \n(1) Edit Profile\n(2) Followers\n(3) Suggested List for follow\n(4) Quit\nEnter a number : '))

        if number == 1:
            EditProfile(user)
        elif number == 2:
            Follower(user)
        elif number == 3:
            findSuggestion(users, user)
        elif number == 4:
            with open('users.json', 'w') as outfile:
                json.dump(users, outfile)
            outfile.close()
            exit(0)
        else:
            print('Error!!!', 'Invalid input', sep='\n')
            os.system('pause')


def findSuggestion(users, user):

    suggested = {}
    priority = [0, 0, 0, 0, 0]
    os.system('cls')
    print(' -----------------------------Suggested for  Follow----------------------------- ')
    print('Give each item a score between 0 to 5 in order of priority : ')
    priority[0] = int(input('Date of Birth : '))
    priority[1] = int(input('University : '))
    priority[2] = int(input('Field : '))
    priority[3] = int(input('Workplace : '))
    priority[4] = int(input('Specialties : '))
    for item in users:
        item['visited'] = False
        item['level'] = 0
    subChild(users, suggested, user, priority)
    for item in users:
        item.pop('visited')
        item.pop('level')
    for List in suggested.values():
        for item in List:
            print('\nName : ', item['name'], '\nDate of Birth : ', item['dateOfBirth'], '\nUniversity : ',
                  item['universityLocation'],
                  '\nField : ', item['field'], '\nWorkplace : ', item['workplace'], '\nSpecialties : ',
                  item['specialties'], end='\n\n')
    while True:
        do = input('Do you want to follow someone ? (Y/N) ')
        if do == 'Y':
            flage = True
            name = input('Enter his/her name : ')
            for List in suggested.values():
                for item in List:
                    if item['name'] == name:
                        users[int(user['id']) -
                              1]['connectionId'].append(item['id'])
                        print('Successfully added to your followers')
                        flage = False
            if flage:
                print(
                    'Error!!!', 'No user was found with this information.', sep='\n')
                os.system('pause')
        elif do == 'N':
            break
        else:
            print('Error!!!', 'Invalid input', sep='\n')
            os.system('pause')


def subChild(users, suggested, user, priority):
    l = []
    users[int(user['id']) - 1]['visited'] = True
    users[int(user['id']) - 1]['level'] = 0
    l.append(user)
    while len(l) > 0:
        p = l.pop(0)
        for item in p['connectionId']:
            if not users[int(item) - 1]['visited']:
                users[int(item) - 1]['level'] = p['level'] + 1
                users[int(item) - 1]['visited'] = True
                l.append(users[int(item) - 1])
        if p['level'] >= 6:
            return
        if 1 < p['level'] < 6:
            userRate = rate(priority, user, p)
            if userRate == 0:
                continue
            state = suggested.get(userRate)
            if state:
                suggested[userRate].append(p)
            else:
                suggested[userRate] = [p]


def rate(priority, user, contact):

    sep = 0
    for item in user['specialties']:
        if item in contact['specialties']:
            sep += 1
    return priority[0] * (user['dateOfBirth'] == contact['dateOfBirth']) + priority[1] * (user['universityLocation'] == contact['universityLocation']) + priority[2] * (user['field'] == contact['field']) + priority[3] * (user['workplace'] == contact['workplace']) + priority[4] * sep


def EditProfile(user):

    os.system('cls')
    print(' -----------------------------Edit Profile----------------------------- ')
    name = input('Name : (Hint : (0) No Change) ')
    password = input('password : (Hint : (0) No Change) ')
    date = input('Date of Birth : (Hint : yyyy/mm/dd, (0) No Change) ')
    university = input('University : (Hint : (0) No Change) ')
    field = input('Field : (Hint : (0) No Change) ')
    workplace = input('Workplace : (Hint : (0) No Change) ')
    specialties = list(
        input('Specialties : (Hint : spread them by space, (0) No Change) ').split(' '))
    index = int(user['id']) - 1

    if name != '0':
        users[index]['name'] = name
    if password != '0':
        users[index]['password'] = password
    if date != '0':
        users[index]['dateOfBirth'] = date
    if university != '0':
        users[index]['universityLocation'] = university
    if field != '0':
        users[index]['field'] = field
    if workplace != '0':
        users[index]['workplace'] = workplace
    if specialties != ['0']:
        users[index]['specialties'] = specialties

    print('Profile updated successfully', sep='\n')
    os.system('pause')


def Follower(user):

    os.system('cls')
    print(' -----------------------------Followers----------------------------- ')
    for item in user['connectionId']:
        print(users[int(item) - 1]['name'])
    os.system('pause')


if __name__ == '__main__':

    # read from json file and save it in users
    file = open('users.json', 'r')
    users = json.load(file)
    file.close()

    while True:
        number = login_signinPage(users)

        if number == 1:
            user = sign_in(users)
            if user is None:
                print(
                    'Error!!!', 'No user was found with this information. Please Login.', sep='\n')
                os.system('pause')
            else:
                userPage(users, user)
        elif number == 2:
            user = login(users)
            userPage(users, user)
        elif number == 3:
            break
        else:
            print('Error!!!', 'Invalid input', sep='\n')
            os.system('pause')
