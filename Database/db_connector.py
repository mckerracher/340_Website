import pymysql

h = "us-cdbr-east-03.cleardb.com"
u = "be5765a97239e1"
pw = "VU^nX$#g!a&3NrSJU4YR"
dbase = "heroku_27223dfa0403044"


def connect_to_database(host=h, user=u, passwd=pw, datab=dbase):
    db_connection = pymysql.connect(host=host,
                             user=user,
                             password=passwd,
                             database=datab,
                             cursorclass=pymysql.cursors.DictCursor)
    return db_connection


if __name__ == '__main__':
    db = connect_to_database()
