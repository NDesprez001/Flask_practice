## TESTING TO SEE IF I CAN IMPLEMENT THE LOGIN FUNCTION FROM PREVIOUS REPO. (Editing_user.file-w-python)

## LOGIN_FUNCTION 

def login_func():
    json = request.get_json()
    
    username = input('Enter username here:')
    password = input('Enter password here:')

    user_found = False
    for d in json:
        if d['first_name'] == username and d['password'] == password:
            print('Access granted')
            print(d)
            user_found = True
    if not user_found:
        print("User not found 404")