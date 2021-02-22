import MySQLdb

# Database Info



def connect_to_database(host=host, user=user, passwd=passwd, db=db):
    '''
    connects to a database and returns a database objects
    '''
    db_connection = MySQLdb.connect(host, user, passwd, db)
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