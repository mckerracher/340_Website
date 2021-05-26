import pymysql
import os

#Original Website

h = "us-cdbr-east-03.cleardb.com"
u = os.environ.get('DB_USER')
pw = os.environ.get('DB_PW')
dbase = "heroku_27223dfa0403044"

"""
#for running locally
#u = "be5765a97239e1"
#pw = "6d4a5cc8"
# local running
h = "us-cdbr-east-03.cleardb.com"
u = "be5765a97239e1"
pw = "6d4a5cc8"
dbase = "heroku_27223dfa0403044"
"""

def connect_to_database(host=h, user=u, passwd=pw, datab=dbase):
    """This function provides a connection to the database."""
    db_connection = pymysql.connect(host=host,
                                    user=user,
                                    password=passwd,
                                    database=datab)
    return db_connection
