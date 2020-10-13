from sql import connect,select

connect()

def user_get(name):
    return select(name)