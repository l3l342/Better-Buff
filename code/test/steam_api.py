from bs4 import BeautifulSoup
from datetime import date
from utils.csgo import CSGOItem
import requests, json
loop = True

while (loop):
    print('――――――――――――――――――――――――――――――――――――――――――')
    print('>>> Select an action')
    print('――――――――――――――――――――――――――――――――――――――――――')
    print('')
    print(' 0) Exit program')
    print(' 1) Search item')
    print('')
    action = input('Action: ')
    if action == '0':
        loop = False
        continue
    elif action == '1':
        name = input('Enter item: ')
        item = CSGOItem(name)
        print(item)
        print('')
    elif action == '2':
        continue
    elif action == '3':
        continue
    input('ENTER to continue')
