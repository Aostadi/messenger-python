import datetime
import register
import login

date = datetime.datetime.now()
print(f'\t\t\t{"*"*7}-- WELCOME TO MESSENGER --{"*"*7}')
hour = date.hour
if 5 <= hour <= 12:
    print('good morning!')
elif 13 <= hour <= 18:
    print('good afternoon!')
elif 19 <= hour <= 4:
    print('good night!')

while True:
    menu = input("""
    1.register
    2.login
    3.exit
    Please enter menu number : """)
    if menu == '1':
        register.register()
    elif menu == '2':
        login.login()
    else:
        exit()