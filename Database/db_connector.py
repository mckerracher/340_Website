import MySQLdb

# Database Info
host = "us-cdbr-east-03.cleardb.com"
user = "be5765a97239e1"
passwd = "6d4a5cc8"
db = "heroku_27223dfa0403044"
ssl_disabled = "True"


def connect_to_database(host=host, user=user, passwd=passwd, db=db, ssl_disabled= ssl_disabled):
    '''
    connects to a database and returns a database objects
    '''
    db_connection = MySQLdb.connect(host, user, passwd, db, ssl_disabled)
    return db_connection


if __name__ == '__main__':
    print(
        "Executing a sample query on the database using the credentials from db_credentials.py")
    db = connect_to_database()
    query = "SELECT * from game;"
    results = execute_query(db, query);
    print("Printing results of %s" % query)

    for r in results.fetchall():
        print(r)