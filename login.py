import func
# import send_email
import send_message


def login():
    email = input('****** Please enter email : ')
    result = func.check_user(email=email, user=None,
                             want_sth=1, col_want='user')
    if result is not 0:
        # send_email.send_email(email=email)
        user_name = result['email'][0]
        send_message.messager(user=user_name)
    else:
        print('user doesn\'t exists please register ')
