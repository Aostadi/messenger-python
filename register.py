import class_file
# import send_email
import func
import send_message


def register():
    print(f"\t\t */-{'-'*10} REGISTER {'-'*10}-\*")
    user = input('*** Please enter user name  : ')
    email = input('*** Please enter email : ')
    chioce = input('do you want to continue (y/n): ').lower()
    if user == '' or email == '' or chioce != 'y':
        register()
    user_exist_result = func.check_user(user=user, email=email, want_sth=0)
    if user_exist_result != 0:
        print('Sorry !! User exist')
    else:
        # send = send_email.send_email(email)
        # send.send_code()
        insert_user(user, email)
        send_message.messager(user=user)


def insert_user(user, email):
    try:
        sql = class_file.Mysql(host='127.0.0.1', user='root')
        sql.set_db('messenger')
        sql.connect()
        sql.set_table('users')
        sql.set_colomn('user', 'email')
        sql.set_values(user, email)
        sql.insert()
        sql.set_default()
        print('\nsucess full registertion\n')
        # send = send_email.send_email(email)
        # send.sucess()
    except:
        print('some thing went wrong please try agian later')
