import sys 
sys.path.insert(1, './database')

import dbConn

def registerUser(user, pwd):
    """
        Registers user to the database
    """

    # TODO: do register logic (create new document in db)


def authenticateUser(user, pwd):
    """
        Checks if user exists in the databse
    """

    # TODO: do authetication logic (check if user exists in db)
    print(f'[Authentication Log] User: {user}\n')
    print(f'[Authentication Log] Password: {pwd}\n')
