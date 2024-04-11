import bcrypt

def serializePassword(pwd):
    salt = bcrypt.gensalt()

    hashed = bcrypt.hashpw(pwd, salt)

    return hashed

def checkPwd(pwdToChck, hashedPwd):
    if checkPwd(pwdToChck, hashedPwd):
        return True
    return False