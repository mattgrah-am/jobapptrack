import bcrypt


def hashpassword(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def checkpassword(provided_password, password_hash):
    return bcrypt.checkpw(provided_password.encode(), password_hash.encode())
