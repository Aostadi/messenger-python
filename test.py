# import class_file
# connect = class_file.Mysql()
# connect.set_db('messenger')
# connect.connect()
# connect.select('email', 'phone')
# connect.set_table('hhhh')
# connect.where('email', '=', 'jjjj', 'and', 'phone', '=', 'nnn')
# connect.fecth('1')
# connect.set_colomn('email', 'passord', 'user', 'number')
# connect.set_values('email1', '123', 'abolfazl', '125478',)
# connect.insert()

import inspect


# def f1(): f2()


def f2():
    print( inspect.stack()[1][3])


