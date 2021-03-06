import pymysql

h = ""
u = ""
pw = ""
dbase = ""


def connect_to_database(host=h, user=u, passwd=pw, datab=dbase):
    db_connection = pymysql.connect(host=host,
                             user=user,
                             password=passwd,
                             database=datab,
                             cursorclass=pymysql.cursors.DictCursor)
    return db_connection


if __name__ == '__main__':
    db = connect_to_database()
