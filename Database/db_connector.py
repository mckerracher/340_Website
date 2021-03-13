import pymysql

h = "classmysql.engr.oregonstate.edu"
u = "cs340_mckerraj"
pw = ""
dbase = "cs340_mckerraj"


def connect_to_database(host=h, user=u, passwd=pw, datab=dbase):
    """This function provides a connection to the database."""
    db_connection = pymysql.connect(host=host,
                                    user=user,
                                    password=passwd,
                                    database=datab)
    return db_connection
