from bson import json_util
import json

import database.dbConn as dbConn
from . import hashPassword as hash

db = dbConn.mongoConnection()
users = db['Restaurant']['users']


def authenticateUser(user, pwd):
    """
        Checks if user exists in the databse
    """

    try:
        dbQuery = users.find_one(user)
        isEmpty = len(list(dbQuery))
        response = {"result": json.load(json_util(dict(dbConn)))}

        if(isEmpty):
            
            if(hash.checkPwd(pwd, response.password)):
                return True     
            else:
                raise Exception("Wrong password entered!") 
        else:
            return False
    except Exception as e:
        print(f'[Authentication Debugging]: guh, error: {e}')
