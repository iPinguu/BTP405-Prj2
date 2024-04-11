import database.dbConn as dbConn
from . import hashPassword as hash
import json


db = dbConn.mongoConnection()
users = db['Restaurant']['users']

class userSchema:
    
    def __init__(self, name=None, email=None, password=None, role=None):
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.name,
            "password": self.password,
            "role": self.role
        }

def registerUser(userName, userEmail, userPwd):
    """
        Registers user in the database and encrypts their password
    """

    try:
        dbQuery = users.find_one(userName)
        Empty = len(list(dbQuery))

        if(not Empty):
            
            encryptedPwd = hash.serializePassword(userPwd)
            
            newUser = userSchema (
                name = userName,
                email = userEmail,
                password = encryptedPwd,
            )

            users.insert_one(newUser)
            return True
            
        else:
            raise Exception("User already exists!")
            

    except Exception as e:
        print(f'[Authentication Debugging]: guh, error: {e}')
        return False