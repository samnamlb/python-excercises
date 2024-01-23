import webbrowser
import os
def loginusername():
    username = input('Enter username: ')
    return username
def loginpass():
    password = input('Enter password: ')
    return password

while True:
    token = 0

    username = loginusername()
    with open('username.txt', 'r') as userdata:
        data_username = userdata.read()
        if username in data_username:
            token += 1

    password = loginpass()
    with open('password.txt', 'r') as passwordata:
        data_password = passwordata.read()
        if password in data_password:
            token += 1

    if token == 2:
        mainpage = 'file:///'+os.getcwd()+'/' + 'index.html'
        webbrowser.open_new_tab(mainpage)
        print('Logged in')
        break
    else:
        print('Failed to login')
        continue
