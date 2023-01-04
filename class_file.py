import mysql.connector


class Mysql:
    def __init__(sql, host='127.0.0.1', user='root', password=""):
        sql.__host = host
        sql.__user = user
        sql.__password = password
        sql.__offset_text = ''
        sql.__limit_text = ''
        sql.__order_by_text = ''
        sql.__asc = ''
        sql.__desc = ''

    def set_default(sql):
        sql.__table_select_text = ""
        sql.__table_other_text = ""
        sql.__where_text = ''
        sql.__col_text = ''
        sql.__values = ''
        sql.__select_text = ''
        sql.__offset_text = ''
        sql.__limit_text = ''
        sql.__order_by_text = ''

    def set_db(sql, database: str):
        sql.__db = database

    def connect(sql):
        try:
            sql.__connect = mysql.connector.connect(
                host=sql.__host, user=sql.__user, password=sql.__password, database=sql.__db)
            sql.__cursor = sql.__connect.cursor()
        except:
            print("can't connect to the servers")
            exit()

    def select(sql, *select: tuple):
        sql.__select = list(select)
        if sql.__select == ['*']:
            sql.__select_text = f"SELECT *"
        else:
            sql.__select_text = f"SELECT {','.join(sql.__select)}"

    def set_table(sql, table: str):
        sql.__table = table
        sql.__table_select_text = f" FROM {sql.__table} "
        sql.__table_other_text = f" `{sql.__table}` "

    def where(sql, *where):
        sql.__where = list(where)
        n = 0
        for t in sql.__where:
            if t not in ('=', 'and', 'or', 'is', 'not', 'LIKE', '1', 1, '%s'):
                if n % 3 == 0:
                    sql.__where[n] = f"`{t}`"
                else:
                    sql.__where[n] = f"'{t}'"
            n += 1
        sql.__where_text = f"WHERE {' '.join(sql.__where)} "

    def offset(sql, offset):
        sql.__offset = offset
        sql.__offset_text = f"OFFSET {sql.__offset}"

    def limit(sql, limit: int):
        sql.__limit = limit
        sql.__limit_text = f" LIMIT {sql.__limit} "

    def orderby(sql, order_by='', asc=0, desc=0):
        sql.__order_by = order_by
        if asc != 0 :
            sql.__asc = 'ASC'
        elif desc != 0:
            sql.__desc = 'DESC'
        sql.__order_by_text = f"ORDER BY {sql.__order_by} {sql.__asc}{sql.__desc} "

    def set_colomn(sql, *col):
        sql.__col = list(col)
        n = 0 
        for i in sql.__col:
            sql.__col[n] = f"`{sql.__col[n]}`"
            n += 1
        sql.__col_text = f"INSERT INTO {sql.__table_other_text} ({','.join(sql.__col)}) VALUES ({('%s,'*(len(sql.__col))).strip(',')}) "

    def set_values(sql, *values):
        sql.__values = values

    def insert(sql):
        try:
            sql.__cursor.execute(sql.__col_text, sql.__values)
            sql.__connect.commit()
        except:
            print('sth went wrong')
            exit()

    def fecth(sql, fetch_type='fecth all=2,fecth one=1'):
    # try:
        sql.__feth_text = f"""{sql.__select_text}{sql.__table_select_text}{sql.__where_text}{sql.__order_by_text}{sql.__limit_text}{sql.__offset_text}"""
        sql.__cursor.execute(sql.__feth_text)
        if fetch_type == 1:
            return sql.__cursor.fetchone()
        elif fetch_type == 2:
            return sql.__cursor.fetchall()
    # except:
        print("can't fetch data from server!")
