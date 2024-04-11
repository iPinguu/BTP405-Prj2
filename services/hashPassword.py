import bcrypt

def serializePassword(pwd):
    salt = bcrypt.gensalt()

    hashed = bcrypt.hashpw(pwd, salt)

    return hashed