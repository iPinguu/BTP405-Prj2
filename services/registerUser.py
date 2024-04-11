import database.dbConn as dbConn
import hashPassword as hash
import json


db = dbConn.mongoConnection()
users = db['Restaurant']['users']

class userSchema:
    
    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.name,
            "password": self.password
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

            users.insert_one({newUser})
            
        else:
            raise Exception("User already exists!")
            

    except Exception as e:
        print(f'[Authentication Debugging]: guh, error: {e}')