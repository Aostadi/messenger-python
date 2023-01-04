import class_file


def check_user(email=None, user=None, col_want='id', want_sth=0):
    sql = class_file.Mysql(host='127.0.0.1', user='root')
    sql.set_db('messenger')
    sql.connect()
    sql.set_table('users')
    sql.select(col_want)

    if user == None and email == None:
        print('invalid email and user !')
        exit()
    if user != None:
        sql.where('user', '=', user)
        result_user = sql.fecth(1)
    else:
        result_user = None
    if email != None:
        sql.where('email', '=', email)
        result_email = sql.fecth(1)
    else:
        result_email = None

    sql.set_default()
    info_dic = {}
    if result_email is None and result_user is None:
        return 0
    else:
        if want_sth != 0:
            info_dic['user'] = result_user
            info_dic['email'] = result_email
            return info_dic
        return 1
