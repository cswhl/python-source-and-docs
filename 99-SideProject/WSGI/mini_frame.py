
def login():
    return 'hello world'

def register():
    return "register"

def application(file_name):
    if file_name == '/login.py':
        return login()
    elif file_name == '/register.py':
        return register()
    else:
        return 'not found'
