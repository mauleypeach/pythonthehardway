#!/bin/python
user = {'admin': True, 'active': False, 'name': 'Mauli'}
print(user['admin'])
if user['admin'] == True and user['active'] == False:
    print('ADMIN',  user['name'])

if user['active'] == True and user['admin'] == False:
        print ('ACTIVE', user['name'])

if user['admin'] == True and user['active'] == True :
    print ('ACTIVE - ADMIN', user['name'])
