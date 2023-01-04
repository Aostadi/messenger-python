import class_file
import func


def messager(user):
    n = 0
    limit = 7
    while True:
        print(f'page : {n + 1}')
        print('last messages : \n')
        fetch_message(user=user,offset=(n*limit),limit=limit)
        menu = input('''\n************************************
        1.refresh page
        2.next page
        3.send message
        4.exit
        ****** please enter menu number : ''')
        if menu == '1' :
            n = 0
            continue
        elif menu == '2':
            n += 1
            continue
        elif menu == '3':
            send_message(user=user)
        else:
            exit()

        


def fetch_message(user, offset, limit):
    sql = class_file.Mysql(host='127.0.0.1', user='root')
    sql.set_db('messenger')
    sql.connect()
    sql.set_table('message')
    sql.select('sender','message','date_at')
    sql.where('reciever','=',user)
    sql.limit(limit=limit)
    sql.orderby('date_at DESC')
    sql.offset(offset=offset)
    messages = sql.fecth(2)
    sql.set_default()
    if messages != []:
        for i in messages:
            print('-'*15)
            print(f'FROM : {i[0]}')
            print(f'DATE : {i[2]}')
            print(f'MESSAGE : {i[1]}')
    else:
        print('no message to show')

def send_message(user):
    while True:
        sender = user
        reciever = input('please enter user name of the reciever : ')
        message = input(' Please enter your message : ')
        chioce = input('Do you want to continue (Y/N): ').upper()
        if chioce != 'Y':
            continue
        result = func.check_user(email=None, user=reciever,want_sth=0)
        if result == 0:
            print('user name not found')
            continue
        sql = class_file.Mysql(host='127.0.0.1', user='root')
        sql.set_db('messenger')
        sql.connect()
        sql.set_table('message')
        sql.set_colomn('sender','reciever','message')
        sql.set_values(sender, reciever, message)
        sql.insert()
        sql.set_default()
        print('message was sent !\n')
        break
