from os import system
import random
user = {
    'username'  :   'johny777',
    'online'    :   'true',
    'e-mail'    :   'johny777@lucky.me',
    'rating'    :   10000,
    'friends'   :   [
        'marry888',
        'candy001',
        'peter99'
    ]
}
random_integer = random.randint(10, 100000000000)
user['rating']=random_integer
user['rm'] =''
if user['rating']>1000 and user['rating']<1000000:
    user['rating']= round(float(user['rating']/1000),2)
    user['rm'] = 'k likes'
if user['rating']>1000000 and user['rating']<1000000000:
    user['rating']= round(float(user['rating']/1000000),2)
    user['rm'] = 'm likes'
if user['rating']>1000000000 and user['rating']<1000000000000:
    user['rating']= round(float(user['rating']/1000000000),2)
    user['rm'] = 't likes'
option=-1
#HW1- add friends
while option!=0:
    system('cls')
    print('That  is our user Data:\n\n')
    #print user data
    print("login:  ", user['username'])
    print("e-mail: ",user['e-mail'])
    print("rating: ",user['rating'],user['rm'])
    print('\nFRIENDS LIST: \n')
    for i in range(len(user['friends'])):
        print('>>', user['friends'][i])
    print('\nIntroduce new friends  or hit enter to exit\n')
    new_fr = input('introduce some friends: \n>>  ')
    user['friends'].append(new_fr)
    if new_fr=='':
        option=0



