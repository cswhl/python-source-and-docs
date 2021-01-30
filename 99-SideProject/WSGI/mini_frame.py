
def login():
    return 'hello world'


def register():
    return "register"


def application(env, start_response):
    status = '200 ok'
    headers = [('Content-typ', 'text/html')]
    start_response(status, headers)

    file_name = env['path_info']
    if file_name == '/login.py':
        return login()
    elif file_name == '/register.py':
        return register()
    else:
        return 'not found'
