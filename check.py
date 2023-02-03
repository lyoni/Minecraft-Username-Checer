import requests

def prRed(prt):
    print(f"\033[91m{prt}\033[00m")

def prGreen(prt):
    print(f"\033[92m{prt}\033[00m")

def check_username(username):
    response = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{username}')
    if response.status_code == 200:
        prRed(f'Username {username} is unavailable')
    if response.status_code == 404:
        prGreen(f'Username {username} is available')

with open('names.txt', 'r') as file:
    for username in file:
        username = username.strip()
        check_username(username)
